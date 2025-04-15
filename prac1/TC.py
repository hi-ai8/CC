from flask import Flask, request, jsonify 
 
app = Flask(__name__) 
 
@app.route('/convert') 
def convert(): 
    scale = request.args.get('scale', '').lower()
    value = request.args.get('value')
    
    try: 
        value = float(value)
        if scale == 'celsius': 
            return jsonify({"c": value, "f": value * 9/5 + 32}) 
        if scale == 'fahrenheit': 
            return jsonify({"f": value, "c": (value - 32) * 5/9}) 
        return jsonify({"error": "Invalid scale"})
    except: 
        return jsonify({"error": "Invalid input"})
 
if __name__ == '__main__': 
    app.run(debug=True)