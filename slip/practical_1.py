from flask import Flask, request, jsonify

app = Flask(__name__)
# conversion_rate = 0.012
conversion_rate = 1/85.70

@app.route('/', methods=['GET'])
def hello():
    return "Hello, This is the currency converter API"

@app.route('/convert', methods=['GET'])
def convert_currency():
    inr = request.args.get('inr')
    if not inr:
        return jsonify({"error": "INR amount missing"}), 400
    try:
        inr_value = float(inr)
        return jsonify({"INR": inr_value, "USD": inr_value * conversion_rate})
    except ValueError:
        return jsonify({"error": "Invalid INR amount"}), 400

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Conversion function
# def fahrenheit_to_celsius(f):
#     return (f - 32) * 5.0 / 9.0

# @app.route('/')
# def home():
#     return "Welcome! Use /convert?fahrenheit=value to convert Fahrenheit to Celsius."

# @app.route('/convert', methods=['GET'])
# def convert():
#     f = request.args.get('fnt')
#     if not f:
#         return jsonify({"error": "Missing 'fahrenheit' parameter"}), 400
#     try:
#         f = float(f)
#         c = fahrenheit_to_celsius(f)
#         return jsonify({
#             "fahrenheit": f,
#             "celsius": round(c, 2),
#             "message": f"{f}F is equal to {round(c, 2)}C"
#         })
#     except ValueError:
#         return jsonify({"error": "Invalid temperature value"}), 400

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, request, jsonify

# app = Flask(__name__)

# def is_prime(n):
#     if n <= 1:
#         return False  # 0 and 1 are not prime numbers
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False  # If divisible by any number other than 1 and itself
#     return True

# @app.route('/', methods=['GET'])
# def hello():
#     return "Hello, this is for checking whether a number is prime or not."

# @app.route('/isprime', methods=['GET'])
# def check_prime():
#     num = request.args.get('num')
#     if not num:
#         return jsonify({"error": "Number is missing"}), 400
#     try:
#         num = int(num)  # Convert from string to int
#         result = is_prime(num)
#         message = f"{num} is {'a prime' if result else 'not a prime'} number."
#         return jsonify({
#             "number": num,
#             "is_prime": result,
#             "message": message
#         })
#     except ValueError:
#         return jsonify({"error": "Invalid number"}), 400

# if __name__ == '__main__':
#     app.run(debug=True)


# new file name should be rupee_converter_client.py

# import java.io.BufferedReader;
# import java.io.InputStreamReader;
# import java.net.HttpURLConnection;
# import java.net.URL;

# public class RupeeConverterClient {
#     public static void main(String[] args) throws Exception {
#         String rupees = "89";
#         // String rupees = "85.70";
#         @SuppressWarnings("deprecation")
#         // URL url = new URL("http://127.0.0.1:5000/convert?fnt=" + rupees);
#         URL url = new URL("http://127.0.0.1:5000/isprime?num=" + rupees);
#         // URL url = new URL("http://localhost:5000/convert?inr=" + rupees);
#         HttpURLConnection conn = (HttpURLConnection) url.openConnection();
#         conn.setRequestMethod("GET");

#         BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
#         String inputLine, response = "";

#         while ((inputLine = in.readLine()) != null) {
#             response += inputLine;
#         }
#         in.close();

#         System.out.println("Response from server: " + response);
#     }
# }
