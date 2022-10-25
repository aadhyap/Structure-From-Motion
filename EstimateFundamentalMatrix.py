#Estimating fundamental matrix

class EstimateFundamentalMatrix:
    def __init__(self, points):










        n = x1.shape[1]
        if x2.shape[1] != n:
            raise ValueError("Number of points don't match.")
        
        # build matrix for equations
        A = zeros((9,9))
        i = 0
        for keys in range(len(points)):
            refpoints = points[keys]
            A[i] = [[keys[0]*refpoints[0], keys[0]*refpoints[1], keys[0],
                    keys[1]*refpoints[0], keys[1]*refpoints[1], keys[1], refpoints[0], refpoints[1], 1 ]]
            i = i + 1


                
        # compute linear least square solution
        U,S,V = linalg.svd(A)
        F = V[-1].reshape(3,3)
            
        # constrain F
        # make rank 2 by zeroing out last singular value
        U,S,V = linalg.svd(F)
        S[2] = 0
        F = dot(U,dot(diag(S),V))
        F = F/F[2,2]
        print("_____F_____")
        print(F)

        
        return F/F[2,2]

            


#if __name__ == '__main__':
     #FundamentalMatrix = EstimateFundamentalMatrix()