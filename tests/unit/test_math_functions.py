import sys
import unittest
import numpy as np

sys.path.append("src/")  # noqa

import math_utils


class TestExtractionFunctions(unittest.TestCase):

    def test_add(self):

        self.assertTrue(False)

        # Done many times with rand. numbers to test robustness
        for _ in range(100):

            # Generates two random numbers bewteen 0 and 1
            x, y = np.random.uniform(0, 1, 2)

            # This should always hold!
            self.assertTrue(math_utils.add(x, y) == x + y)


if __name__ == "__main__":
    unittest.main()
