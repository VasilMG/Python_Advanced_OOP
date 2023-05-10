from project.user import User
from project.movie_specification.movie import Movie


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __check_user_owner(self, user: User, movie: Movie):
        if movie.owner != user:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")
        return True
    # --------------------------------------------------------------------------------------------
    def check_if_user_exists(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False

    def check_if_movie_exists(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def check_if_user_liked_movie(self, username, movie_title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == movie_title:
                        return True
                return False

    #-----------------------------------------------------------------------------------------------


    def register_user(self, username: str, age: int):
        names = [x.username for x in self.users_collection]
        if username in names:
            raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."


    def upload_movie(self, username: str, movie: Movie):
        user = next((filter(lambda x: x.username == username, self.users_collection)), None)
        if not user:
            raise Exception("This user does not exist!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        u = user
        mo = movie.owner
        print(u == mo)
        print(u != mo)
        # no fucking idea why
        if user != movie.owner:
            print('whyyyyyyyyy')
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."



    def like_movie(self, username, movie):
        if username == movie.owner.username:
            raise Exception(f'{username} is the owner of the movie {movie.title}!')
        elif self.check_if_user_liked_movie(username, movie.title):
            raise Exception(f'{username} already liked the movie {movie.title}!')
        else:
            movie.likes += 1
            for user in self.users_collection:
                if user.username == username:
                    user.movies_liked.append(movie)
            return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username, movie):
        if not self.check_if_user_liked_movie(username, movie.title):
            raise Exception(f'{username} has not liked the movie {movie.title}!')
        else:
            movie.likes -= 1
            for user in self.users_collection:
                if user.username == username:
                    user.movies_liked.pop(user.movies_liked.index(movie))
            return f'{username} disliked {movie.title} movie.'

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return 'No movies found.'
        else:
            result_str = []
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                result_str.append(movie.details())
            return '\n'.join(result_str)

    def __str__(self):
        if len(self.users_collection) == 0:
            users = 'No users.'
        else:
            users = ', '.join([user.username for user in self.users_collection])
        if len(self.movies_collection) == 0:
            movies = 'No movies.'
        else:
            movies = ', '.join([movie.title for movie in self.movies_collection])

        return f'All users: {users}\nAll movies: {movies}'


    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie  not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = next((filter(lambda x: x.username == username, self.users_collection)), None)
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for key, value in kwargs.items():

            if key == 'title':
                movie.title = value
            elif key == 'year':
                movie.year = value
            elif key == 'age_restriction':
                movie.age_restriction = value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = next((filter(lambda x: x.username == username, self.users_collection)), None)
        if user != movie.owner:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

