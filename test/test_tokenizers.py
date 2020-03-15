import unittest
from tokenizer import WhiteSpaceTokenizer, Tokenizer, Token
from util import Span


class TestWhiteSpaceTokenizer(unittest.TestCase):

    def setUp(self):
        self._tokz = WhiteSpaceTokenizer()

    def test_split(self):
        text = 'This is a test'
        tokenz = self._tokz.tokenize(text)

        self.assertEqual(tokenz[0], Token(text, Span(0, 4)))
        self.assertEqual(tokenz[1], Token(text, Span(5, 7)))
        self.assertEqual(tokenz[2], Token(text, Span(8, 9)))
        self.assertEqual(tokenz[3], Token(text, Span(10, 14)))

    def test_specials(self):
        text = 'This Dr. is a test!'
        #       0123456789012345678
        tokenz = self._tokz.tokenize(text)

        self.assertEqual(tokenz, [Token(text, Span(0, 4)),
                                  Token(text, Span(5, 8)),
                                  Token(text, Span(9, 11)),
                                  Token(text, Span(12, 13)),
                                  Token(text, Span(14, 19))])

    def test_singleword(self):
        text = 'This'
        tokenz = self._tokz.tokenize(text)
        self.assertEqual(tokenz[0], Token(text, Span(0, 4)))

    def test_empty(self):
        text = ''
        tokenz = self._tokz.tokenize(text)
        self.assertEqual(tokenz[0], Token(text, Span(0, 1)))


class TestTokenizer(unittest.TestCase):

    def setUp(self):
        self._tokz = Tokenizer()

    def test_whitspace(self):
        text = 'Hello there 5555 my dearest world'
        #       012345678901234567890123456789012
        res = self._tokz.tokenize(text)

        self.assertEqual(res, [Token(text, Span(0, 5)),
                               Token(text, Span(6, 11)),
                               Token(text, Span(12, 16)),
                               Token(text, Span(17, 19)),
                               Token(text, Span(20, 27)),
                               Token(text, Span(28, 33))])

    def test_prefix(self):
        text = '(Hello my $555 dearest world'
        #       0123456789012345678901234567
        res =  self._tokz.tokenize(text)
        self.assertEqual(res, [Token(text, Span(0, 1)),
                               Token(text, Span(1, 6)),
                               Token(text, Span(7, 9)),
                               Token(text, Span(10, 11)),
                               Token(text, Span(11, 14)),
                               Token(text, Span(15, 22)),
                               Token(text, Span(23, 28))])

    def test_postfix(self):
        text = 'Hello) my 555! dearest world?'
        #       01234567890123456789012345678
        res = self._tokz.tokenize(text)

        self.assertEqual(res, [Token(text, Span(0, 5)),
                               Token(text, Span(5,6)),
                               Token(text, Span(7, 9)),
                               Token(text, Span(10, 13)),
                               Token(text, Span(13, 14)),
                               Token(text, Span(15, 22)),
                               Token(text, Span(23, 28)),
                               Token(text, Span(28, 29))])

    def test_infix(self):
        text = 'Hel?lo my 55!5! dear,est (world?'
        #       01234567890123456789012345678901
        res = self._tokz.tokenize(text)
        self.assertEqual(res, [Token(text, Span(0, 3)),
                               Token(text, Span(3, 4)),
                               Token(text, Span(4, 6)),
                               Token(text, Span(7, 9)),
                               Token(text, Span(10, 12)),
                               Token(text, Span(12, 13)),
                               Token(text, Span(13, 14)),
                               Token(text, Span(14, 15)),
                               Token(text, Span(16, 20)),
                               Token(text, Span(20, 21)),
                               Token(text, Span(21, 24)),
                               Token(text, Span(25, 26)),
                               Token(text, Span(26, 31)),
                               Token(text, Span(31, 32))
                               ])


if __name__ == '__main__':
    unittest.main()
