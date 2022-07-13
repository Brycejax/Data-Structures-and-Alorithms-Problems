class Solution:
    def searchMatrix(self, matrix, target):
        arr = []
        for i in matrix:
            if i[0] <= target:
                arr = i
        
        l, r = 0, len(arr) - 1
        
        while l <= r:
            midpoint = l + (r - l) // 2
            if arr[midpoint] == target:
                return True
            elif arr[midpoint] > target:
                r = midpoint - 1
            else:
                l = midpoint + 1
                
        return False