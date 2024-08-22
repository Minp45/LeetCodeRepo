class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorting O(nlogn), compare is O(n)
        if len(s) != len(t):
            return False
        return sorted(list(s)) == sorted(list(t))
