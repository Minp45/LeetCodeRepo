# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node, targetSum):
            if not node:
                return
            if node.val == targetSum and not node.left and not node.right:
                return True
            return dfs(node.left, targetSum - node.val) or dfs(node.right, targetSum - node.val)
        
        return True if dfs(root, targetSum) else False
        