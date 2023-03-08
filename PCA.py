"""
Script containing functions to apply PCA to data cube containing maps at different frequencies,nz. 
"""

import numpy as np 
import scipy 

    
def mean_centre(data): 
    """" 
    Function to reshape and mean-centre cube of maps so that PCA can be applied. 
    Takes in data cube of the shape [nx,ny,nz] and outputs mean-centered cube of shape
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
    Function to produce a PCA foreground estimate for data. Data input must be mean-centered and in the shape (Nz,Npix). 
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
    eig_vals, eig_vecs = scipy.linalg.eig(cov)    #find eigenvalues and vectors of covariance matrix
    A = np.matmul(eig_vecs.real, B)          #construct mixing matrix
    A_trans = A.transpose() 
    S = np.matmul(A_trans,data)         #find eigensources #mixing matrix projected onto data
   
    return A,S


def clean(data,FG_est): 
    """
    Clean the data by removing the estimated foreground. Data must be in shape [nx,ny,nz] and foreground shape [nz,npix].
    """
    FG_est = FG_est.swapaxes(0,1) #reshape the foreground
    FG_est = FG_est.reshape(data.shape) 

    cleaned = data - FG_est #remove the foreground
    return cleaned


def shaping(data,xyz = True):
    """
    Function to reshape data from [nx,ny,nz] to [nz,nx,ny] or vice versa.
    """   
    if xyz == True:
        #reshape to shape zxy:
        axes = data.shape #x,y,z
        data = np.reshape(data,(axes[0]*axes[1],axes[2]))
        data = data.swapaxes(0,1)
        data = data.reshape(axes[2],axes[0],axes[1])
    else:
        #reshape from zxy to xyz
        axes = data.shape #z,x,y
        data = np.reshape(data,(axes[0],axes[1]*axes[2]))
        data = np.swapaxes(data,0,1)
        data = np.reshape(data,(axes[1],axes[2],axes[0]))
   
    
    return data

    
    
    
    
    
    
    
    
    