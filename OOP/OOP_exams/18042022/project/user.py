
class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == '':
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value


    def __str__(self):
        user = f"Username: {self.username}, Age: {self.age}"
        liked = [x.details() for x in self.movies_liked]
        owned = [y.details() for y in self.movies_owned]
        result_liked = ''
        if liked:
            result_liked = '\n'.join(liked)
        else:
            result_liked = "No movies liked."
        liked_movies = f"Liked movies:" + '\n' + result_liked
        result_owned = ''
        if owned:
            result_owned = '\n'.join(owned)
        else:
            result_owned = "No movies owned."
        owned_movies = "Owned movies:" + '\n' + result_owned
        return user + '\n' + liked_movies + '\n' + owned_movies

