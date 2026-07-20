class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = {}

        for num in nums:
            if num in frequency:
                return True
            else:
                frequency[num] = 1

        return False
        