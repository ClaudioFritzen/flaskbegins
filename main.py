from flask import Flask, render_template

app = Flask(__name__)


# criar a 1° pagina do site

#toda pagina sempre tem um route e uma função

# route -> é o dominio apos o .com/alguma coisa

# função -> o que voce quer exibir naquela página

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# COLOCAR O SITE NO AR

if __name__ == "__main__":
    app.run(debug=True)

# pip freeze > requiremens.txt