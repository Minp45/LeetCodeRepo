class Solution:
    def climbStairs(self, n: int) -> int:
        # this is db problem because we can save all the pass proabilitys
        
        # time complexity: O(N^2)
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev1, prev2 = 1, 2
        for _ in range(3, n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        
        return curr
