from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Updated coddddddddddddddddddddddddddd"
@app.route("/app")
def hello1():
    return "Sonarscan"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
