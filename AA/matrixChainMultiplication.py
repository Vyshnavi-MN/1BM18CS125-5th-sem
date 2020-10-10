import sys
def matrixChain(lst):
    n = len(lst)
    m = [[0 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]
    for d in range(1,n):
        for i in range(1,n-d):
            j = i + d
            min = sys.maxsize
            for k in range(i,j):
                res = m[i][k] + m[k+1][j] + lst[i-1]*lst[k]*lst[j]
                if res < min:
                    min = res
                    s[i][j] = k
            m[i][j] = min
    print(m[1][n-1])
    for i in range(n-1, 1, -1):
        print(s[1][i])

matrixChain([5,4,6,2,7])