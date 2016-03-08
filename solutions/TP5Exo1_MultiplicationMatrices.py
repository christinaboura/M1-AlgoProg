def printPyramide(M, n) :
    i = 1
    for j in range(n, 1, -1) :
        l = j
        print(" "*(2*j), end = " ")
        for k in range(1, i+1) :
            print(M[k][l], end = " ")
            l = l+ 1
        print()
        i = i + 1


def printMatrix(M, n) :
    for i in range(0, n) :
        for j in range(i, n) :
            print("i = ", i,  "j = ", j, ": m = ", M[i][j])
        print(" ")

def ordreMatrices(P,l) :
    M = [[0 for i in range(l+1)] for i in range(l+1)]
    S = [[0 for i in range(l+1)] for i in range(l+1)]
    n = len(P) - 1
    
    for i in range(1, n+1) :
        M[i][i] = 0
    for l in range(2, n+1) :
        for i in range(1, n - l + 2) :
            j = i + l - 1
            M[i][j] = 1591510100 # nombre aléatoire très grand
            for k in range(i,j) :
                q = M[i][k] + M[k+1][j] + P[i-1]*P[k]*P[j]
                if q < M[i][j] :
                    M[i][j] = q
                    S[i][j] = k
    L = [M,S]
    return L

P = [5, 10, 3, 12, 5, 50, 6]

L = ordreMatrices(P, len(P)+1)

printPyramide(L[0], len(P)-1)
printMatrix(L[1], len(P))
