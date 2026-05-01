class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}

        for i in range(len(nums)):
            candidates[target-nums[i]] = i

        for j in range(len(nums)):
            if nums[j] in candidates and candidates[nums[j]] != j:
                return [j, candidates[nums[j]]]
