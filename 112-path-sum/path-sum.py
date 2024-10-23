# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # this is a dfs method
        def dfs(node, currSum):
            if not node:
                return False
            if not node.left and not node.right and currSum == node.val:
                return True
            return dfs(node.left, currSum - node.val) or dfs(node.right, currSum - node.val) 

        return dfs(root, targetSum)

