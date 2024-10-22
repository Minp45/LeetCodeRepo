class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashtable

        # There is no edge case in this problem
        
        # create a dict for visted 
        visited = {}
        # will create for loop with length of nums
        for i in range(len(nums)):
            if target - nums[i] in visited:
                return [i, visited[target - nums[i]]]
            visited[nums[i]] = i