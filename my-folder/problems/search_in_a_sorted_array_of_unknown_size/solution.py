# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        l, r = 0, 10**4
        
        while l <= r:
            mid = (l + r) // 2
            if reader.get(mid) == target:
                return mid
            
            if reader.get(mid) > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1

   