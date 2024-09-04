class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get the starting color (level)
        level = image[sr][sc]

        # If the starting color is the same as the target color, no need to do anything
        if level == color:
            return image

        # Recursive helper function for flood fill
        def waterFlow(row, col):
            # Check if the current position is out of bounds or not the target color
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
                return
            if image[row][col] != level:
                return
            
            # Fill the current position with the new color
            image[row][col] = color

            # Recurse in all 4 directions
            waterFlow(row - 1, col)  # Up
            waterFlow(row + 1, col)  # Down
            waterFlow(row, col - 1)  # Left
            waterFlow(row, col + 1)  # Right

        # Start the flood fill from the initial position
        waterFlow(sr, sc)
        return image