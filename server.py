from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/somar/<v1>/<v2>")
def somar(v1,v2):

    v1 = int(v1)
    v2 = int(v2)

    resposta = v1+v2

    return str(resposta)

app.run(port=5000, host="0.0.0.0")