class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        frequency = {}

        if len(s) != len(t):
            return False

        for ch in s:
            frequency[ch] = frequency.get(ch, 0) + 1

        for ch in t:
            if ch not in frequency:
                return False
            
            if ch in frequency:
                frequency[ch] -= 1

            if frequency[ch] < 0:
                return False

        return True