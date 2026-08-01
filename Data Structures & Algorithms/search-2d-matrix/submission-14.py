class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        lr = 0
        rr = rows - 1
        rc = cols - 1
        if target == matrix[0][0]:
            return True
        while lr < rr:
            medr = (rr + lr + 1) // 2
            if matrix[medr][0] == target:
                return True
            elif matrix[medr][0] < target:
                lr += 1
            else:
                rr = medr - 1

        l = 0 
        r = rc
        while l <= r:
            med = (l + r) // 2
            if matrix[lr][med] == target:
                return True
            elif matrix[lr][med] < target:
                l = med + 1
            else:
                r = med - 1
        return False

                

