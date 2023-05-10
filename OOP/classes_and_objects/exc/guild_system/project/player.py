class Player:
    DEFAULT_GUILD = "Unaffiliated"
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = self.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills.keys():
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        return 'Name: ' + self.name + '\n' + 'Guild: ' + self.guild +\
            '\n' + 'HP: ' + str(self.hp) +'\n' + 'MP: ' + str(self.mp) + '\n' +\
            '\n'.join(f'==={k} - {v}' for k, v in self.skills.items())