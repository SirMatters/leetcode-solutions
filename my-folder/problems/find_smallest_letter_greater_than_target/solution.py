class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        target_ord = ord(target)

        while l <= r:
            mid = (l + r) // 2
            mid_ord = ord(letters[mid])

            if mid_ord > target_ord:
                if mid == l or ord(letters[mid - 1]) <= target_ord:
                    return letters[mid]
            
            if mid_ord <= target_ord:
                l = mid + 1
            else:
                r = mid - 1
            
        return letters[0]