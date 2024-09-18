class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # i want to store the length of list
        # next use the two variable to store the front and the back
        # until the end

        length = len(intervals)
        i = 0
        result = []

        while i != length and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < length and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        while i != length and intervals[i][0] > newInterval[0]:
            result.append(intervals[i])
            i += 1
        return result

            
        

                