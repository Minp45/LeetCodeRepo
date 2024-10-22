class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create a dict for thr count of letters in magazine
        magazineChars = Counter(magazine)
        
        for char in ransomNote:
            if magazineChars[char] > 1:
                 magazineChars[char] -= 1
            elif magazineChars[char] == 1:
                del magazineChars[char]
            else:
                return False
        return True

