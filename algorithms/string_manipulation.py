"""
Some String Manipulation Algorithms
"""
import string


class StringManipulation:
    @staticmethod
    def get_number_of_vowels(s: str):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        counter = 0
        for char in s:
            if char.lower() in vowels:
                counter += 1
        return counter

    @staticmethod
    def reverse(s: str):
        reversed_string = list()
        for i in range(len(s)):
            reversed_string.append(s[len(s) - 1 - i])
        return "".join(reversed_string)

    @staticmethod
    def reverse_word_orders(s: str):
        words = s.strip().split()
        reversed_order = list()
        i = len(words)
        while i > 0:
            reversed_order.append(words[i - 1])
            i -= 1
        return " ".join(reversed_order)

    @staticmethod
    def is_rotation(s1: str, s2: str):
        s1 = s1.strip()
        s2 = s2.strip()
        return len(s1) == len(s2) and s2 in s1 + s1

    @staticmethod
    def is_rotation_2(s1: str, s2: str):
        if len(s1) != len(s2):
            return False
        for i in range(len(s2)):
            if s2[i] == s1[0] and s2[i:] + s2[:i] == s1:
                return True
        return s1 == s2

    @staticmethod
    def remove_duplicates(s: str):
        seen = set()
        output = list()
        for char in s.strip():
            if char not in seen:
                seen.add(char)
                output.append(char)
        return "".join(output)

    @staticmethod
    def get_most_repeated_character(s: str):
        if not s:
            raise ValueError("The string doesn't have any characters!")
        char_counts = dict()
        most_repeated = ""
        max_repeat = 0
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
            if char_counts[char] > max_repeat:
                most_repeated = char
                max_repeat = char_counts[char]
        return most_repeated

    @staticmethod
    def capitalize_first_letters(s: str):
        words = s.strip().split()
        for i in range(len(words)):
            first_letter = words[i][0]
            if first_letter in string.ascii_letters:
                words[i] = first_letter.upper() + words[i][1:].lower()
        return " ".join(words)

    @staticmethod
    def is_anagram(s1: str, s2: str):
        if len(s1) != len(s2):
            return False
        s1 = s1.replace(" ", "").lower()
        s2 = s2.replace(" ", "").lower()
        letter_count = dict()
        for letter in s1:
            letter_count[letter] = letter_count.get(letter, 0) + 1
        for letter in s2:
            count = letter_count.get(letter, 0)
            if count < 1:
                return False
            letter_count[letter] = count - 1
        return True

    @staticmethod
    def is_palindrome(s: str):
        i = 0
        j = len(s) - 1
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
