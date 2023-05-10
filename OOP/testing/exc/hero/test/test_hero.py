import unittest
from unittest import TestCase

from project.hero import Hero

class TestHero(TestCase):
    ATTACKER_USERNAME = "USER"
    LEVEL = 10
    HEALTH = 100
    DAMAGE = 75

    BATTLE_LEVEL_INCREMENT = 1
    BATTLE_HEALTH_INCREMENT = 5
    BATTLE_DAMAGE_INCREMENT = 5

    def setUp(self) -> None:
        self.current_hero = Hero(self.ATTACKER_USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test_hero_init_returns_proper_values(self):
        self.assertEqual(self.ATTACKER_USERNAME, self.current_hero.username)
        self.assertEqual(self.LEVEL, self.current_hero.level)
        self.assertEqual(self.HEALTH, self.current_hero.health)
        self.assertEqual(self.DAMAGE, self.current_hero.damage)

    def test_battle_when_other_username_is_the_same(self):
        enemy = Hero(self.ATTACKER_USERNAME, 20, 50, 25)
        with self.assertRaises(Exception) as exc:
            self.current_hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(exc.exception))

    def test_battle_raises_when_attacker_health_is_zero_or_less(self):
        enemy = Hero("pesho", 20, 50, 25)
        self.current_hero.health = 0
        with self.assertRaises(ValueError) as exc:
            self.current_hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(exc.exception))


    def test_battle_raises_when_enemy_health_is_zero_or_less(self):
        enemy = Hero("pesho", 20, 0, 25)
        with self.assertRaises(ValueError) as exc: 
            self.current_hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(exc.exception))

    def test_battle_when_both_heroes_health_zero(self):
        enemy = Hero("pesho", self.LEVEL, self.HEALTH, self.DAMAGE)
        result = self.current_hero.battle(enemy)
        self.assertEqual("Draw", result)
        expected_health = self.HEALTH - (self.DAMAGE * self.LEVEL)
        self.assertEqual(expected_health, self.current_hero.health)
        self.assertEqual(expected_health, enemy.health)

    def test_battle_returns_win_when_enemy_defeated(self):
        enemy = Hero("pesho", 5, 100, 10)
        enemy_expected_health = enemy.health - (self.current_hero.level * self.current_hero.damage)
        resilt = self.current_hero.battle(enemy)

        self.assertEqual("You win", resilt)
        self.assertEqual(enemy_expected_health, enemy.health)
        self.assertEqual(self.LEVEL + self.BATTLE_LEVEL_INCREMENT, self.current_hero.level)
        self.assertEqual(self.DAMAGE + self.BATTLE_DAMAGE_INCREMENT, self.current_hero.damage)
        attacker_expected_health = self.HEALTH - (enemy.level * enemy.damage) + self.BATTLE_HEALTH_INCREMENT
        self.assertEqual(attacker_expected_health, self.current_hero.health)

    def test_battle_returns_lose_when_attacker_defeated(self):
        atacker = Hero("pesho", 5, 100, 10)
        enemy = Hero("PEPI", self.LEVEL, self.HEALTH, self.DAMAGE)
        attacker_expected_health = atacker.health - (enemy.level * enemy.damage)

        resilt = atacker.battle(enemy)
        self.assertEqual("You lose", resilt)
        self.assertEqual(attacker_expected_health, atacker.health)
        self.assertEqual(self.LEVEL + self.BATTLE_LEVEL_INCREMENT, enemy.level)
        self.assertEqual(self.DAMAGE + self.BATTLE_DAMAGE_INCREMENT, enemy.damage)
        enemy_expected_health = self.HEALTH - (atacker.level * atacker.damage) + self.BATTLE_HEALTH_INCREMENT
        self.assertEqual(enemy_expected_health, enemy.health)

    def test_str_expect_proper_value(self):
        self.assertEqual(f"Hero {self.ATTACKER_USERNAME}: {self.LEVEL} lvl\n" \
               f"Health: {self.HEALTH}\n" \
               f"Damage: {self.DAMAGE}\n", str(self.current_hero))


if __name__ == '__main__':
    unittest.main()
