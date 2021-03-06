import unittest
from fun_with_collections import sort_and_search_array


class SearchArray(unittest.TestCase):
    def test_search_array_for_item_found(self):
        self.assertEqual(sort_and_search_array.search_array([6, 12, 18, 24, 30], 30), 4)

    def test_search_array_for_item__not_found(self):
        self.assertEqual(sort_and_search_array.search_array([6, 12, 18, 24, 30], 36), -1)


if __name__ == '__main__':
    unittest.main()