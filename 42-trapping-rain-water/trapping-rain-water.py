class Solution:
    def trap(self, height: List[int]) -> int:
        # i need to use a decreatring monotonic stack
        stack = []
        water_trapped = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                
                if not stack:
                    break
                
                distance = i - stack[-1] - 1

                bounded_height = min(height[stack[-1]], h) - height[top]

                water_trapped += distance * bounded_height
            stack.append(i)
        return water_trapped
        