from flask import Flask, render_template, request


app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Super Mário', 'Ação', 'SNES')
jogo2 = Jogo('Teris', 'Ação', 'SNES')
jogo3 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo4 = Jogo('Mortal Komat', 'Luta', 'SNES')

lista = [jogo1, jogo2, jogo3, jogo4 ]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Games', jogos=lista )

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo' )


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return render_template('lista.html', titulo='Games', jogos=lista)

app.run(debug=True)