"""
Unit tests for MyBigNumber.sum()
Run with:  python -m pytest tests/ -v
"""

import unittest
from my_big_number import MyBigNumber


class TestMyBigNumber(unittest.TestCase):

    def setUp(self):
        self.calc = MyBigNumber()

    # ── Basic cases from the requirement ──────────────────────────────────────

    def test_example_from_spec(self):
        """1234 + 897 = 2131  (example given in the requirement)"""
        self.assertEqual(self.calc.sum("1234", "897"), "2131")

    # ── Zero ──────────────────────────────────────────────────────────────────

    def test_zero_plus_zero(self):
        self.assertEqual(self.calc.sum("0", "0"), "0")

    def test_zero_plus_number(self):
        self.assertEqual(self.calc.sum("0", "12345"), "12345")

    def test_number_plus_zero(self):
        self.assertEqual(self.calc.sum("9999", "0"), "9999")

    # ── Same length ───────────────────────────────────────────────────────────

    def test_same_length_no_carry(self):
        self.assertEqual(self.calc.sum("123", "456"), "579")

    def test_same_length_with_carry(self):
        self.assertEqual(self.calc.sum("999", "1"), "1000")

    def test_all_nines(self):
        self.assertEqual(self.calc.sum("9999", "9999"), "19998")

    # ── Different lengths ─────────────────────────────────────────────────────

    def test_first_longer(self):
        self.assertEqual(self.calc.sum("10000", "1"), "10001")

    def test_second_longer(self):
        self.assertEqual(self.calc.sum("1", "10000"), "10001")

    # ── Single digits ─────────────────────────────────────────────────────────

    def test_single_digit_no_carry(self):
        self.assertEqual(self.calc.sum("3", "5"), "8")

    def test_single_digit_with_carry(self):
        self.assertEqual(self.calc.sum("7", "8"), "15")

    # ── Very large numbers ────────────────────────────────────────────────────

    def test_large_numbers(self):
        a = "99999999999999999999"   # 20 nines
        b = "1"
        self.assertEqual(self.calc.sum(a, b), "100000000000000000000")

    def test_large_equal_numbers(self):
        a = "12345678901234567890"
        b = "98765432109876543210"
        # Verify against Python's own big-int arithmetic
        expected = str(int(a) + int(b))
        self.assertEqual(self.calc.sum(a, b), expected)

    # ── Leading-zero output never occurs ─────────────────────────────────────

    def test_no_leading_zeros_in_result(self):
        result = self.calc.sum("500", "500")
        self.assertEqual(result, "1000")
        self.assertFalse(result.startswith("0"))


if __name__ == "__main__":
    unittest.main()
