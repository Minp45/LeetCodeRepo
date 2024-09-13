class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        majority_element = length/2
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
                if counter[num] > majority_element:
                    return num