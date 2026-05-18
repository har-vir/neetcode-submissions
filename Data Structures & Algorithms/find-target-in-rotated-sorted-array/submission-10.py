class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0

        l = 0
        r = len(nums) - 1
        pivot = 0

        while l < r:
            m = (l+r)//2
            
            if nums[m] > nums[r]: 
                l = m + 1
            else:
                r = m 
        
        pivot = l
        l = 0
        r = pivot - 1

        while l <= r:
            m = (l+r)//2
            
            if nums[m] == target: 
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        l = pivot
        r = len(nums) - 1

        while l <= r:
            m = (l+r)//2
            
            if nums[m] == target: 
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1