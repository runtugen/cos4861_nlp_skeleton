from estimator.mle import MaxLikelihoodEstimator
from util import Span
from tokenizer import Token
import pkg_resources

# The data sources, use these to train the tagger model, which is used by the tagger to
# classify the tokens in the sentence.
training_data_file = pkg_resources.resource_filename(__name__, 'data/pos_tagged.txt')
golden_standard_data_file = pkg_resources.resource_filename(__name__, 'data/pos_golden_standard.txt')
test_data_file = pkg_resources.resource_filename(__name__, 'data/pos_test.txt')


class APosTaggerModel:

    def __init__(self):
        pass

    def train(self, training_data=training_data_file):
        """
        Create the model on the data provided.

        The expected file should contain 'word/tag' pairs which the trainer will
        split and use to train the model.
        :param training_data: A file containing training data in word/tag format.
        :return: None
        """
        raise NotImplemented('train method on the tagger is not implemented')

    def classify(self, token_str):
        """
        Classifies a token string using the trained model.
        :param token_str: A str token that should be tagged.
        :return: The tag for the token string
        """
        raise NotImplemented('Classify is not Implemented yet')


class APosTagger:

    def __init__(self, tagger_model):
        self._tagger_model = tagger_model

    def tag_sentence(self, sentence_toks):
        """
        Accept a list of Tokens, and tag each one according to a trained training model.
        :param sentence_toks: A list of Tokens (from tokenizer.Token)
        :return: None
        """
        raise NotImplemented('Tagger is not implemented')