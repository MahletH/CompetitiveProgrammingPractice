class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        if matrix == [[]] or not len(matrix): return False
        R = len(matrix)
        C = len(matrix[0])
        l = 0
        h = R*C-1
        while l < h:
            mid = (l+h)//2
            if matrix[mid//C][mid%C] == target:
                return True
            elif matrix[mid//C][mid%C] < target:
                l = mid + 1
            else:
                h = mid
        if l == h and matrix[l//C][l%C] == target: return True
        return False