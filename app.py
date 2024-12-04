from flask import Flask, render_template, request
import bcrypt

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hash_password', methods=['POST'])
def hash_password():
    password = request.form['password']
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return render_template('index.html', hashed_password=hashed_password.decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True)
