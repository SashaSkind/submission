# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def heightOf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.heightOf(root.left)
        rightHeight = self.heightOf(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return -1

        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        hightOfLeft = self.heightOf(root.left)
        hightOfRight = self.heightOf(root.right)
        if hightOfLeft == -1 or hightOfRight == -1 or abs(hightOfLeft - hightOfRight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


        