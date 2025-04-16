from flask import Flask, request, jsonify

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # If divisible by any number other than 1 and itself
    return True

@app.route('/', methods=['GET'])
def hello():
    return "Hello, this is for checking whether a number is prime or not."

@app.route('/isprime', methods=['GET'])
def check_prime():
    num = request.args.get('num')
    if not num:
        return jsonify({"error": "Number is missing"}), 400
    try:
        num = int(num)  # Convert from string to int
        result = is_prime(num)
        message = f"{num} is {'a prime' if result else 'not a prime'} number."
        return jsonify({
            "number": num,
            "is_prime": result,
            "message": message
        })
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

if __name__ == '__main__':
    app.run(debug=True)
