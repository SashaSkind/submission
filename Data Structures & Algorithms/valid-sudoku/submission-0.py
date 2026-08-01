class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # board[row][col]
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]
        for row_num, row  in enumerate(board):
            for col_num, elem in enumerate(board[row_num]):
                box_index = (row_num // 3) * 3 + col_num // 3
                if elem != ".":
                    if elem not in row_set[row_num]:
                        row_set[row_num].add(elem)
                    else:
                        return False
                    if elem not in col_set[col_num]:
                        col_set[col_num].add(elem)
                    else:
                        return False
                    if elem not in box_set[box_index]:
                        box_set[box_index].add(elem)
                    else:
                        return False
        return True
                

        