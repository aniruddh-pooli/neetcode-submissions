class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows= set()
        cols=set()
        boxes=set()
        for r in range(9):
            for c in range(9):
                num=board[r][c]
                if num==".":
                    continue
                if ((r, num) in rows or
                    (c, num) in cols or
                    (r // 3, c // 3, num) in boxes):
                    return False

                rows.add((r, num))
                cols.add((c, num))
                boxes.add((r // 3, c // 3, num))

        return True
        