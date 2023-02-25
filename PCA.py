"""
Script containing functions to apply PCA to data cube containing maps at different frequencies,nz. 
"""

import numpy as np 

def mean_centre(data): 
    """" 
    Function to reshape and mean-centre cube of maps so that PCA can be applied. 
    Takes in data cube of theshape [nx,ny,nz] and outputs mean-centered cube of shape
    [nz, npix] where npix=nx*ny
    """
    axes = np.shape(data)
    reshaped = np.reshape(data,(axes[0]*axes[1],axes[2]))     #reshape data so long 1d array of pixels for each z
    reshaped = np.swapaxes(reshaped,0,1)                                #swap axes so that data in form Nz, Npix
    for i in range(axes[2]):
        reshaped[i] = reshaped[i] - np.mean(reshaped[i])
    
    return reshaped

def fg_est(data,N):
    """
    Function to produce a PCA foreground estimate for data. Data input in the shape (Nz,Npix) 
    Returns a foreground estimate of the same shape.
    """
    axes = np.shape(data)
    B = selection_matrix(axes[0],N)     
    A,S = PCA(data,B)
    FG_est = np.matmul(A,S)      #estimate foreground
    
    return FG_est
                
                
    
def selection_matrix(nz,N): 
    """
    Construct the selection matrix for PCA
    """
    B = np.zeros([nz,N])    #construct selection matrix
    for i in range(nz): 
        for j in range(N): 
            if i == j: 
                B[i,j] = 1   
                
    return B



def PCA(data,B):
    """
    Apply PCA to the data
    """
    cov = np.cov(data)                         #find covariance matrix
    eig_vals, eig_vecs = np.linalg.eig(cov)    #find eigenvalues and vectors of covariance matrix
    A = np.matmul(eig_vecs, B)          #construct mixing matrix
    A_trans = A.transpose() 
    S = np.matmul(A_trans,data)         #find eigensources #mixing matrix projected onto data
    return A,S


    