# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stackLeft = []
        stackRight = []
        curLeft = root.left
        curRight = root.right
        while True:
            if not (curLeft or curRight): # if both are None
                if not (stackLeft and stackRight):
                    return True
                curLeft = stackLeft.pop()
                curRight = stackRight.pop()
            elif not (curLeft and curRight): # ones None but the othe isn't
                return False
            elif not (curLeft.val == curRight.val): # they're different values
                return False
            else:
                stackLeft.append(curRight.left)
                curRight = curRight.right
                stackRight.append(curLeft.right)
                curLeft = curLeft.left
                
            
           
            
                
            
        