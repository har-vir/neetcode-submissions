class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, n in enumerate(numbers):
            nums_dict[n] = i
        
        for i in range(len(numbers)):
            if (target - numbers[i]) in nums_dict:
                return [i+1, nums_dict[target - numbers[i]]+1]
        
