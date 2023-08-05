from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session
from blueprints.pokeapi.pokeapi import pokeapi
from os import getenv

app = Flask(__name__)
app.register_blueprint(pokeapi)

app.config['SECRET_KEY'] = getenv('SESSION_SECRETKEY')
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():

    return render_template('index.html',pokemon=dict(session['last_pokemon']))

@app.route('/cache/create/pokemon', methods=["POST","GET"])
def pokemon_cache():
    session['last_pokemon'] = request.args

    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)