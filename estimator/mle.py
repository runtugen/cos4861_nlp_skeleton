from estimator import AEstimator


class MaxLikelihoodEstimator(AEstimator):
    """
    The estimator using maximum likelihood. We hide the pseudocount in here to be used with LaPlace smoothing.
    By default it is set to 0, which means no smoothing occurs.
    """

    def __init__(self, pseudocount=0):
        """
        Constructor for the class
        :param pseudocount: Sets the pseudocount value for the object. This enables Laplace smoothing at no extra
        cost.
        """
        self._model = dict()
        self._alpha = pseudocount
        self._N = 0
        self._V = 0

    def train(self, samples):
        """
        Train the estimator. We record N, the number of instances seen, and d, the number of different items.

        :param samples: The sample for training
        :return: None
        """
        raise NotImplementedError("The training method for the MLE model has not been implemented yet.")

    def p(self, evidence, history):
        """
        Return the value of v from the samples
        :param evidence: The provided evidence
        :param history: The history to take into account.
        :return: The probability of v
        """
        raise NotImplementedError("The p method for the MLE model has not been implemented yet.")
