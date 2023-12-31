class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums = sorted(nums)
		res = []

		for i, fixed_num in enumerate(nums):
			if i > 0 and nums[i-1] == fixed_num:
				continue

			l, r = i + 1, len(nums) - 1
			while l < r:
				tree_sum = fixed_num + nums[l] + nums[r]
				if tree_sum > 0:
					r -= 1
				elif tree_sum < 0:
					l += 1
				else:
					res.append([fixed_num, nums[l], nums[r]])
					l += 1
					r -= 1
					while l < r and nums[l] == nums[l-1]:
						l += 1

		return res