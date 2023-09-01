class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        pivot_index = l

        if target == nums[pivot_index]:
            return pivot_index
        
        if target <= nums[-1]:
            l, r = pivot_index, len(nums) - 1
        else:
            l, r = 0, pivot_index

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l if nums[l] == target else -1