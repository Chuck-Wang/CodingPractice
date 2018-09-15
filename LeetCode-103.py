# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = []
        nextStack = []
        direct = True
        ans = []

        stack.append(root)

        while stack:
            level = []
            while stack:
                node = stack.pop()
                level.append(node.val)
                if direct:
                    nextStack.append(node.left)
                    nextStack.append(node.right)
                else:
                    nextStack.append(node.left)
                    nextStack.append(node.right)
            stack = nextStack
            direct = not direct
            ans.append(level)
        return ans
