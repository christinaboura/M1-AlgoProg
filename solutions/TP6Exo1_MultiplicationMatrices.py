#-*- coding: utf-8 -*-

def ordreMatrices(P):
    n = len(P)-1
    M = [[0 for i in range(n+1)] for i in range(n+1)]
    S = [[0 for i in range(n+1)] for i in range(n+1)]
    
    for i in range(n):
        M[i][i] = 0
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            M[i][j] = 4294967296 #2^32-1 considéré comme très grand
            for k in range(i,j):
                q = M[i][k] + M[k+1][j] + P[i-1]*P[k]*P[j]
                if q < M[i][j]:
                    M[i][j] = q
                    S[i][j] = k
    return [M,S]

def printMatrix(M, n):
    for i in range(1,n):
        for j in range(i+1, n):
            print("i = ", i,  "j = ", j, ": m = ", M[i][j])
        print()

P = [5, 10, 3, 12, 5, 50, 6]

L = ordreMatrices(P)
#printMatrix(L[0], len(P))
print(L[0][1][len(P)-1])

def printParentheses(S,i,j):
    if i==j:
        print("A{0}".format(i), end='')
    else:
        print("(", end='')
        printParentheses(S,i,S[i][j])
        printParentheses(S,S[i][j]+1,j)
        print(")", end='')

printParentheses(L[1],1,len(P)-1)
print()
