def minDistance(self, A, B):
	n = len(A) + 1
	m = len(B) + 1
	M = [[0]*m for _ in range(n)]
	for j in range(m):
	   M[0][j] = j
	for i in range(n):
	   M[i][0] = i
	for i in range(1, n):
	   for j in range(1, m):
	       c = 0 if A[i - 1] == B[j - 1] else 1
	       M[i][j] = min(M[i][j - 1] + 1, M[i - 1][j] + 1, M[i - 1][j - 1] + c)
	return M[-1][-1]