# from math import factorial

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         sumValue = 0
#         for i in range(int(n / 2) + 1):
#             sumValue += factorial(n - i) / (factorial(n - 2 * i) * factorial(i))
#         return int(sumValue)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
        a = 1
        b = 1
        for i in range(n):
            temp = a + b
            a = b
            b = temp
        return b

if __name__ == "__main__":
    so = Solution()
    for i in range(20):
        print(so.climbStairs(i), 'steps: ', i)