# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        midIndex = len(nums) // 2
        return TreeNode(nums[midIndex],
                       self.sortedArrayToBST(nums[:midIndex]),
                       self.sortedArrayToBST(nums[midIndex + 1:]))