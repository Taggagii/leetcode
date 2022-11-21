# import math

# class Solution(object):
#     def lemma(self, x):
#         return int(math.log(x, 10)) + 1
    
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x < 0:
#             return False
#         if not x:
#             return True
#         stack = 0
#         length = self.lemma(x)
#         for _ in range(length // 2):
#             x, mod = divmod(x, 10)
#             stack = stack * 10 + mod
            
#         if length & 1:
#             x //= 10

#         return x == stack;

# import math

# class Solution(object):
#     def lemma(self, x):
#         return int(math.log(x, 10)) + 1
    
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x < 0:
#             return False
#         if not x:
#             return True
#         stack = 0
#         tempX = x
#         length = self.lemma(x)
#         for _ in range(length):
#             tempX, mod = divmod(tempX, 10)
#             stack = stack * 10 + mod
#         return stack == x
        
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        stringX = str(x)
        listX = []
        #populates listX
        for i in stringX:
            listX += i
        print(listX)
        #duplicate and reverse listX
        reverseListX = listX.copy()
        reverseListX.reverse()
        
        for i in range(len(listX)):
            if listX[i] != reverseListX[i]:
                return False
            
        return True

    
s = Solution()
print(s.isPalindrome(1234321))
print(s.isPalindrome(121))
print(s.isPalindrome(10))
            