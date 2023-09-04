class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        first_idx = find_idx(nums, target, True)

        if first_idx == -1:
            return [-1, -1]

        last_idx = find_idx(nums, target, False)
        
        return [first_idx, last_idx]


def find_idx(arr: List[int], target: int, isFirst: bool) -> int:
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            if isFirst:
                if mid == l or arr[mid - 1] != target:
                    return mid
                r = mid - 1
            else:
                if mid == r or arr[mid + 1] != target:
                    return mid
                l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1

