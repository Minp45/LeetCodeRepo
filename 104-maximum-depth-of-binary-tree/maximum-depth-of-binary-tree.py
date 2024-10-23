# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # i can use dfs or bfs
        def height(root, depth):
            if not root:
                return depth
            return max(height(root.left, depth + 1), height(root.right, depth + 1))
        
        return height(root, 0)


