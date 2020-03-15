
class Span:
    """
    Span objects are used to define boundaries within other iterables.
    """
    def __init__(self, start, end):
        if not start <= end:
            raise ValueError('Start cannot be greater than or equal to End')

        self._start = start
        self._end = end

    @property
    def span(self):
        """
        Return the span start and end scalars
        :return: The start and end indexes
        """
        return self._start, self._end

    def __eq__(self, other):
        start, fin = other.span()
        return self._start == start and self._end == fin


class DistanceCalculator:
    """
    The ADistanceCalculator class defines a metric on strings. It is a way of determining the distance from
    one string to another.
    """

    def __init__(self, insert_cost=1, deletion_cost=1, subst_cost=1):
        """
        The constructor for the distance calculator. The insert, deletion, and substitution cost can be specified
        as state for the object.
        :param insert_cost:
        :param deletion_cost:
        :param subst_cost:
        """
        self._insert_cost = insert_cost
        self._deletion_cost = deletion_cost
        self._subst_cost = subst_cost

    def distance(self, source, target):
        """
        Calculates the distance between two strings.
        :param source: The source string
        :param target: The target string
        :return: The scalar distance between the source and target.
        """
        raise NotImplementedError('Distance calculation not implemented yet')
