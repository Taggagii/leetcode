# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkSymmetric(self, rootOne, rootTwo):
        if not (rootOne or rootTwo):
            return True
        elif not (rootOne and rootTwo):
            return False
        elif not (rootOne.val == rootTwo.val):
            return False
        
        return self.checkSymmetric(rootOne.left, rootTwo.right) and self.checkSymmetric(rootOne.right, rootTwo.left)
    
                
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkSymmetric(root.left, root.right)
                
            
           
            
                
            
        