class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        heights.append(0)  # Append a 0 height to handle remaining bars in the stack at the end

        for i, num in enumerate(heights):
            # If the current height is less than the height at the stack's top, pop the stack
            while stack and num < heights[stack[-1]]:
                height = heights[stack.pop()]
                # Calculate the width: if stack is empty, the width is i, otherwise it's the distance between indices
                width = i if not stack else i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)  # Push the current index onto the stack

        return res
