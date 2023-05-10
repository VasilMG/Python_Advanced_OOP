from project.movie import Movie
import unittest
from unittest import TestCase

class TestMovie(TestCase):
    def test_init_when_correct(self):
        movie = Movie('Internship', 2002, 9.6)
        self.assertEqual('Internship', movie.name)
        self.assertEqual(2002, movie.year)
        self.assertEqual(9.6, movie.rating)
        self.assertEqual([], movie.actors)

    def test_init_when_name_empty(self):
        with self.assertRaises(ValueError) as exc:
            movie = Movie('', 2002, 9.6)
        self.assertEqual("Name cannot be an empty string!", str(exc.exception))

    def test_init_when_year_not_correct(self):
        with self.assertRaises(ValueError) as exc:
            movie = Movie('Internship', 1886, 9.6)
        self.assertEqual("Year is not valid!", str(exc.exception))

    def test_add_actor_when_correct(self):
        movie = Movie('Internship', 2002, 9.6)
        movie.add_actor('Vince Vohn')
        movie.add_actor('Brad Pitt')
        self.assertEqual(['Vince Vohn', 'Brad Pitt'], movie.actors)

    def test_add_actor_when_actor_in_actors(self):
        movie = Movie('Internship', 2002, 9.6)
        movie.actors = ['Vince Vohn']
        self.assertEqual("Vince Vohn is already added in the list of actors!", movie.add_actor('Vince Vohn'))

    def test_comparison_first_grater_than_other(self):
        movie1 = Movie('Internship', 2002, 9.6)
        movie2 = Movie('Mask', 2000, 8.6)
        self.assertEqual(f'"{movie1.name}" is better than "{movie2.name}"', movie1 > movie2)

    def test_comparison_second_grater_than_other(self):
        movie1 = Movie('Internship', 2002, 7.6)
        movie2 = Movie('Mask', 2000, 8.6)
        self.assertEqual(f'"{movie2.name}" is better than "{movie1.name}"', movie1 > movie2)

    def test_repr(self):
        movie = Movie('Internship', 2002, 9.6)
        movie.add_actor('Vince Vohn')
        movie.add_actor('Brad Pitt')
        self.assertEqual(f"Name: {movie.name}\n" \
               f"Year of Release: {movie.year}\n" \
               f"Rating: {movie.rating:.2f}\n" \
               f"Cast: {', '.join(movie.actors)}", repr(movie))




