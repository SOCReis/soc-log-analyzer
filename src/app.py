
from flask import Flask, render_template
from analisador import analisar_log

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def dashboard():
    dados = analisar_log()
    return render_template("dashboard.html", dados=dados)

if __name__ == "__main__":
    app.run(debug=True)
