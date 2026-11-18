import unittest

from data_structures.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_append_and_length(self):
        games = LinkedList()
        games.append("Portal")
        games.append("Half-Life")
        self.assertEqual(len(games), 2)

    def test_iteration_preserves_order(self):
        games = LinkedList()
        games.append("Portal")
        games.append("Half-Life")
        self.assertEqual(games.to_list(), ["Portal", "Half-Life"])

    def test_remove_head(self):
        games = LinkedList()
        games.append("Portal")
        games.append("Half-Life")
        self.assertTrue(games.remove("Portal"))
        self.assertEqual(games.to_list(), ["Half-Life"])

    def test_remove_missing_item(self):
        games = LinkedList()
        self.assertFalse(games.remove("Missing"))


if __name__ == "__main__":
    unittest.main()
