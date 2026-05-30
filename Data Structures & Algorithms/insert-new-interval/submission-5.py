class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]
        
        start, end = newInterval[0], newInterval[1]
        curr = -1
        remove = []

        for i in intervals:
            if newInterval[1] >= i[0]:
                curr += 1
                if newInterval[0] <= i[1]:
                    start = min(newInterval[0], i[0])
                    end = max(newInterval[1], i[1])
                    remove.append(i)
                    break
        
        for i in intervals[curr+1:]:
            if newInterval[1] >= i[0]:
                end = max(newInterval[1], i[1])
                remove.append(i)
   
        if [start, end] == newInterval:
            intervals.insert(curr+1, [start,end])
        else: intervals.insert(curr, [start,end])
        
        for i in remove:
            intervals.remove(i)

        return intervals
        

        
