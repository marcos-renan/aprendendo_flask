from flask import Flask

app = Flask(__name__)

#Criando primeira rota
@app.route("/")
def home():
    return "Hello World, I love Jesus!"

#Criando segunda rota
@app.route("/login")
def login():
    return "Tela de login"

#Criando rota dinamica
@app.route("/account")
@app.route("/account/<nome>")
@app.route("/account/<nome>/<int:userId>")
def account(nome=None, userId=None):
    #condição que verifica os valores recebidos na url
    if nome and userId:
        return f"Bem vindo {nome}, seu id é {userId}"
    elif nome:
        return f"Bem vindo {nome}, você ainda não possui id."
    else:
        return f"Faça login!"

if __name__ == '__main__' :
    app.run(debug=True)