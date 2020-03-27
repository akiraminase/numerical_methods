import numpy as np
import sys

matrix = None
def main():
    global matrix
    matrix = np.array([[1,1,-1],[6,2,2],[-3,4,1]],dtype=float)
    aug_matrix = np.concatenate((matrix,identity_matrix(3)),axis=1)
    #gaussian2(aug_matrix) #gaussian elimination with maximum pivoting
    LUdecomp(matrix) #LU decompose a square matrix

def identity_matrix(n):
    m = np.empty([n,n],dtype=float)
    for i in range (0,n):
        for j in range (0,n):
            if(i==j): m[i][j] = 1
            else: m[i][j] = 0
    
    return m

def gaussian2(m):
    print()
    print("Gaussian Elimination 2.0:")
    print()

    for j in range (0,m.shape[0]):
        max_pivot_row = j
        max_pivot = m[j][j]
        for a in range (1, m.shape[0]-j):
            if(m[j+a][j]>max_pivot):
                max_pivot_row = j+a
                print("maximum pivoting: R",(j+1),"<->","R",(max_pivot_row+1))
                print()
        
        m[[j,max_pivot_row]] = m[[max_pivot_row,j]]
       
        if(m[j][j]==0):
            print("no unique solution")
            break

        for i in range (j+1, m.shape[0]):
            c = (m[i][j])/(m[j][j])
            if(c==0): 
                print("c==0!!")
                continue
            for a in range (0, m[j].shape[0]):
                m[i][a]=m[i][a]-c*(m[j][a])
    
            print("row operation: R",(i+1),"-",c,"*R",(j+1))
            print(m)
            print()

def LUdecomp(m):
    L = identity_matrix(m.shape[0])

    for j in range (0, m.shape[0]):
        for i in range (j+1, m.shape[0]):
            c = (m[i][j])/(m[j][j])
            if(c==0): 
                continue
            for a in range (0, m[j].shape[0]):
                m[i][a]=m[i][a]-c*(m[j][a])
            L[i][j] = c

            print("row operation: R",(i+1),"-",c,"*R",(j+1))
            print(m)
            print()
    
    print("matrix L is:")
    print(L)
    print("matrix U is:")
    print(m)

main()