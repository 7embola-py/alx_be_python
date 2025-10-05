import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a fresh SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test add with integers, negatives, zeros, large ints and floats."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(10**18, 1), 10**18 + 1)     # large numbers
        self.assertAlmostEqual(self.calc.add(2.5, 0.5), 3.0)       # floats

    def test_subtraction(self):
        """Test subtract with positive, negative, and float inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertAlmostEqual(self.calc.subtract(2.5, 0.5), 2.0)

    def test_multiplication(self):
        """Test multiply with positive, negative, zero and float inputs."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertAlmostEqual(self.calc.multiply(1.5, 2), 3.0)

    def test_division_normal(self):
        """Test divide for normal (non-zero divisor) cases, including floats."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)
        self.assertAlmostEqual(self.calc.divide(1, 4), 0.25)

    def test_division_by_zero(self):
        """Test division by zero returns None (edge case)."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(10, 0.0))  # float zero should also be treated as zero

    def test_methods_exist(self):
        """Make sure the SimpleCalculator exposes expected methods."""
        for method in ('add', 'subtract', 'multiply', 'divide'):
            self.assertTrue(hasattr(self.calc, method), f"Missing method: {method}")

if __name__ == "__main__":
    unittest.main()
