class Solution:
    def insert(self, nums, length, index, value):
        nums[length] = value
        for i in range(length, index, -1):
            temp = nums[i - 1]
            nums[i - 1] = nums[i]
            nums[i] = temp
        length += 1
        return length

    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = 0
        q = 0
        while q <= n and m < len(nums1):
            if p >= m:
                while q < n:
                    m = self.insert(nums1, m, p, nums2[q])
                    p += 2
                    q += 1
                break
            if (nums1[p] > nums2[q]):
                m = self.insert(nums1, m, p, nums2[q])
                q += 1
                p += 1
            elif (nums1[p] < nums2[q]):
                p += 1
            else:
                m = self.insert(nums1, m, p, nums2[q])
                p += 2
                q += 1

# class Solution:
#     def merge(self, nums1, m, nums2, n) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         last = m + n - 1
#         m -= 1
#         n -= 1
#         while m >= 0 and n >= 0:
#             if nums1[m] > nums2[n]:
#                 nums1[last] = nums1[m]
#                 m -= 1
#             else: 
#                 nums1[last] = nums2[n]
#                 n -= 1
#             last -= 1
        
#         while n >= 0:
#             nums1[last] = nums2[n]
#             last -= 1
#             n -= 1
            
                



print('='*100)
sol = Solution()
a = [2, 0]
b = [1]
sol.merge(a, 1, b, len(b))
print(a)

