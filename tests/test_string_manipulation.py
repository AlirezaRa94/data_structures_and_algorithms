from unittest import TestCase

from algorithms.string_manipulation import StringManipulation


class TestStringManipulation(TestCase):
    def setUp(self) -> None:
        self.long_string = """  Hi! This is a   long string for testing some
         algorithms of string manipulation. I have   to test everything. So this
         text should contain multiple numbers like: 1, 2, 5.  """
        self.empty_string = ""
        self.one_word = "Alirezaa"

    def test_get_number_of_vowels(self):
        function = StringManipulation.get_number_of_vowels
        self.assertEqual(45, function(self.long_string))
        self.assertEqual(0, function(self.empty_string))
        self.assertEqual(5, function(self.one_word))

    def test_reverse(self):
        function = StringManipulation.reverse
        self.assertEqual(self.long_string[::-1], function(self.long_string))
        self.assertEqual("", function(self.empty_string))
        self.assertEqual(self.one_word[::-1], function(self.one_word))

    def test_reverse_word_orders(self):
        function = StringManipulation.reverse_word_orders
        print(function(self.long_string))
        self.assertEqual(self.empty_string, function(self.empty_string))
        self.assertEqual(self.one_word, function(self.one_word))

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

    def test_remove_duplicates(self):
        function = StringManipulation.remove_duplicates
        self.assertEqual(
            'Hi! Thsalongtrfem\npu.IvySxdcbk:1,25',
            function(self.long_string)
        )
        self.assertEqual(self.empty_string, function(self.empty_string))
        self.assertEqual('Alireza', function(self.one_word))

    def test_get_most_repeated_character(self):
        function = StringManipulation.get_most_repeated_character
        self.assertEqual(" ", function(self.long_string))
        with self.assertRaises(ValueError) as error:
            function(self.empty_string)
            self.assertEqual(
                error.exception,
                "The string doesn't have any characters!"
            )
        self.assertEqual("a", function(self.one_word))

    def test_capitalize_first_letters(self):
        function = StringManipulation.capitalize_first_letters
        print(function(self.long_string))
        self.assertEqual("", function(self.empty_string))
        self.assertEqual(self.one_word, function(self.one_word))

    def test_is_anagram(self):
        function = StringManipulation.is_anagram
        self.assertTrue(function("ABCD", "BCDA"))
        self.assertFalse(function("ABCD", "ABCE"))
        self.assertTrue(function("ABCD", "ABCD"))
        self.assertTrue(function("", ""))
        self.assertFalse(function("", "B"))
        self.assertTrue(function("A", "A"))

    def test_is_palindrome(self):
        function = StringManipulation.is_palindrome
        self.assertTrue(function("ABbA"))
        self.assertFalse(function("ABC"))
        self.assertTrue(function("Was it a cat I saw?"))
        self.assertTrue(function(""))
        self.assertFalse(function("Ab"))
        self.assertTrue(function("A!"))
