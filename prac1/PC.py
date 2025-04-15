from flask import Flask, request, jsonify 

app = Flask(__name__) 

def is_prime(n): 
    # Handle simple cases
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    
    # Check odd divisors only
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

@app.route('/check_prime')
def check_prime():
    try:
        number = int(request.args.get('number', 0))
        return jsonify({"number": number, "is_prime": is_prime(number)})
    except:
        return jsonify({"error": "Invalid input"})
if __name__ == '__main__':
    app.run(debug=True)