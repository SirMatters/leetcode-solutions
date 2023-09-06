from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i, j = 0, 0

        res = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1

        return res

# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         map1 = Counter(nums1)
#         map2 = Counter(nums2)

#         res = []

#         for key in map1:
#             if key in map2:
#                 for i in range(min(map1[key], map2[key])):
#                     res.append(key)
        
#         return res