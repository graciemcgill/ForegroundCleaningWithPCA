# -*- coding: utf-8 -*-
'''  
Script to apply a gaussian beam convolution to an image to replicate the smoothing effects
of limited telescope resoltution in real data. 
Adapted from: https://github.com/IntensityTools/MultipoleExpansion/blob/master/teletools.py 
'''
import numpy as np
from scipy import fftpack


def makebins(lx,ly,nx,ny):
    ''' 
    Make bins for gaussian smoothing. 
    Input paramaters: lx,ly = physical dimensions of the image in degrees; 
    nx, ny = dimesions of image in pixels. 
    Outputs: x and y minimum values, bin widths and bin centres.
    '''
    xmin, ymin = 0, 0
    xwidth, ywidth = lx, ly
    xbins = np.linspace(xmin,lx,nx+1)
    ybins = np.linspace(ymin,ly,ny+1)
    xbincentres = xbins+(xbins[1]-xbins[0])/2
    xbincentres = xbins[:len(xbins)-1] # remove last value since this is outside of bins
    ybincentres = ybins+(ybins[1]-ybins[0])/2
    ybincentres = ybins[:len(ybins)-1] # remove last value since this is outside of bins
    return xmin,ymin,xwidth,ywidth,xbincentres, ybincentres


def smoothimage(image,lx,ly,nx,ny,sig):
    '''
    Takes a flat image and runs a convolution to smooth the image. Convolution kernel
    is a Gaussian with an input sigma. Units in degrees. 
    Input parameters: image = image to be smoothed, 
    lx,ly = physical dimensions of the image in degrees, 
    nx, ny = dimesions of image in pixels and sig = beam size in degreees.
    Outputs: smoothed image
    '''
    xmin,ymin,xwidth,ywidth,xbincentres,ybincentres = makebins(lx,ly,nx,ny)
    #Create Gaussian field
    x = xbincentres
    y = ybincentres[:,np.newaxis]
    x0 = xmin+xwidth/2
    y0 = ymin+ywidth/2
    gaussian = np.exp(-0.5 * (((x-x0)/sig)**2 + ((y-y0)/sig)**2))
    gaussian = np.swapaxes(gaussian,0,1)
    A = np.sum(gaussian)
    gaussian = gaussian/A #normalise gaussian so that all pixels sum to 1
    ft = fftpack.fft2(image)
    ft_gauss=fftpack.fft2(gaussian)
    smoothimage = fftpack.ifft2(ft*ft_gauss)
    smoothimage = np.real(smoothimage)
    #Now shift the quadrants around into correct position
    return fftpack.fftshift(smoothimage)


