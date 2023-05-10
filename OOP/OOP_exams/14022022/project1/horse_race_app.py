# from project1.horse_specification.horse import Horse
from project1.horse_specification.appaloosa import Appaloosa
from project1.horse_specification.thoroughbred import Thoroughbred
from project1.jockey import Jockey
from project1.horse_race import HorseRace

class HorseRaceApp:
    TYPE_HORSES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}


    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def find_horse(self, horse_type_):
        found_horse = next(
            filter(lambda x: (type(x).__name__ == horse_type_ and not x.is_taken), reversed(self.horses)),
            None
        )
        if not found_horse:
            raise Exception(f"Horse breed {horse_type_} could not be found!")
        return found_horse

    def find_jockey(self, jockey_name_):
        found_jockey = next(filter(lambda x: x.name == jockey_name_, self.jockeys), None)
        if not found_jockey:
            raise Exception(f"Jockey {jockey_name_} could not be found!")
        return found_jockey

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        names = [x.name for x in self.horses]
        if horse_type not in self.TYPE_HORSES.keys():
            return
        if horse_name in names:
            raise Exception(f"Horse {horse_name} has been already added!")
        new_horse = self.TYPE_HORSES[horse_type](horse_name, horse_speed)
        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        names = [x.name for x in self.jockeys]
        if jockey_name in names:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        else:
            new_jockey = Jockey(jockey_name, age)
            self.jockeys.append(new_jockey)
            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        types = [x.race_type for x in self.horse_races]
        if race_type in types:
            raise Exception(f"Race {race_type} has been already created!")
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."


    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        j_names = [x.name for x in self.jockeys]
        type_h = [h for h in self.horses if h.__class__.__name__ == horse_type and not h.is_taken]
        if jockey_name not in j_names:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not type_h:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        the_jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        if the_jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        the_horse = type_h.pop()
        the_jockey.horse = the_horse
        the_horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {the_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        types = [t.race_type for t in self.horse_races]
        j_names = [j.name for j in self.jockeys]
        if race_type not in types:
            raise Exception(f"Race {race_type} could not be found!")
        if jockey_name not in j_names:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."


    def start_horse_race(self, race_type: str):
        types = [t.race_type for t in self.horse_races]
        if race_type not in types:
            raise Exception(f"Race {race_type} could not be found!")
        race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        finish = sorted(self.jockeys, key=lambda j: j.horse.speed)
        winner = finish[-1]
        return f"The winner of the {race_type} race, " \
               f"with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."





