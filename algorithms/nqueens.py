def solveNQueens(self, A):
    result = []
    def solve(A, res): 
        if len(res) == A: 
            result.append(res)
        for i in range(1, A+1):
            if not self.attack(res, i): 
                solve(A, res + [i]) 
    solve(A, []) 
    return [[ "."*(i-1)+"Q"+"."*(A-i) for i in cols] for cols in result]
        
def attack(self, prev_row, pos): 
    # check if row clashes
    # check if diagnol clashes
    for i in range(len(prev_row)):
        row_clash = prev_row[i] == pos
        diagnol_clash = abs(len(prev_row)- i) == abs(prev_row[i]-pos)
        if row_clash or diagnol_clash: 
            return True
    return False