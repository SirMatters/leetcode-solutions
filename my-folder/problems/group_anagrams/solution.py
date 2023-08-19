class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}

        for word in strs:
            letters = [letter for letter in word]
            sorted_letters = sorted(letters)
            str_hash = ''.join(sorted_letters)
            if str_hash in anagrams_map:
                anagrams_map[str_hash].append(word)
            else:
                anagrams_map[str_hash] = [word]

        return list(anagrams_map.values())
