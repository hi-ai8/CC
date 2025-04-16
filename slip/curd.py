# app.py ///////////////////////////////////////
from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__) 
# Configure MySQL database connection (no password required if MySQL is set up like that) 
app.config['SQLALCHEMY_DATABASE_URI'] = 
'mysql://root:aniket@localhost/player_db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
 
db = SQLAlchemy(app) 
 
# Define the Player model 
class Player(db.Model): 
    __tablename__ = 'players' 
    id = db.Column(db.Integer, primary_key=True) 
    player_name = db.Column(db.String(100), nullable=False) 
 
    age = db.Column(db.Integer, nullable=False) 
    country = db.Column(db.String(100), nullable=False) 
    runs = db.Column(db.Integer, nullable=False) 
 
# Create tables when app starts 
with app.app_context(): 
    db.create_all() 
 
# Create a player 
@app.route('/player', methods=['POST']) 
def create_player(): 
    data = request.json 
    player = Player(**data) 
    db.session.add(player) 
    db.session.commit() 
    return jsonify({"message": "Player created successfully"}), 201 
 
# Get all players 
@app.route('/players', methods=['GET']) 
def get_players(): 
    players = Player.query.all() 
    return jsonify([{ 
        "id": p.id, "player_name": p.player_name, "age": p.age,  
        "country": p.country, "runs": p.runs 
    } for p in players]) 
 
# Update a player 
@app.route('/player/<int:id>', methods=['PUT']) 
def update_player(id): 
    player = Player.query.get(id) 
    if not player: 
        return jsonify({"message": "Player not found"}), 404 
 
    data = request.json 
    for key, value in data.items(): 
        setattr(player, key, value) 
 
    db.session.commit() 
    return jsonify({"message": "Player updated successfully"}) 
 
# Delete a player 
@app.route('/player/<int:id>', methods=['DELETE']) 
def delete_player(id): 
    player = Player.query.get(id) 
    if not player: 
        return jsonify({"message": "Player not found"}), 404 
 
    db.session.delete(player) 
    db.session.commit() 
    return jsonify({"message": "Player deleted successfully"}) 
 
if __name__ == '__main__': 
    app.run(debug=True) 
 
# test_app.py ///////////////////////////////////////
from app import db, Player, app 
def create_player(): 
    new_player = Player(player_name="MS Dhoni", age=35, country="India", runs=120) 
    db.session.add(new_player) 
    db.session.commit() 
    print(f"Player created: {new_player.player_name}") 
 
def get_all_players(): 
    players = Player.query.all() 
    print("All players in DB:") 
 
    for player in players: 
        print(f"{player.id}: {player.player_name}, {player.age}, {player.country}, {player.runs}") 
 
def update_player(player_id): 
    player = db.session.get(Player, player_id)  
    if player: 
        player.player_name = "Rohit Sharma" 
        db.session.commit() 
        print(f"Updated player {player.id} ") 
    else: 
        print("Player not found!") 
 
def delete_player(player_id): 
    player = db.session.get(Player, player_id)  
    if player: 
        db.session.delete(player) 
        db.session.commit() 
        print(f"Deleted player {player.player_name}") 
    else: 
        print("Player not found!") 
 
if __name__ == "__main__": 
    with app.app_context(): 
        create_player() 
        get_all_players() 
        update_player(1) 
        get_all_players()