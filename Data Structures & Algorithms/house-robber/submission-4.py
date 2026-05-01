class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        memo = [0] * len(nums)
        memo[0] = nums[0]
        memo[1] = nums[1]

        for i in range(2,len(nums)):
            currBest = memo[i-1]

            for j in range(i-1):
                print(i, j)
                if nums[i] + memo[j] > currBest:
                    currBest = nums[i] + memo[j]
            memo[i] = currBest

        return memo[-1]

        