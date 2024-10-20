class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            if target - nums[i] in visited:
                return [i, visited[target - nums[i]]]
            visited[nums[i]] = i
        hashMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[nums[i]] = i