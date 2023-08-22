class Solution:
    def get_square_idx(self, row, col):
        return (col // 3 * 3) + row // 3

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = tuple(set() for _ in range(9))
        rows = tuple(set() for _ in range(9))
        squares = tuple(set() for _ in range(9))

        for row in range(9):
            for col in range(9):
                item = board[row][col]
                if item == '.':
                    continue
                square_idx = self.get_square_idx(row, col)
                if (
                    item in cols[col]
                    or item in rows[row]
                    or item in squares[square_idx]
                ):
                    return False

                cols[col].add(item)
                rows[row].add(item)
                squares[square_idx].add(item)

        return True