from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
FOLDER = 'mtom'
os.makedirs(FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('file')
    if f:
        f.save(os.path.join(FOLDER, f.filename))
        return {"message": f"{f.filename} uploaded"}
    return {"error": "No file uploaded"}, 400

@app.route('/download/<name>')
def download(name):
    try:
        return send_from_directory(FOLDER, name, as_attachment=True)
    except:
        return {"error": "File not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)