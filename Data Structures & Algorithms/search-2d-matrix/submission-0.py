class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l<=r:
            m = (l+r) // 2
            if matrix[m][-1] < target:
                l += 1
            elif matrix[m][0] > target:
                r -= 1
            else:
                break
        else:
            return False
        target_matrix = matrix[m]
        left, right = 0, len(matrix[m])-1
        while left <= right:
            mid = (left + right) // 2
            if target_matrix[mid] < target:
                left = mid + 1
            elif target_matrix[mid] > target:
                right = mid - 1
            else:
                return True
        return False

        

