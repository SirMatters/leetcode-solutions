class Solution:
	def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
		res = []
		car_arr = list(zip(position, speed))
		car_arr.sort(reverse=True)

		for i in range(len(car_arr)):
			t = (target - car_arr[i][0]) / car_arr[i][1]
			if not res:
				res.append(t)
			elif t > res[-1]:
				res.append(t)

		return len(res)