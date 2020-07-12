import re
from util import Span


def _white_space_spans(text):
    """
    Find the spans for tokens based on the locations of whitespace in the data
    :param text: The text to scan
    :return: A list of spans
    """
    matches = re.finditer(r'\s+', text)

    offset = 0
    for m in matches:
        yield offset, m.span(0)[0]
        offset = m.span(0)[1]
    yield offset, len(text)


class Token:
    """
    The token class represents a single token defined by the spans for an object.
    """

    def __init__(self, text, span, tag=None):
        """
        Initialise the token object using a span object.
        :param text: The text object which is indexed by the span object.
        :param span: The span object
        :param tag: The POS tag for this object.
        """
        self._span = span
        self._text = text
        self._tag = tag

    @property
    def span(self):
        return self._span

    def __repr__(self):
        start, fin = self.span.span
        return self._text[start:fin]

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, tag):
        self._tag = tag


class ATokenizer:
    """
    An abstract tokenizer class
    """

    def __init__(self):
        pass

    def tokenize(self, text):
        """
        The tokenize method takes a string and returns a list of Token objects.
        :param text: The string to tokenize
        :return: A list of Token objects
        """
        raise NotImplemented('Tokenizer not implemented.')


class WhiteSpaceTokenizer(ATokenizer):
    """
    A simple white space tokenizer. Returns Token objects separated by white space.
    """

    def __init__(self):
        super().__init__()

    def tokenize(self, text):
        """
        Tokenize the string using white space.
        :param text: The string of text to tokenize
        :return: The list of tokens separated by white space.
        """
        return [Token(text, Span(s, e)) for s, e in _white_space_spans(text)]


class Tokenizer(ATokenizer):
    """
    The default tokenizer.
    """

    def __init__(self):
        """
        Constructor. Perform any initialisation and setting of state variables that is needed.
        """
        return

    def tokenize(self, text):
        raise NotImplementedError('Default tokenizer method not implemented')


