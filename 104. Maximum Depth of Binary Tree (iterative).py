# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tempMax = 0
        realMax = 0
        stack = []
        curNode = root
        while True:
            if curNode is None:
                realMax = max(realMax, tempMax)
                if not stack:
                    break
                curNode, tempMax = stack.pop()
            else:
                tempMax += 1
                stack.append((curNode.right, tempMax))
                curNode = curNode.left
        return realMax
                