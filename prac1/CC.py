from flask import Flask, request, jsonify 
 
app = Flask(__name__) 
@app.route('/convert') 
def convert(): 
    try: 
        inr = float(request.args['inr']) 
        return jsonify(INR=inr, USD=round(inr * 0.012, 4)) 
    except: 
        return jsonify(error="Invalid INR amount"), 400 
 
if __name__ == '__main__': 
    app.run(debug=True) 