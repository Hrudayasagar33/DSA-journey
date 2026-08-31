class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to map value -> index
        seen = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement is already stored
            if complement in seen:
                return [seen[complement], index]
            
            # Store the current number's index
            seen[num] = index
