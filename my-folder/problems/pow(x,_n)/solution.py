class Solution:
    def binary_exp(self, x: float, n: float) -> float:
        if n == 0: return 1.0
        if n < 0: return (1.0 / self.binary_exp(x, -n))

        if n % 2 != 0:
            return x * self.binary_exp(x * x, (n - 1) / 2)
        
        return self.binary_exp(x * x, n / 2)

    def myPow(self, x: float, n: int) -> float:
       return self.binary_exp(x, n)
