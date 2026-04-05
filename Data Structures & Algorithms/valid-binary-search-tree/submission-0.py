# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            while node.left:
                if node.val < node.left.val:
                    return False
                node = node.left
            while node.right:
                if node.val > node.right.val:
                    return False
                node = node.right
            return True
        return dfs(root)
        