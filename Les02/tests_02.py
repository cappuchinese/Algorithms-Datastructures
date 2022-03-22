"""Tests for examples"""

from copy import deepcopy
import unittest

from Les02 import answers_02

SORTED_INT_LIST = [1, 7, 15, 20, 30]
SORTED_RESULT_PREPEND = [0, 1, 7, 15, 20, 30]
SORTED_RESULT_APPEND = [1, 7, 15, 20, 30, 31]
SORTED_RESULT_INSERT = [1, 7, 15, 17, 20, 30]
SORTED_RESULT_DOUBLE = [1, 7, 15, 15, 20, 30]


class InsertFromStart(unittest.TestCase):
    """Tests for bag.Bag"""

    def setUp(self):
        """create a copy of the sorted list array
        and prepend, insert and append items
        also insert a double item ;)"""
        self.s_int_list = deepcopy(SORTED_INT_LIST)

    def test_prepend(self):
        """test if items are correctly prepended."""
        answers_02.insert_from_start(self.s_int_list, 0)
        self.assertListEqual(SORTED_RESULT_PREPEND, self.s_int_list)

    def test_append(self):
        """test if items are correctly appended."""
        answers_02.insert_from_start(self.s_int_list, 31)
        self.assertListEqual(SORTED_RESULT_APPEND, self.s_int_list)

    def test_insert(self):
        """test if items are correctly inserted."""
        answers_02.insert_from_start(self.s_int_list, 17)
        self.assertListEqual(SORTED_RESULT_INSERT, self.s_int_list)

    def test_double(self):
        """test if double items are correctly inserted."""
        answers_02.insert_from_start(self.s_int_list, 15)
        self.assertListEqual(SORTED_RESULT_DOUBLE, self.s_int_list)


class InsertFromBack(unittest.TestCase):
    """Tests for bag.Bag"""

    def setUp(self):
        """create a copy of the sorted list array
        and prepend, insert and append items
        also insert a double item ;)"""
        self.s_int_list = deepcopy(SORTED_INT_LIST)

    def test_prepend(self):
        """test if items are correctly prepended."""
        answers_02.insert_from_back(self.s_int_list, 0)
        self.assertListEqual(SORTED_RESULT_PREPEND, self.s_int_list)

    def test_append(self):
        """test if items are correctly appended."""
        answers_02.insert_from_back(self.s_int_list, 31)
        self.assertListEqual(SORTED_RESULT_APPEND, self.s_int_list)

    def test_insert(self):
        """test if items are correctly inserted."""
        answers_02.insert_from_back(self.s_int_list, 17)
        self.assertListEqual(SORTED_RESULT_INSERT, self.s_int_list)

    def test_double(self):
        """test if double items are correctly inserted."""
        answers_02.insert_from_back(self.s_int_list, 15)
        self.assertListEqual(SORTED_RESULT_DOUBLE, self.s_int_list)


def add_tests():
    """indicate tests to be run"""
    suite = unittest.TestSuite()
    suite.addTest(InsertFromBack('test_prepend'))
    suite.addTest(InsertFromBack('test_append'))
    suite.addTest(InsertFromBack('test_insert'))
    suite.addTest(InsertFromBack('test_double'))
    suite.addTest(InsertFromStart('test_prepend'))
    suite.addTest(InsertFromStart('test_append'))
    suite.addTest(InsertFromStart('test_insert'))
    suite.addTest(InsertFromStart('test_double'))
    return suite


if __name__ == '__main__':
    RUNNER = unittest.TextTestRunner()
    RUNNER.run(add_tests())
