class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}

        for word in strs:
            letters = [letter for letter in word]
            sorted_letters = sorted(letters)
            hash = ''.join(sorted_letters)
            if hash in anagrams_map:
                anagrams_map[hash].append(word)
            else:
                anagrams_map[hash] = [word]

        return list(anagrams_map.values())
