from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_data():
    text = request.form['username']
    password = request.form['pass']
    if(text == 'nikhil' and password == '123'):
        return f'username {text} password {password}'
    else:
        return f'invalid credentials'


if __name__ == '__main__':
    app.run(debug=True, port=8083)