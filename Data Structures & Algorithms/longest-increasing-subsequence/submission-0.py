class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums[:i+1])):
                if nums[j] < nums[i] and memo[j] + 1 >= memo[i]:
                    memo[i] = memo[j] + 1
        
        return max(memo)