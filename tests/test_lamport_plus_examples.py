"""Exact controls for the shareable Lamport-Plus worked examples."""

from itertools import combinations, product
import unittest


def binary_span(*vectors):
    points = {0}
    for vector in vectors:
        points |= {point ^ vector for point in points}
    return frozenset(points)


def quotient_size(numerator, denominator):
    return len({frozenset(x ^ y for y in denominator) for x in numerator})


class LamportPlusExampleTests(unittest.TestCase):
    def test_integer_parity_witness_including_negative_inputs(self):
        for integer in range(-21, 22):
            quotient, remainder = divmod(integer, 2)
            with self.subTest(integer=integer):
                if remainder == 1:
                    witness = 2 * quotient**2 + 2 * quotient
                    self.assertEqual(integer**2, 2 * witness + 1)
                self.assertEqual((integer**2) % 2, remainder)
        self.assertNotEqual((-3)**2, 2 * ((-3) // 2) + 1)

    def test_divisibility_needs_the_positive_domain(self):
        counterexamples = {
            (a, b)
            for a, b in product(range(-5, 6), repeat=2)
            if a != 0 and b % a == 0 and a > b
        }
        self.assertTrue({(2, 0), (2, -4)} <= counterexamples)
        self.assertFalse({(a, b) for a, b in counterexamples if a > 0 and b > 0})
        strict_counterexamples = {
            (a, b)
            for a, b in product(range(1, 6), repeat=2)
            if b % a == 0 and a >= b
        }
        self.assertIn((2, 2), strict_counterexamples)

    def test_exact_quotient_counts_over_all_binary_three_space_subspaces(self):
        subspaces = {
            binary_span(*basis)
            for rank in range(4)
            for basis in combinations(range(1, 8), rank)
        }
        self.assertEqual(len(subspaces), 16)
        cases = 0
        for A, W, P in product(subspaces, repeat=3):
            J, V = P & W, A & W
            U = J & V
            # Represent the projection M -> M/A by its full coset.
            image_of_W = {frozenset(w ^ a for a in A) for w in W}
            image_of_J = {frozenset(j ^ a for a in A) for j in J}
            complement, remainder = divmod(len(image_of_W), len(image_of_J))
            self.assertEqual(remainder, 0)
            self.assertEqual(quotient_size(W, J), quotient_size(V, U) * complement)
            cases += 1
        self.assertEqual(cases, 4096)

    def test_projecting_before_intersection_changes_the_example(self):
        A, W, P = binary_span(1, 2), binary_span(1, 4, 8), binary_span(6, 8)
        J, V = P & W, A & W
        U = V & J
        # In this coordinate example the projection keeps coordinates 3 and 4.
        projected_W = {w & 12 for w in W}
        projected_J = {j & 12 for j in J}
        wrong_denominator = projected_W & {p & 12 for p in P}
        self.assertEqual((J, V, U), ({0, 8}, {0, 1}, {0}))
        self.assertEqual(quotient_size(W, J), 4)
        self.assertEqual(quotient_size(V, U), 2)
        self.assertEqual(quotient_size(projected_W, projected_J), 2)
        self.assertEqual(quotient_size(projected_W, wrong_denominator), 1)
        self.assertNotEqual(
            quotient_size(W, J),
            quotient_size(V, U) * quotient_size(projected_W, wrong_denominator),
        )
