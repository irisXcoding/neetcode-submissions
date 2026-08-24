class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        c = len(matrix[0])
        r = len(matrix)
        left, right = 0, c*r-1
        while left<=right:
            mid = int((left+right)/2)
            r_idx = mid//c
            c_idx = mid%c
            if matrix[r_idx][c_idx]==target:
                return True
            elif matrix[r_idx][c_idx]<target:
                left = mid+1
            else:
                right = mid -1
        return False

        