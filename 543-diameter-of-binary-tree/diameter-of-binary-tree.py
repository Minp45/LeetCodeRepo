class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Initialize a global variable to track the diameter

        # Helper function to calculate height
        def height(node):
            if not node:
                return 0
            # Recursively calculate the height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update the diameter at this node
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of this node
            return 1 + max(left_height, right_height)
        
        # Compute the height starting from the root, which updates the diameter
        height(root)
        
        return self.diameter
