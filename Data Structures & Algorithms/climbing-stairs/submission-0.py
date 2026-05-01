class Solution:
    def climbStairs(self, n: int) -> int:
        self.total = 0
        self.recursiveClimb(1, n)
        self.recursiveClimb(2, n)
        return self.total
        
    def recursiveClimb(self, curr, n):
        if curr > n:
            return
        if curr == n:
            self.total += 1
            return
        self.recursiveClimb(curr+1, n)
        self.recursiveClimb(curr+2, n)

#total is being overwritten, find out how to recursively preserve variable