from flask import Flask, request, jsonify 

app = Flask(__name__) 

@app.route('/factorial') 
def factorial(): 
    try: 
        n = int(request.args.get('n', 0))
        result = 1
        for i in range(2, n+1): 
            result *= i 
        return jsonify({"factorial": result}) 
    except: 
        return jsonify({"error": "Invalid input"})

if __name__ == '__main__': 
    app.run(debug=True)
