
def pretty(A):

    
    n = []
    dim = A + A -1
    for i in range(dim):
        n_ = [1] * dim
        n.append(n_)
    # initial row
    r,c = 0,0
    # final row
    R,C = dim,dim
    # iterators
    i,j = r,c
    while i<R and j<C:
        print(A,i,j,r,c,R,C)
        # first row
        for j in range(c, C):
            n[r][j] = A
        
        
        # last column
        for i in range(r, R):
            n[i][C-1] = A
        
        
        # last row
        for j in range(c, C):
            n[R-1][j] = A
        
        # first column
        for i in range(r, R):
            n[i][c] = A
      

        
        A -= 1
        r += 1
        c += 1
        i,j = r,c
        R -= 1
        C -= 1
        print(A,i,j,r,c,R,C)

    # return n
    for item in n:
        print(item)

pretty(5)

