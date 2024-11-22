from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        email = request.form.get('email')    
        message = request.form.get('message')

        print(f'Email {email}')
        print(f'Message {message}')

        if not email or not message:
            return render_template('error.html')

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug = True, port = 8989)

