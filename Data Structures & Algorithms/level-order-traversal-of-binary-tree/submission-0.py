# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        levels = []
        def helper(node, depth):
            if len(levels) == depth:
                levels.append([])
            levels[depth].append(node.val)
            if node.left:
                helper(node.left, depth + 1)
            if node.right:
                helper(node.right, depth + 1)
        helper(root, 0)
        return levels