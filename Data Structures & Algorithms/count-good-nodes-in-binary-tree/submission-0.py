# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, val):
            if not node:
                return
            nonlocal res
            max_val = max(node.val, val)
            if node.val >= val:
                res += 1
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        dfs(root, root.val)
        return res