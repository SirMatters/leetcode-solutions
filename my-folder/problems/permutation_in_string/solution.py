from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = Counter(s1)
        window_counter = Counter()

        for i in range(len(s2)):
            window_counter[s2[i]] += 1

            if i >= len(s1):
                if window_counter[s2[i - len(s1)]] == 1:
                    del window_counter[s2[i - len(s1)]]
                else:
                    window_counter[s2[i - len(s1)]] -= 1
            
            if window_counter == s1_dict:
                return True
        
        return False
