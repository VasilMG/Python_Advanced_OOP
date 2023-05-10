from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.band_members.drummer import Drummer
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.concerts = []
        self.musicians = []
        self.bands = []
        self.all_types = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ["Guitarist", "Drummer", "Singer"]:
            raise ValueError("Invalid musician type!")
        names = [x.name for x in self.musicians]
        if name in names:
            raise Exception(f"{name} is already a musician!")
        new_musician = self.all_types[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band_names = [x.name for x in self.bands]
        if name in band_names:
            raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if place == concert.place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        for musician in self.musicians:
            if musician_name == musician.name:
                new_musician = musician
                break
        else:
            raise Exception(f"{musician_name} isn't a musician!")

        for band in self.bands:
            if band_name == band.name:
                new_band = band
                break
        else:
            raise Exception(f"{band_name} isn't a band!")

        new_band.members.append(new_musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        searched_band = [x for x in self.bands if x.name == band_name]
        if searched_band == []:
            raise Exception(f"{band_name} isn't a band!")
        current_band = searched_band[0]
        searched_musician = [x for x in current_band.members if x.name == musician_name]
        if searched_musician == []:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        current_musician = searched_musician[0]

        current_band.members.remove(current_musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        the_band = [x for x in self.bands if x.name == band_name][0]
        members_types = [x.__class__.__name__ for x in the_band.members]
        if 'Guitarist' not in members_types or 'Drummer' not in members_types \
                or 'Singer' not in members_types:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        the_concert = [x for x in self.concerts if x.place == concert_place][0]
        # band_skills = [z[0] for z in [[x for x in y.skills] for y in the_band.members]]
        if the_concert.genre == 'Rock':
            for band_member in the_band.members:
                if band_member.__class__.__name__ == 'Drummer' and \
                        "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing high pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play rock" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif the_concert.genre == 'Metal':
            for band_member in the_band.members:
                if band_member.__class__.__name__ == 'Drummer' and "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif the_concert.genre == 'Jazz':
            for band_member in the_band.members:
                if band_member.__class__.__name__ == 'Drummer' \
                        and "play the drums with drum brushes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' \
                        and ("sing low pitch notes" not in band_member.skills
                             or "sing high pitch notes" not in band_member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        # band_skills = []
        # for member in the_band.members:
        #     for skill in member.skills:
        #         band_skills.append(skill)
        # if the_concert.genre == 'Rock':
        #     for skill in the_concert.get_needed_skills():
        #         if skill not in band_skills:
        #             raise Exception(f"The {band_name} band is not ready to play at the concert!")
        # elif the_concert.genre == 'Metal':
        #     for skill in the_concert.get_needed_skills():
        #         if skill not in band_skills:
        #             raise Exception(f"The {band_name} band is not ready to play at the concert!")
        # elif the_concert.genre == 'Jazz':
        #     for skill in the_concert.get_needed_skills():
        #         if skill not in band_skills:
        #             raise Exception(f"The {band_name} band is not ready to play at the concert!")
        profit = the_concert.audience * the_concert.ticket_price - the_concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {the_concert.genre} concert in {the_concert.place}."

