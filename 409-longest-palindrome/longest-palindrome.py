class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        char_dict = {}
        result = 0
        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                del char_dict[char]
                result += 2
            print(char_dict)
        if char_dict:
            return result + 1
        return result


        