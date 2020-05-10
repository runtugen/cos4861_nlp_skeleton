import unittest
import random
from collections import defaultdict
from estimator.mle import MaxLikelihoodEstimator


class TestMLE(unittest.TestCase):

    def test_equiprobable(self):
        training_data = ['<s>', 'sam', 'i', 'am']
        mle = MaxLikelihoodEstimator()
        mle.train(zip(training_data, training_data[1:]))

        self.assertEqual(mle.p('sam', '<s>'), 1.0)
        self.assertEqual(mle.p('i', 'sam'), 1.0)
        self.assertEqual(mle.p('am', 'i'), 1.0)

    def test_other_distribution(self):
        training_data = ['<s>', 'sam', 'i', 'am', 'i', 'am', 'sam']

        mle = MaxLikelihoodEstimator()
        mle.train(zip(training_data, training_data[1:]))

        self.assertEqual(mle.p('sam', '<s>'), 1.0)
        self.assertEqual(mle.p('i', 'sam'), 0.5)
        self.assertEqual(mle.p('am', 'i'), 1.0)
        self.assertEqual(mle.p('sam', 'am'), 0.5)

    def test_laplace(self):
        training_data = ['<s>', 'sam', 'i', 'am', 'i', 'am', 'sam']

        mle = MaxLikelihoodEstimator(pseudocount=1)
        mle.train(zip(training_data, training_data[1:]))

        self.assertAlmostEqual(mle.p('sam', 'i'), 0.167, 3)
        self.assertAlmostEqual(mle.p('i', 'i'), 0.167, 3)
        self.assertAlmostEqual(mle.p('am', 'sam'), 0.167, 3)
        self.assertAlmostEqual(mle.p('sam', 'i'), 0.167, 3)
        self.assertAlmostEqual(mle.p('i', 'sam'), 0.333, 3)

    def test_trigrams(self):
        training_data = ['<s>', 'sam', 'i', 'am', 'i', 'am', 'sam']

        mle = MaxLikelihoodEstimator(pseudocount=1)
        mle.train(zip(training_data[3:], zip(training_data, training_data[1:])))

        self.assertEqual(mle.p('i', ('<s>', 'sam')), 0.4, 3)

