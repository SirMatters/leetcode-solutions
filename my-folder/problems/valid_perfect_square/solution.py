class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        l, r = 2, num // 2
        while l <= r:
            mid = (r + l) // 2
            sq = mid ** 2
            if sq == num:
                return True
            
            if sq > num:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
