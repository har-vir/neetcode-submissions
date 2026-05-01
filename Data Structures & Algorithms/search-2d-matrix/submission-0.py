class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        first = 0
        last = len(matrix[0]) * len(matrix) - 1
        mid = (first + last) // 2
        adjusted_mid = 0

        while last >= first:
            for k in range(len(matrix)):
                if mid < len(matrix[k]) * (k+1):
                    adjusted_mid = [k, mid % len(matrix[0])]
                    break
            
            if target == matrix[adjusted_mid[0]][adjusted_mid[1]]:
                return True
            elif target < matrix[adjusted_mid[0]][adjusted_mid[1]]:
                last = mid - 1
            else:
                first = mid + 1
            mid = (first + last) // 2
            
        return False

            