class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		operations_dict = {
			'-': lambda x, y: x - y,
			'+': lambda x, y: x + y,
			'*': lambda x, y: x * y,
			'/': lambda x, y: int(x / y),
		}

		tracking_stack = []

		for token in tokens:
			if token in operations_dict:
				b = tracking_stack.pop()
				a = tracking_stack.pop()
				tracking_stack.append(operations_dict[token](a, b))
			else:
				tracking_stack.append(int(token))

		return tracking_stack[0]