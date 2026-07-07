import sys
import unittest
import numpy as np

sys.path.append("src/")  # noqa

import math_utils


class TestExtractionFunctions(unittest.TestCase):

    def test_add(self):

        # Done many times with rand. numbers to test robustness
        for _ in range(100):

            # Generates two random numbers bewteen 0 and 1
            x, y = np.random.uniform(0, 1, 2)

            # This should always hold!
            self.assertTrue(math_utils.add(x, y) == x + y)

    def test_subtract(self):

        for _ in range(100):
            pass

    def test_multiply(self):

        for _ in range(100):
            pass

    def test_divide(self):

        # Done many times with rand. numbers to test robustness
        for _ in range(100):

            # Generates two random numbers bewteen 1 and 5
            x, y = np.random.uniform(1, 5, 2)

            # This should always hold!
            self.assertTrue(math_utils.divide(x, y) == x / y)

            # Test that a number divided by itself is always 1:
            self.assertTrue(math_utils.divide(x, x) == 1)

            # Test that a number divided by 1 is always itself:
            self.assertTrue(math_utils.divide(x, 1) == x)

            # Test that zero divided by anything is always 0:
            if y != 0:
                # should always hold, but just in case we check that y != 0 first:
                self.assertTrue(math_utils.divide(0, y) == 0)

            # Test that if x < y then x / y < 1:
            if x < y:
                self.assertTrue(math_utils.divide(x, y) < 1)
            else:
                self.assertTrue(math_utils.divide(x, y) >= 1)

            # Other potential tests:
            # - Test what happens if y = 0 (should raise an error)
            # - Test what happens if x = 0 and y = 0 (should raise an error)


if __name__ == "__main__":
    unittest.main()
