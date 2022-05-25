"""
Some String Manipulation Algorithms
"""
from collections import deque


class StringManipulation:
    @staticmethod
    def get_number_of_vowels(string: str):
        if string is None:
            return 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        counter = 0
        for char in string:
            if char.lower() in vowels:
                counter += 1
        return counter

    @staticmethod
    def reverse(string: str):
        if string is None:
            return ""
        reversed_string = list()
        for i in range(len(string)):
            reversed_string.append(string[len(string) - 1 - i])
        return "".join(reversed_string)

    @staticmethod
    def reverse_word_orders(string: str):
        words = string.strip().split()
        reversed_order = list()
        i = len(words)
        while i > 0:
            reversed_order.append(words[i - 1])
            i -= 1
        return " ".join(reversed_order)

    @staticmethod
    def is_rotation(s1: str, s2: str):
        if s1 is None or s2 is None:
            return False
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
