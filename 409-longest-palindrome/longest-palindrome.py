class Solution:
    def longestPalindrome(self, s: str) -> int:
        nums = {}
        maxlength = 0
        for char in s:
            if char not in nums:
                nums[char] = 1
            else:
                del nums[char]
                maxlength += 2
                
        return maxlength + 1 if nums else maxlength 

        