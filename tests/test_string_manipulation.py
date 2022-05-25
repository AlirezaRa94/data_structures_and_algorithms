from unittest import TestCase

from algorithms.string_manipulation import StringManipulation


class TestStringManipulation(TestCase):
    def setUp(self) -> None:
        self.long_string = """  Hi! This is a long string for testing some algorithms of string manipulation. I have to
         test everything. So this text should contain multiple numbers like: 1, 2, 5.  """
        self.empty_string = ""
        self.one_word = "Alireza"

    def test_get_number_of_vowels(self):
        self.assertEqual(45, StringManipulation.get_number_of_vowels(self.long_string))
        self.assertEqual(0, StringManipulation.get_number_of_vowels(self.empty_string))
        self.assertEqual(4, StringManipulation.get_number_of_vowels(self.one_word))

    def test_reverse(self):
        self.assertEqual(self.long_string[::-1], StringManipulation.reverse(self.long_string))
        self.assertEqual("", StringManipulation.reverse(self.empty_string))
        self.assertEqual(self.one_word[::-1], StringManipulation.reverse(self.one_word))

    def test_reverse_word_orders(self):
        print(StringManipulation.reverse_word_orders(self.long_string))
        self.assertEqual(self.empty_string, StringManipulation.reverse_word_orders(self.empty_string))
        self.assertEqual(self.one_word, StringManipulation.reverse_word_orders(self.one_word))

    def base_test_is_rotation(self, function):
        self.assertTrue(function("ABCDE", "BCDEA"))
        self.assertFalse(function("ABCDE", "BCDE"))
        self.assertFalse(function("ABCDE", "AABCD"))
        self.assertTrue(function("", ""))
        self.assertFalse(function("A", "B"))
        self.assertTrue(function("A", "A"))

    def test_is_rotation(self):
        self.base_test_is_rotation(StringManipulation.is_rotation)

    def test_is_rotation_2(self):
        self.base_test_is_rotation(StringManipulation.is_rotation_2)
