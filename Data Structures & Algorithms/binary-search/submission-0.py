class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2

        while end >= start:

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
            
            mid = (start + end) // 2
        
        return -1
    