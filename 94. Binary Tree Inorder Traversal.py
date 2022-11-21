# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        values = []
        current = root

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif (stack):
                current = stack.pop()
                values.append(current.val)
                current = current.right
            else:
                break
                
        # values = [root]
        # while True:
        #     print(values)
        #     i = 0
        #     done = True
        #     while i < len(values):
        #         value = values[i]
        #         if isinstance(value, int):
        #             i += 1
        #             continue
        #         values[i] = value.val
        #         if (value.left != None):
        #             values.insert(i, value.left)
        #         if (value.right != None):
        #             values.insert(i + 1, value.right)
        #         done = False
        #         break
        #     if done:
        #         return values
                
# values = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
values = TreeNode(3, TreeNode(1, None, TreeNode(2, None, None)))

sol = Solution()
print(sol.inorderTraversal(values))
