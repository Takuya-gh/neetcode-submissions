# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.dfs(root) == -1:
            return False
        else:
            return True

    def dfs(self, root) -> int:
        if not root:
            return 0
        leftD = self.dfs(root.left)
        rightD = self.dfs(root.right)
        if leftD == -1 or rightD == -1:
            return -1
        if abs(leftD - rightD) > 1:
            return -1
        else:
            return 1 + max(leftD, rightD)