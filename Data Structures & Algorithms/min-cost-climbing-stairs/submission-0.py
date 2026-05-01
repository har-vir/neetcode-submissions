class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        currTotal = [-1 for x in range(len(cost))]
        
        for i in range(len(cost)):
            if i <= 1:
                currTotal[i] = cost[i]
            else:
                currTotal[i] = cost[i] + min(currTotal[i-1], currTotal[i-2])
        print(currTotal)
        return min(currTotal[i], currTotal[i-1])
