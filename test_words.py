import unittest
from nose.tools import *
from words import numwords, wordcounts, addcounts
def test_numwords():
    assert_equal(0, numwords(""))
    assert_equal(1, numwords("hey"))
    assert_equal(3, numwords("blue moon is blue"))
    assert_equal(3, numwords("Blue moon is blue"))
    assert_equal(3, numwords("Blue moon, is blue."))
    assert_equal(3, numwords("Blue moon, ... is blue."))
    assert_equal(3, numwords("Blue moon, ...is blue."))
    assert_equal(3, numwords("Blue moon, is ...blue."))
    assert_equal(3, numwords("Truth is beauty; beauty, truth."))
    assert_equal(15, numwords("A bidarka, is it not so? Look! a bidarka, and one man who drives clumsily with a paddle!"))

def test_wordcounts():
    assert_dict_equal({}, wordcounts(""))
    assert_dict_equal({'foo': 1}, wordcounts("foo"))
    assert_dict_equal({'truth': 2, 'is': 1, 'beauty': 2},
            wordcounts("Truth is beauty; beauty, truth."))
    assert_dict_equal({'truth': 2, 'is': 1, 'beauty': 2},
            wordcounts("Truth is beauty; beauty ... truth."))

@raises(ValueError)
def test_addcounts_badarg_existing():
    addcounts(None, {})

@raises(ValueError)
def test_addcounts_badarg_new():
    addcounts({}, None)

@raises(ValueError)
def test_addcounts_badargs():
    addcounts(None, None)

class TestWords_addcounts(unittest.TestCase):
    def setUp(self):
        self.existing = {'truth': 2, 'is': 1, 'beauty': 2}

    def test_addcounts_empty(self):
        addcounts(self.existing, {})
        self.assertEqual({'truth': 2, 'is': 1, 'beauty': 2}, self.existing)

    def test_addcounts_double(self):
        new = dict(self.existing)
        addcounts(self.existing, new)
        self.assertEqual({'truth': 4, 'is': 2, 'beauty': 4}, self.existing)

    def test_addcounts_newword(self):
        addcounts(self.existing, {'love': 1})
        self.assertEqual({'truth': 2, 'is': 1, 'beauty': 2, 'love': 1}, self.existing)

