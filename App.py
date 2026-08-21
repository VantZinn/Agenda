from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


def calcular_revisao(dia, mes, ano):
    novo_mes = mes + 6

    if novo_mes > 12:
        novo_mes -= 12
        ano += 1

    return dia, novo_mes, ano


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        cliente = request.form["cliente"]
        telefone = request.form["telefone"]
        endereco = request.form["endereco"]
        aparelho = request.form["aparelho"]

        dia = int(request.form["dia"])
        mes = int(request.form["mes"])
        ano = int(request.form["ano"])

        observacao = request.form["observacao"]

        dia_revisao, mes_revisao, ano_revisao = calcular_revisao(
            dia, mes, ano
        )

        return f"""
        <h2>Cliente cadastrado</h2>

        <p>Cliente: {cliente}</p>
        <p>Telefone: {telefone}</p>
        <p>Endereço: {endereco}</p>
        <p>Aparelho: {aparelho}</p>

        <p>
        Próxima manutenção:
        {dia_revisao}/{mes_revisao}/{ano_revisao}
        </p>

        <p>Observação: {observacao}</p>
        """

    return render_template("cadastro.html")


app.run(debug=True)