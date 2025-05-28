# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if not root:
                return 0  # base case
            left = depth(root.left)
            right = depth(root.right)
            self.res = max(self.res, left+right)
            return 1 + max(left, right)
        depth(root)
        return self.res
        
        