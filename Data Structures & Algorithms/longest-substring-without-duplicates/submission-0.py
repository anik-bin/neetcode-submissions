class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}

        left = 0
        max_length = 0

        for right in range(len(s)):
            ch = s[right]

            # IF DUPLICATE IS FOUND
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            # UPDATE RIGHT POINTER
            last_seen[ch] = right

            # CALCULATE CURRENT WINDOW LENGTH
            current_window_length = right - left + 1
            max_length = max(current_window_length, max_length)

        
        return max_length
        