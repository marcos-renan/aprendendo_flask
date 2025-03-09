from flask import Flask

app = Flask()

#Criando primeira rota
@app.route("/")
def home():
    return "Hello World"