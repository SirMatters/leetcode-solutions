class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t_row = 0
        b_row = len(matrix) - 1
        row = -1

        while t_row <= b_row:
            if t_row == b_row:
                row = t_row
                break

            if b_row - t_row == 1:
                if matrix[b_row][0] > target:
                    row = t_row
                else:
                    row = b_row
                break

            mid = (b_row + t_row) // 2

            val = matrix[mid][0]
            if val == target:
                row = mid
                break

            if val < target:
                t_row = mid
            else:
                b_row = mid - 1

        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = (r + l) // 2

            if matrix[row][mid] == target:
                return True

            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False