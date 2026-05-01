class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        result = 1
        for i, n in enumerate(nums):
            for i2, num in enumerate(nums):
                if i2 != i:
                    result *= num
            output.append(result)
            result = 1
    
        return output
