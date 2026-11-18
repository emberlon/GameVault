import unittest

from data_structures.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_insert_and_get(self):
        table = HashTable()
        table.insert("Portal 2", 2011)
        self.assertEqual(table.get("Portal 2"), 2011)

    def test_lookup_is_case_insensitive(self):
        table = HashTable()
        table.insert("Portal 2", 2011)
        self.assertEqual(table.get("PORTAL 2"), 2011)

    def test_insert_updates_existing_key(self):
        table = HashTable()
        table.insert("Portal 2", 2011)
        table.insert("Portal 2", 2012)
        self.assertEqual(table.get("Portal 2"), 2012)
        self.assertEqual(len(table), 1)

    def test_remove(self):
        table = HashTable()
        table.insert("Portal 2", 2011)
        self.assertTrue(table.remove("Portal 2"))
        self.assertIsNone(table.get("Portal 2"))


if __name__ == "__main__":
    unittest.main()
