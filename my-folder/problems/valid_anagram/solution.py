class Solution:
    def isAnagram(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False

        a_letters = {}
        b_letters = {}

        for letter in a:
            a_letters[letter] = a_letters.get(letter, 0) + 1

        for letter in b:
            if letter not in a_letters:
                return False
            b_letters[letter] = b_letters.get(letter, 0) + 1

        return a_letters == b_letters