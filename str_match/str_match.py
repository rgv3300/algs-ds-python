def str_match(p,t):
    m = len(p)
    n = len(t)

    for i in range(0,n-m):
        j = 0
        while j < m and t[i + j] == p[j]:
            j = j+1
        if j == m:
            return i


