class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(res, '', 0, 0, n)
        return res


    def backtrack(self, arr, s, n_o, n_c, n):
        if len(s) == n*2:
            arr.append(s)
            return

        if n_o < n:
            self.backtrack(arr, s + '(', n_o + 1, n_c, n)

        if n_c < n_o:
            self.backtrack(arr, s + ')', n_o, n_c + 1, n)