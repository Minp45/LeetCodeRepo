class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        res = cur_sum
        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i-k]
            res = max(cur_sum, res)
        return res/k
