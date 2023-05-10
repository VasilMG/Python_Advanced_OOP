from wild_zoo.project import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for p in self.pokemons:
            if p.name == pokemon_name:
                self.pokemons.remove(p)
                return f"You have released {pokemon_name}"
        else:
            return f"Pokemon is not caught"

    def trainer_data(self):
        return 'Pokemon Trainer ' + self.name +\
            '\n' + 'Pokemon count ' + str(len(self.pokemons)) + '\n- ' +\
            '\n- '.join([Pokemon.pokemon_details(x) for x in self.pokemons])

pokemon1 = Pokemon("Gosho", 900)
pokemon = Pokemon("Pikachu", 90)

print(pokemon.pokemon_details())

trainer = Trainer("Ash")

print(trainer.add_pokemon(pokemon))
print(trainer.add_pokemon(pokemon1))

second_pokemon = Pokemon("Charizard", 110)

print(trainer.add_pokemon(second_pokemon))

print(trainer.add_pokemon(second_pokemon))

print(trainer.release_pokemon("Pikachu"))

print(trainer.release_pokemon("Pikachu"))

print(trainer.trainer_data())
