
class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for _ in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count: int):
        if photos_count % 4 == 0:
            return cls(photos_count // 4)
        return cls((photos_count // 4) + 1)

    def add_photo(self, label:str):
        for r in range(len(self.photos)):
            if len(self.photos[r]) < 4:
                self.photos[r].append(label)
                return f"{label} photo added successfully on page {r+1} slot {len(self.photos[r])}"
            else:
                continue
        return f"No more free slots"

    def display(self):
        return '-----------\n'+ \
            '\n-----------\n'.join([' '.join(["[]" if x is not None else '' for x in j]) for j in self.photos]) +\
            '\n-----------'


