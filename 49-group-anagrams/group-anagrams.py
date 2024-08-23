class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time complexity
        # O(N)      length of strs
        # O(K)      maximum length of string in str
        # O(KlogK)  sorted each string

        # O(NK)
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()