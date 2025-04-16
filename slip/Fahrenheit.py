from flask import Flask, request, jsonify

app = Flask(__name__)

# Conversion function
def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0

@app.route('/')
def home():
    return "Welcome! Use /convert?fahrenheit=value to convert Fahrenheit to Celsius."

@app.route('/convert', methods=['GET'])
def convert():
    f = request.args.get('fnt')
    if not f:
        return jsonify({"error": "Missing 'fahrenheit' parameter"}), 400
    try:
        f = float(f)
        c = fahrenheit_to_celsius(f)
        return jsonify({
            "fahrenheit": f,
            "celsius": round(c, 2),
            "message": f"{f}F is equal to {round(c, 2)}C"
        })
    except ValueError:
        return jsonify({"error": "Invalid temperature value"}), 400

if __name__ == '__main__':
    app.run(debug=True)

