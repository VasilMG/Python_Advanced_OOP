class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []
        self.food = []
        self.drinks = []

    def add_player(self, *args):
        newly_added = []
        for pl in args:
            if pl not in self.players:
                self.players.append(pl)
                newly_added.append(pl)
        return f"Successfully added: " + ', '.join([x.name for x in newly_added])

    def add_supply(self, *args):
        for sup in args:
            self.supplies.append(sup)
            if sup.type == "Food":
                self.food.append(sup)
            elif sup.type == "Drink":
                self.drinks.append(sup)

    def sustain(self, player_name: str, sustenance_type: str):
        player_names = set()
        for p in self.players:
            player_names.add(p.name)
        if player_name not in player_names or sustenance_type not in ["Food", "Drink"]:
            return
        if sustenance_type == 'Food' and not self.food:
            raise Exception("There are no food supplies left!")
        if sustenance_type == 'Drink' and not self.drinks:
            raise Exception("There are no drink supplies left!")

        current_player = ''
        for c_player in self.players:
            if c_player.name == player_name:
                current_player = c_player
                break
        if current_player.need_sustenance == False:
            return f"{player_name} have enough stamina."

        if sustenance_type == 'Food':
            the_food = self.food.pop()
            new_stamina = current_player.stamina + the_food.energy
            self.supplies.remove(the_food)
            if new_stamina > 100:
                current_player.stamina = 100
            else:
                current_player.stamina = new_stamina
            return f"{player_name} sustained successfully with {the_food.name}."
        if sustenance_type == 'Drink':
            the_drink = self.drinks.pop()
            new_stamina = current_player.stamina + the_drink.energy
            self.supplies.remove(the_drink)
            if new_stamina > 100:
                current_player.stamina = 100
            else:
                current_player.stamina = new_stamina
            return f"{player_name} sustained successfully with {the_drink.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        left_player = ''
        right_player = ''
        for pl in self.players:
            if pl.name == first_player_name:
                left_player = pl
            if pl.name == second_player_name:
                right_player = pl
        if left_player.stamina == 0 and right_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina." + '\n' \
                + f"Player {second_player_name} does not have enough stamina."
        if left_player.stamina == 0 and right_player.stamina != 0:
            return f"Player {first_player_name} does not have enough stamina."
        if left_player.stamina != 0 and right_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        first_attacker = ''
        second_attacker = ''
        if left_player.stamina < right_player.stamina:
            first_attacker = left_player
            second_attacker = right_player
        else:
            first_attacker = right_player
            second_attacker = left_player

        the_second_stamina = second_attacker.stamina - first_attacker.stamina / 2
        if the_second_stamina <= 0:
            second_attacker.stamina = 0
            return f"Winner: {first_attacker.name}"
        else:
            second_attacker.stamina = the_second_stamina


        the_first_stamina = first_attacker.stamina - second_attacker.stamina / 2
        if the_first_stamina <= 0:
            first_attacker.stamina = 0
            return f"Winner: {second_attacker.name}"
        else:
            first_attacker.stamina = the_first_stamina

        winner = first_attacker if first_attacker.stamina > second_attacker.stamina else second_attacker
        return f"Winner: {winner.name}"

    def next_day(self):
        for pl in self.players:
            new_stamina = pl.stamina - pl.age * 2
            if new_stamina <= 0:
                pl.stamina = 0
            else:
                pl.stamina = new_stamina
            self.sustain(pl.name, "Food")
            self.sustain(pl.name, "Drink")

    def __str__(self):
        return '\n'.join([str(x) for x in self.players]) + '\n' + '\n'.join([s.details() for s in self.supplies])


