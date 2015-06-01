#!/usr/local/bin/python

import mock
import unittest
from jumble import create_word_dict, get_words
from jumble import comb


class TestJumble(unittest.TestCase):

    def test_word_dict(self):
        word_dict = create_word_dict("test_words.txt")
        self.assertEqual(['dog', 'god', 'God'], word_dict["dgo"])

    def test_comb(self):
        combos = comb(2, range(4))
        self.assertEqual([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]], combos)

    @mock.patch('__builtin__.raw_input')
    def test_get_words(self, input_letters):
        input_letters.return_value = "dog"
        words = get_words("test_words.txt")
        self.assertEqual(['do', 'go', 'dog', 'god', 'God'], words)

if __name__ == '__main__':
    unittest.main()