from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Correct the matrix dimensions
        height = len(mat)  # Number of rows
        width = len(mat[0])  # Number of columns
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # Possible directions (right, left, down, up)

        queue = deque()
        
        # Initialize queue with all the 0 cells and set all 1 cells to infinity
        for row in range(height):
            for col in range(width):
                if mat[row][col] == 0:
                    queue.append((row, col))  # Add 0s to the queue
                else:
                    mat[row][col] = float('inf')  # Mark 1s as infinity
        
        # BFS to find the minimum distance to the nearest 0
        while queue:
            row, col = queue.popleft()

            # Check all four directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # If the new cell is within bounds and has a larger distance, update it
                if 0 <= new_row < height and 0 <= new_col < width and mat[new_row][new_col] > mat[row][col] + 1:
                    mat[new_row][new_col] = mat[row][col] + 1  # Update distance
                    queue.append((new_row, new_col))  # Add updated cell to the queue
        
        return mat  # Return the matrix directly, not wrapped in a list
