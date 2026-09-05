class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() 
        triplets = set()  

        for i in range(len(nums)):
            target = -nums[i]
            seen = set()

            for j in range(i + 1, len(nums)):
                required = target - nums[j]
                if required in seen:
                    triplets.add((nums[i], required, nums[j]))
                seen.add(nums[j])

        return [list(t) for t in triplets]
