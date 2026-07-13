class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            map[num] = i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums and map[difference] != i:
                return [i, map[difference]]
