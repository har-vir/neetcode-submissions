class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        currBest = min(heights[l], heights[r]) * (r - l)

        while l < r:
            if heights[l] >= heights[r]:
                while heights[l] >= heights[r] and r > l:
                    r -= 1
                    if currBest < min(heights[l], heights[r]) * (r - l):
                        currBest = min(heights[l], heights[r]) * (r - l)
            elif heights[r] >= heights[l]:
                while heights[r] >= heights[l] and  r > l:
                    l += 1
                    if currBest < min(heights[l], heights[r]) * (r - l):
                        currBest = min(heights[l], heights[r]) * (r - l)


        return currBest