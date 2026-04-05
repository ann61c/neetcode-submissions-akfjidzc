# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(root, found):
            if not found and not root:
                return True
            if not found or not root:
                return False
            if found.val != root.val:
                return False
            return isSame(root.left, found.left) and isSame(root.right, found.right)
        if not isSame(root, subRoot):
            return isSame(root.left, subRoot) or isSame(root.right, subRoot)
        return isSame(root, subRoot)