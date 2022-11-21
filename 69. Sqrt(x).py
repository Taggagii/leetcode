import math

# class Solution(object):
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         # really just asking, what is the closest power of 2 to this number
#         i = 0
#         i2 = 0
#         while (i2 := i * i) < x:
#             i += 1
#         if x == i2: # if it's a perfect square just return it
#             return i
#         # if it's not a perfect square then return the previous i
#         return i - 1

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # use the babylonian method of approximation
        # take any inital guess 
        guess = 500
        # apply the formula to improve the guess
        for _ in range(100):
            guess = (guess + (x / guess)) / 2
        return int(guess)


solutionObj = Solution()
for i in range(1000):
    print(solutionObj.mySqrt(i) == int(math.sqrt(i)))