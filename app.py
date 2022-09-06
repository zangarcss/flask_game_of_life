from flask import Flask, render_template
import game_of_life

app = Flask(__name__)


@app.route('/')
def index():
    game_of_life.GameOfLife(15, 15)
    return render_template('index.html')


@app.route('/live')
def live():
    game = game_of_life.GameOfLife()
    if game.counter > 0:
        game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game=game)


if __name__ == '__main__':
    app.run(debug=True)
