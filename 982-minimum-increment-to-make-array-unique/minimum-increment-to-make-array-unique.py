class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        increment = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                needed_increment = nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
                increment += needed_increment
    
        return increment
        
        # nums = [3,2,1,2,1,7]

        # nums = [1,1,2,2,3,7]
        # increment = 0

        # needed_increment = 1
        # nums = [1,2,2,2,3,7]
        # increment = 1

        # needed_increment = 1
        # nums = [1,2,3,2,3,7]
        # increment = 2

        # needed_increment = 2
        # nums = [1,2,3,4,3,7]
        # increment = 4

        # needed_increment = 2
        # nums = [1,2,3,4,5,7]
        # increment = 6