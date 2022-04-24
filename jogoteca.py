from flask import Flask, render_template


app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = ['Tetris', 'Super Mário', 'Pokemon Gold']
    return render_template('lista.html', titulo='Games', jogos=lista )

app.run()