"""
Objective
In this challenge, we practice calculating probability.

Task
In a single toss of 2 fair (evenly-weighted) -sided dice, find the probability of that their sum will be at most 9.

Output Format

In the editor below, submit your answer as Plain Text in the form of an irreducible fraction A/B, where A and B are both integers.

Your answer should resemble something like:

3/4
(This is NOT the answer, just a demonstration of the answer format.)
"""
import itertools
from fractions import Fraction

if __name__ == '__main__':
    dices = list(range(1, 7))
    total = itertools.product(dices, dices)
    satisfied = len([1 for dice in total if sum(dice) <= 9])
    print(Fraction(satisfied, 36))
