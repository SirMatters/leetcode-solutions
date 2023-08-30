class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        prim_arr = []
        o_n = 0
        c_n = 0
        start = 0

        for i, letter in enumerate(s):
            if letter == '(':
                o_n += 1
            else:
                c_n += 1

            if o_n == c_n:
                prim_arr.append(s[start:i+1])
                o_n = 0
                c_n = 0
                start = i+1
        res = ''
        for prim in prim_arr:
            res += prim[1:len(prim)-1]
        return res