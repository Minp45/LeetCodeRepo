class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # Step 1: Create a dictionary for all characters in t
        t_dict = {}
        for letter in t:
            if letter not in t_dict:
                t_dict[letter] = 1
            else:
                t_dict[letter] += 1
        
        # Step 2: Initialize pointers, window counts, and min window variables
        l = 0
        r = 0
        cur_dict = {}
        required = len(t_dict)  # Number of unique characters in t that must be in the window
        formed = 0  # Number of unique characters in the current window that match the required count
        min_len = float('inf')
        min_left = 0
        
        # Step 3: Start sliding window
        while r < len(s):
            # Add character from the right pointer to cur_dict
            char = s[r]
            if char in t_dict:
                cur_dict[char] = cur_dict.get(char, 0) + 1
                # If the current character's frequency matches t_dict, increment formed
                if cur_dict[char] == t_dict[char]:
                    formed += 1
            
            # Step 4: When all characters from t are in the window, move the left pointer to minimize
            while l <= r and formed == required:
                char = s[l]
                
                # Update the minimum window
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_left = l
                
                # Remove character from the left pointer from cur_dict
                if char in t_dict:
                    cur_dict[char] -= 1
                    if cur_dict[char] < t_dict[char]:
                        formed -= 1
                
                l += 1  # Move the left pointer to shrink the window
            
            r += 1  # Expand the window by moving the right pointer
        
        # Step 5: Return the minimum window substring if found, otherwise an empty string
        return s[min_left:min_left + min_len] if min_len != float('inf') else ""
