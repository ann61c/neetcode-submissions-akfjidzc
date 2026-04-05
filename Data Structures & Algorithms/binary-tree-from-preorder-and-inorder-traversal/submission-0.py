# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
                return None
        root = TreeNode()
        root.val = preorder[0]
        # preorder: root, left, right
        # inorder: left, root, right
        mid_index = inorder.index(preorder[0])

        left_inorder_slice = inorder[0 : mid_index]
        right_preorder_slice = inorder[mid_index + 1 : ]
        left_preorder_slice = preorder[1 : 1 + mid_index]
        right_preorder_slice = preorder[mid_index+ 1: ]

        root.left = self.buildTree(left_preorder_slice, left_inorder_slice)
        root.right = self.buildTree(right_preorder_slice, right_preorder_slice)
        return root