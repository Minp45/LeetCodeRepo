class Solution:
    def isPalindrome(self, s: str) -> bool:
        def checkChar(char):
            # Check if the character is alphanumeric
            if ('0' <= char <= '9') or ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
                return True
            return False

        left = 0
        right = len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not checkChar(s[left]):
                left += 1
            while left < right and not checkChar(s[right]):
                right -= 1

            # Compare characters in a case-insensitive manner
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True