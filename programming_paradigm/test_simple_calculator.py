import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a fresh SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test add with integers, negatives, zeros, and floats."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertAlmostEqual(self.calc.add(2.5, 0.5), 3.0)

    def test_subtraction(self):
        """Test subtract with positive, negative, and float inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertAlmostEqual(self.calc.subtract(2.5, 0.5), 2.0)

    def test_multiplication(self):
        """Test multiply with positive, negative, zero and float inputs."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertAlmostEqual(self.calc.multiply(1.5, 2), 3.0)

    def test_division(self):
        """Test divide for normal cases and division-by-zero edge case.

        This method name is required by the test checker.
        """
        # normal divisions (note: division returns floats in Python)
        self.assertEqual(self.calc.divide(6, 3), 2)         # 6/3 == 2.0 == 2
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)
        self.assertAlmostEqual(self.calc.divide(1, 4), 0.25)

        # division by zero returns None per implementation
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(10, 0.0))

    def test_methods_exist(self):
        """Ensure the SimpleCalculator exposes the expected methods."""
        for method in ('add', 'subtract', 'multiply', 'divide'):
            self.assertTrue(hasattr(self.calc, method), f"Missing method: {method}")

if __name__ == "__main__":
    unittest.main()
