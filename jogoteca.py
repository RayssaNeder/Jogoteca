from flask import Flask, render_template


app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Super Mário', 'Ação', 'SNES')
    jogo2 = Jogo('Teris', 'Ação', 'SNES')
    jogo3 = Jogo('Pokemon Gold', 'RPG', 'GBA')
    jogo4 = Jogo('Mortal Komat', 'Luta', 'SNES')

    lista = [jogo1, jogo2, jogo3, jogo4 ]
    return render_template('lista.html', titulo='Games', jogos=lista )

app.run()