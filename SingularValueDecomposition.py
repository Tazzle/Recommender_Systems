import numpy as np
from numpy.linalg import *

X = [[3,4,3,1]
    ,[1,3,2,6]
    ,[2,4,1,5]
    ,[3,3,5,2]]

def svd(data):
     
    U, E, V = linalg.svd( data )

    #eye: return a matrix with ones on the diagonal and zeros elsewhere
    #multiply with E matrix to get sigma value
    Sigma = np.mat(np.eye(2)*E[:2])
    # - or - Sigma = np.diag(E)[:2,:2]
   
    U = U[:,:2]
    #V^T - transpose
    V =  V.transpose()[:,:2]
            
svd(X)