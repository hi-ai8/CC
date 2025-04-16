from pickletools import stringnl
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello, This is the calculator API"

@app.route('/add', methods=['GET'])

def add_numbers():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    
    # Calculate the sum
    result = num1 + num2
    
    # Return the result as JSON
    # return jsonify({"result": result})
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
