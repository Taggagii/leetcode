import math

def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if not x: return True
        length = int(math.log(abs(x), 10)) + 1
        flipped_x = 0
        for _ in range(length // 2):
            x, to_add = divmod(x, 10)
            flipped_x += to_add
            flipped_x *= 10
        flipped_x //= 10
        if (length & 1):
            x /= 10
        
        return x == flipped_x



thing = isPalindrome(1001)
print(thing)
