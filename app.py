from flask import Flask

app = Flask(__name__)

#Criando primeira rota
@app.route("/")
def home():
    return "Hello World, I love Jesus!"

@app.route("/login")
def login():
    return "Tela de login"

if __name__ == '__main__' :
    app.run(debug=True)