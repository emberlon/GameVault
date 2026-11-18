import unittest

from models.game import Game


class TestGame(unittest.TestCase):
    def test_game_defaults_to_not_completed(self):
        game = Game("Portal 2", "PC", "Puzzle", 2011)
        self.assertFalse(game.completed)

    def test_game_strips_title_whitespace(self):
        game = Game("  Portal 2  ", "PC", "Puzzle", 2011)
        self.assertEqual(game.title, "Portal 2")

    def test_empty_title_is_rejected(self):
        with self.assertRaises(ValueError):
            Game("   ", "PC", "Puzzle", 2011)


if __name__ == "__main__":
    unittest.main()
