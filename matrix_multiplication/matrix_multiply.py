def matrix_multiply(a,b,c):
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    print(c)


a = [[1,2,3],[3,4,5]]
b= [[4,5,6],[6,5,4],[1,2,4]]
c = [[0,0,0],[0,0,0],[0,0,0]]
matrix_multiply(a,b,c)
