from flask import Flask, render_template

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/inicio')
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Ataria')
    jogo2 = Jogo('God of War', "Hack n'slash", 'PS2')
    jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html',
                           titulo='Jogos',
                           jogos=lista)


if __name__ == '__main__':
    app.run()
