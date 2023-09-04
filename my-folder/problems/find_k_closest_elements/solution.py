class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest_idx = find_closest_element_idx(arr, x)
        
        left_pointer = closest_idx - 1
        right_pointer = left_pointer + 1
        
        while right_pointer - left_pointer - 1 < k:
            if left_pointer == -1:
                right_pointer += 1
                continue
            
            if right_pointer == len(arr) or abs(arr[left_pointer] - x) <= abs(arr[right_pointer] - x):
                left_pointer -= 1
            else:
                right_pointer += 1

        return arr[left_pointer + 1: right_pointer]
        

def find_closest_element_idx(arr: List[int], el: int) -> int:
    l, r = 0, len(arr) - 1

    while l < r:
        mid = (r + l) // 2
        if arr[mid] < el:
            l = mid + 1
        else:
            r = mid

    return l    