class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res=[1] * length
        
        pre = 1
        for i in reversed(range(length)):
            res[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(length):
            res[i] *= post
            post *= nums[i]
        
        return res