class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I first convert this into a dict
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        # Need to way to order the counts
        heap = []
        for num, count in hashMap.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = [num for count, num in heap]

        # return the arry
        return result