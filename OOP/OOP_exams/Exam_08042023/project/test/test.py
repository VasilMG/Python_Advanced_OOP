from project.tennis_player import TennisPlayer
from unittest import TestCase



class TestTennisPlayer(TestCase):

    def test_init_values_correct(self):
        tp = TennisPlayer("peter", 18, 25.5)
        self.assertEqual('peter', tp.name)
        self.assertEqual( 18, tp.age)
        self.assertEqual( 25.5, tp.points)
        self.assertEqual([], tp.wins)

    def test_init_name_incorrect_expect_error(self):
        with self.assertRaises(ValueError) as va:
            tp = TennisPlayer("pa", 18, 25.5)
        self.assertEqual("Name should be more than 2 symbols!", str(va.exception))

    def test_init_age_incorrect_expect_error(self):
        with self.assertRaises(ValueError) as va:
            tp = TennisPlayer("peter", 17, 25.5)
        self.assertEqual("Players must be at least 18 years of age!", str(va.exception))

    def test_add_win_new_tournament(self):
        tp = TennisPlayer("peter", 18, 25.5)
        tp.add_new_win('Wimbledon')
        tp.add_new_win('AUS Open')
        self.assertEqual(['Wimbledon', "AUS Open"], tp.wins)
        self.assertEqual(2, len(tp.wins))

    def test_add_win_tournament_already_added(self):
        tp = TennisPlayer("peter", 18, 25.5)
        tp.add_new_win('Wimbledon')
        tp.add_new_win('AUS Open')
        result = tp.add_new_win('AUS Open')
        expected = f"AUS Open has been already added to the list of wins!"
        self.assertEqual(expected, result)
        self.assertEqual(['Wimbledon', "AUS Open"], tp.wins)
        self.assertEqual(2, len(tp.wins))

    def test_comparison_first_player_equal_to_second(self):
        tp = TennisPlayer("peter", 18, 25.5)
        sec_player = TennisPlayer("Ivan", 18, 25.5)
        result = tp < sec_player
        self.assertEqual(f'peter is a better player than Ivan', result)

    def test_comparison_first_player_better_to_second(self):
        tp = TennisPlayer("peter", 18, 26)
        sec_player = TennisPlayer("Ivan", 18, 25.5)
        result = tp < sec_player
        self.assertEqual(f'peter is a better player than Ivan', result)

    def test_comparison_second_player_better_to_first(self):
        tp = TennisPlayer("peter", 18, 20)
        sec_player = TennisPlayer("Ivan", 18, 25.5)
        result = tp < sec_player
        self.assertEqual(f'Ivan is a top seeded player and he/she is better than peter', result)

    def test_string(self):
        tp = TennisPlayer("peter", 18, 25.5)
        tp.add_new_win('Wimbledon')
        tp.add_new_win('AUS Open')
        self.assertEqual('Tennis Player: peter\n' +
                         'Age: 18\n' + 'Points: 25.5\n' +
                         'Tournaments won: Wimbledon, AUS Open', str(tp))


