from blueprints.pokeapi.pokeclass import PokeApi
from flask import Blueprint, request, redirect, url_for

pokeapi = Blueprint('pokeapi', __name__)
query = PokeApi(None)

@pokeapi.route('/api/pokemon/')
def SearchPokemon():
    try:
        query.pokemon(request.args.get('query'))

        return redirect(url_for('pokemon_cache',**query.show()))
    
    except Exception as e:
        print("Error:", e)
        return "error"