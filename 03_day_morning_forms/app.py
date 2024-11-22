from flask import Flask, render_template

app = Flask(__name__)


@app.route('/form', methods = ['GET', 'POST'])
def form():
    ...

if __name__ == '__main__':
    app.run(debug = True)

