from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Welcome page </h1>'

if __name__ == 'main':
    app.run(debug = True)


