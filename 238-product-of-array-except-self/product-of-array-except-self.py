class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        L = [0] * length

        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]

        R = 1
        for i in reversed(range(length)):
            L[i] = L[i] * R
            R *= nums[i]

        return L