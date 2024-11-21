from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def home():
    return "<p>Welcome Home -----  </p>"

if __name__ == '__main__':
    app.run(debug = True)