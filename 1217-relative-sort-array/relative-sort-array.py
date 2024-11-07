class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # lets do the most brute force way, which is record the index of every index at arr2
        dict_arr1 = defaultdict(int)
        end_arr = []
        for element in arr1:
            if element in arr2:
                dict_arr1[element] += 1
            else:
                end_arr.append(element)
        
        result = []
        for element in arr2:
            for i in range(dict_arr1[element]):
                result.append(element)
        
        for element in sorted(end_arr):
            result.append(element)
        return result