from wild_zoo.project import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if self.name == player.guild:
            return f"Player {player.name} is already in the guild."
        if player.guild != player.DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for item in self.players:
            if player_name == item.name:
                item.guild = item.DEFAULT_GUILD
                self.players.remove(item)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        return 'Guild: ' + self.name + '\n' +'\n'.join([x.player_info() for x in self.players])

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())