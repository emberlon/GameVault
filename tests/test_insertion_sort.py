import unittest

from algorithms.insertion_sort import insertion_sort
from models.game import Game


class TestInsertionSort(unittest.TestCase):
    def test_sorts_numbers(self):
        self.assertEqual(insertion_sort([5, 2, 4, 1]), [1, 2, 4, 5])

    def test_sorts_games_by_title(self):
        games = [
            Game("Zelda", "Switch", "Adventure", 2017),
            Game("Portal", "PC", "Puzzle", 2007),
            Game("Halo", "Xbox", "Shooter", 2001),
        ]
        result = insertion_sort(games, key=lambda game: game.title)
        self.assertEqual(
            [game.title for game in result],
            ["Halo", "Portal", "Zelda"],
        )

    def test_does_not_modify_original_list(self):
        original = [3, 1, 2]
        insertion_sort(original)
        self.assertEqual(original, [3, 1, 2])


if __name__ == "__main__":
    unittest.main()
