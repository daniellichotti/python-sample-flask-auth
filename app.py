from flask import Flask, jsonify, request
from models.user import User
from database import db
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

# TODO view login

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        # login
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            return jsonify({'message': 'Autenticação realizada com sucesso'}), 200
            
    return jsonify({'message': 'Credenciais invalidas'}), 400

@app.route('/hello-world')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)