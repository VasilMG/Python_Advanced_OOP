from wild_zoo.project import Song
class Album:
    def __init__(self, name, *args: Song):
        self.name = name
        self.args = args
        self.published = False
        self.songs = [x for  x in self.args]

    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."
        if self.published == True:
            return "Cannot add songs. Album is published."
        if song.single == True:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published == True:
            return "Cannot remove songs. Album is published."

        for item in self.songs:
            if song_name == item.name:
                self.songs.remove(item)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published == True:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return 'Album ' + self.name + '\n' + '\n'.join([f'== {x.get_info()}' for x in self.songs])

