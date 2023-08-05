import requests

class GetPoke:
    def __init__(self,pokemon_name=None):
        self.url = 'https://pokeapi.co/api/v2/pokemon/'
        self.pkmn = None if not pokemon_name else self.request(pokemon_name)

    def request(self, pokemon_name):
        pokemon_name = str(pokemon_name)
        request_url = f'{self.url}{pokemon_name.lower()}/'
        response = requests.get(request_url)

        if response.status_code == 200:
            self.pkmn = response.json()
            return self.pkmn
        
        return None
    
    def get(self, pokemon_name=None): 

        pokemon = self.pkmn if self.pkmn else self.request(pokemon_name)
        type1 = pokemon['types'][0]['type']['name']
        type2 = pokemon['types'][1]['type']['name'] if len(pokemon["types"]) >= 2 else None

        pokemon_json = {
            "name": pokemon['species']['name'],
            "id": pokemon['id'],
            "artwork": pokemon['sprites']['other']['official-artwork']['front_default'],

            "types": {
                "type1": type1,
                "type2": type2
            },

            "height": {
                "decimeter": round(pokemon['height'],2),
                "centimeter": round(pokemon['height'] * 10, 2),
            },

            "weight": {
                "hectogram": round(pokemon['weight']),
                "kilograms": round(pokemon['weight'] / 10, 2),
            }
        }

        return pokemon_json

class PokeApi:
    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name
        self.getpoke = GetPoke(pokemon_name=self.pokemon_name)

    def pokemon(self, pokemon_name):
        self.pokemon_name = pokemon_name
        self.getpoke = GetPoke(pokemon_name=self.pokemon_name)
        return self.getpoke.get()

    def show(self):
        return self.getpoke.get()