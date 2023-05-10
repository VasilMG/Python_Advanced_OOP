from wild_zoo.project import Album


class Band:
    ALBUMS = []
    def __init__(self, name):
        self.name = name
        self.albums = self.ALBUMS

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for item in self.albums:
            if album_name == item.name:
                if item.published == True:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(item)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        return 'Band ' + self.name + '\n' + '\n'.join([x.details() for x in self.albums])

