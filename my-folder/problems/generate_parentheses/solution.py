class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		res = []
		stack = []

		def gen_par(o_num: int, c_num: int):
			if o_num == c_num == n:
				res.append("".join(stack))
				return

			if o_num < n:
				stack.append("(")
				gen_par(o_num + 1, c_num)
				stack.pop()

			if c_num < o_num:
				stack.append(")")
				gen_par(o_num, c_num + 1)
				stack.pop()

		gen_par(0, 0)
		return res