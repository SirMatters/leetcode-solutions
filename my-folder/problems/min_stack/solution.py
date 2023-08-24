class MinStack:
	def __init__(self):
		self.stack: List[int] = []
		self.last_min: Optional[int] = None

	def push(self, val: int) -> None:
		self.stack.append(val)
		if self.last_min is None or val <= self.last_min:
			self.last_min = val

	def pop(self) -> None:
		val = self.stack.pop()
		if not self.stack or val == self.last_min:
			self.last_min = min(self.stack) if self.stack else None

	def top(self) -> int:
		return self.stack[-1]

	def getMin(self) -> int:
		return self.last_min