import unittest

from codeUnderTest import rstrip_C


class TestSum(unittest.TestCase):
    def test_rstrip_C(self):
        self.assertEqual(rstrip_C('   test   '),'   test')
    def test_rstrip_C_empty_str(self):
        self.assertEqual(rstrip_C(''),'')

if __name__ == "__main__":
    unittest.main()
