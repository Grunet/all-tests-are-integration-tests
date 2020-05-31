import unittest

from codeUnderTest import strip_C


class TestSum(unittest.TestCase):
    def test_strip_C(self):
        self.assertEqual(strip_C("   test   "), "test", "Should be 'test'")

    def test_strip_C_empty_str(self):
        self.assertEqual(strip_C(""), "", "Should be null")


if __name__ == "__main__":
    unittest.main()
