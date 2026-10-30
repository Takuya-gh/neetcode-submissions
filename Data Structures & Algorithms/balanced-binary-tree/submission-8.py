# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            leftD = dfs(root.left)
            rightD = dfs(root.right)
            if leftD == -1 or rightD == -1:
                return -1
            if abs(leftD - rightD) > 1:
                return -1
            return 1 + max(leftD, rightD)
        if dfs(root) == -1:
            return False
        else:
            return True
