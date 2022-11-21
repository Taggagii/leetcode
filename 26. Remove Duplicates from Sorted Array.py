class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == [0]:
            return [1]
        i = len(digits) - 1
        while digits[i] == 9 and i >= 0:
            digits[i] = 0
            i -= 1
        if (digits[0] == 0):
            digits.append(0)
        digits[max(0, i)] += 1
    
        return digits

print('\n'*500)

solutionObj = Solution()
print(solutionObj.plusOne([9, 8, 9]))
print(solutionObj.plusOne([9, 9, 9]))
print(solutionObj.plusOne([1, 9]))
print(solutionObj.plusOne([9]))
print(solutionObj.plusOne([0]))