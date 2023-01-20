# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def midIndex(self, nums):
        return len(nums) // 2
    def mid(self, nums):
        return nums[self.midIndex(nums)]
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(nums[len(nums) // 2])
        stack = [(root, nums)]

        while stack:
            node, curNums = stack.pop()
            
            mid = self.midIndex(curNums)
            leftValues = curNums[:mid]
            rightValues = curNums[mid + 1:]
            
            if leftValues:
                node.left = TreeNode(self.mid(leftValues))
                stack.append((node.left, leftValues))
            if rightValues:
                node.right = TreeNode(self.mid(rightValues))
                stack.append((node.right, rightValues))
        return root