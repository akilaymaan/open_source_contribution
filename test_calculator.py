"""Run with: python -m unittest -v."""

import contextlib
import importlib
import io
import unittest

import calculator
from calculator import add, subtract


class CalculatorTests(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_large_integers(self):
        # Large integer calculations should remain exact.
        large = 10 ** 20
        self.assertEqual(add(large, 1), large + 1)
        self.assertEqual(subtract(large, 1), large - 1)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(7, 0), 7)
        self.assertEqual(subtract(7, 0), 7)
        self.assertEqual(subtract(0, 7), -7)

    def test_negative_numbers(self):
        self.assertEqual(add(-3, -2), -5)
        self.assertEqual(add(-3, 5), 2)
        self.assertEqual(subtract(-3, -2), -1)
        self.assertEqual(subtract(3, -2), 5)

    def test_equal_operands(self):
        self.assertEqual(subtract(8, 8), 0)

    def test_subtraction_order(self):
        self.assertEqual(subtract(5, 10), -5)

    def test_decimal_numbers(self):
        # Floats may round, so compare approximately rather than exactly.
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2)

    def test_mixed_integer_and_float(self):
        self.assertAlmostEqual(add(2, 0.5), 2.5)
        self.assertAlmostEqual(subtract(2, 0.5), 1.5)

    def test_import_does_not_print_demo(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            importlib.reload(calculator)
        self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
