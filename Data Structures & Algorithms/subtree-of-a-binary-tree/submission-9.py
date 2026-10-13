# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sequenceStart = False
        sameTree = False

        if not subRoot:
            return True 

        if not root:
            return False

        if sequenceStart and (not root and not subRoot):
            return True
        
        if root.val == subRoot.val:
            sequenceStart = True
        else:
            sequenceStart = False
        
        if sequenceStart:
            sameTree = self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        if sameTree:
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
