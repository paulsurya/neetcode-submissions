class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue
                
                rKey = f'r{i}_{val}'
                cKey = f'c{j}_{val}'
                bKey = f'b{i//3}_{j//3}_{val}'

                if rKey in seen or cKey in seen or bKey in seen:
                    return False
                
                seen.add(rKey)
                seen.add(cKey)
                seen.add(bKey)

        return True