class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        counts = []
        count = 1
        n = 0
        
        num, nex = nums[n], nums[n]+1


        while n < len(nums):
            if nex in nums:
                count += 1
            else:
                counts.append(count)
                count = 1
                n += 1
                if n >= len(nums):
                    break
                num, nex = nums[n], nums[n]+1
                continue
            nex += 1
        
        return max(counts)

            