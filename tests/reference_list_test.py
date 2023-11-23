import unittest
from reference_list import list_references

class TestReferenceList(unittest.TestCase):
    def setUp(self):
        pass

    def test_lists_length(self):
        books = []
        articles = []
        inproceedings = []
        references = list_references(books, articles, inproceedings)
        self.assertEqual(len(references), 0)