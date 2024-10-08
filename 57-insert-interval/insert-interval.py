class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        result = []
        length = len(intervals)
        i = 0
        while i < length and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < length and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        while i < length:
            result.append(intervals[i])
            i += 1
        return result