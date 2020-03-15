import unittest
from util import DistanceCalculator


class TestEditDistance(unittest.TestCase):

    def test_emptyStrings(self):
        """
        Test emtpy strings using default values
        :return:
        """

        ed = DistanceCalculator()
        self.assertEqual(ed.distance('', ''), 0)
        self.assertEqual(ed.distance('a', ''), 1)
        self.assertEqual(ed.distance('', 'a'), 1)

    def test_sameStrings(self):
        ed = DistanceCalculator()

        self.assertEqual(ed.distance('abc', 'abc'), 0)

    def test_levensteinDistance(self):

        ed = DistanceCalculator()
        self.assertEqual(ed.distance('book', 'books'), 1)
        self.assertEqual(ed.distance('book', 'back'), 2)
        self.assertEqual(ed.distance('books', 'book'), 1)

    def test_nonStandardDistances(self):
        ed = DistanceCalculator(2, 2, 4)

        self.assertEqual(ed.distance('book', 'books'), 2)
        self.assertEqual(ed.distance('book', 'back'), 8)
        self.assertEqual(ed.distance('books', 'book'), 2)




