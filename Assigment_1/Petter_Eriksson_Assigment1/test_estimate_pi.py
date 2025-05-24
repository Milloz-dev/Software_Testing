import unittest
from unittest.mock import mock_open, patch
import random
import math
from estimate_pi import estimate_pi, PiFileWriter

class TestEstimatePi(unittest.TestCase):
    def test_estimate_pi(self):
        pi_expected = 3.141592653589793
        pi_actual = estimate_pi(1000000)
        self.assertAlmostEqual(pi_expected, pi_actual, delta=0.01)

    def test_pi_accuracy_stability(self):
        sample_sizes = [100, 1000, 10000]
        for _ in range(10):  # run 10 times to check stability
            for n in sample_sizes:
                result = estimate_pi(n)
                self.assertAlmostEqual(result, math.pi, delta=0.1, msg=f"Failed at n={n}")

    def test_with_seed(self):
        """Test consistency with fixed random seed"""
        random.seed(29)
        r1 = estimate_pi(15000)
        random.seed(29)
        r2 = estimate_pi(15000)
        self.assertEqual(r1, r2)
        
    def test_pifilewrite_mock(self):
        m = mock_open() # mock open()

        with patch("builtins.open", m): # patch open() so it uses the mock
            PiFileWriter.write("test content", "fake_file.txt")

        m.assert_called_once_with("fake_file.txt", 'w', encoding='utf8')
        handle = m() #  mock file handle open() returned
        handle.write.assert_called_once_with("test content")


if __name__ == '__main__':
    unittest.main()
