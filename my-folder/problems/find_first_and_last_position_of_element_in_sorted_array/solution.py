class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        st = self.find_boundary(nums, target, True)

        if st == -1:
            return [-1, -1]

        en = self.find_boundary(nums, target, False)

        return [st, en]
    
    def find_boundary(self, nums: List[int], target: int, isFirst: bool) -> int:
        length = len(nums)
        l, r = 0, length - 1
        while l <= r:
            mid = (l + r) // 2 
            
            if nums[mid] == target:
                if isFirst:
                    if mid == l or nums[mid - 1] != target:
                        return mid
                    else:
                        r = mid - 1
                else:
                    if mid == r or nums[mid + 1] != target:
                        return mid
                    else:
                        l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1