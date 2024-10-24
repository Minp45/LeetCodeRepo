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
        levelOrder = []
        queue = deque([root])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                currentNode = queue.popleft()
                level.append(currentNode.val)
                if currentNode.left: queue.append(currentNode.left)
                if currentNode.right: queue.append(currentNode.right)
            levelOrder.append(level)
        
        return levelOrder