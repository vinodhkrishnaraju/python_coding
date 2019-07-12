from pdb import set_trace as bp
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        
        matrix = [x for x in [0]*A]
        list_items = [i for i in range(A*A,0,-1)]
        
        r,l = 0,0
        m,n = A,A
        while r<m and l<n:
            
            # fill the first row
            sub_matrix = []
            for i in range(l,n):
                sub_matrix += [list_items.pop()]

            matrix[r] = sub_matrix
            r += 1
            # print(list_items)
            
            bp()
            print(matrix)
            print('/n/n')
            # fill the last column
            for i in range(r,m):
                print(i)
                print(matrix[i][n-1])
                matrix[i][n-1] = list_items.pop()
            
            matrix[i][n-1] = sub_matrix
            n -= 1    
            print(matrix)
            print('/m/m')
            
            if r < m:
                # fill the last row
                for i in range(n-1,l-1,-1):
                    matrix[m-1][i] = list_items.pop()
                m -= 1 
            
            if l<n:
                # fill the first column
                for i in range(m-1,r-1,-1):
                    matrix[i][l] = list_items.pop()
                m -= 1 
            
        return matrix


print(Solution().generateMatrix(5))