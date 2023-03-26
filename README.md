# Foreground Cleaning of HI Intensity Maps with Principal Component Analysis (PCA) 

This repository contains code written and adapted by Gracie McGill for the senior honours project titled above. 
This project aims to investigate the use of PCA as a foreground removal technique for cosmological HI insensity mapping. In order to do this code was written to apply PCA to data to remove a specified number of 'prinicpal components'. The functions to do this are contained in the script: 'PCA.py'. This repository also contains notebooks which apply this cleaning to the data and analyse the resulting maps.  <br/>

## Notebooks 
These notebooks contain the analysis done for this project. The notebook 'EXPLORING_THE_SIMULATED_DATA' loads in the simulated data from https://github.com/IntensityTools/MultipoleExpansion (see acknowledgements) and explores the properties of the different componets of this data. The other three notebooks apply PCA foreground cleaning to the simulated data (and the smoothed simulated data) and the MeerKAT data (see acknowledgements).

## Acknowledgements
##### Code to produce the power spectrum is from: https://github.com/paulassoares/gpr4im : <br/>
Paula S Soares, Catherine A Watkinson, Steven Cunnington, Alkistis Pourtsidou, Gaussian Process Regression for foreground removal in H i Intensity Mapping experiments, Monthly Notices of the Royal Astronomical Society, Volume 510, Issue 4, March 2022, Pages 5872–5890, https://doi.org/10.1093/mnras/stab2594 

##### The notebook analysing the MeerKAT data was adapted from a notebook written by Isabella Carucci (which uses the same data):<br/>
Steven Cunnington, Yichao Li, Mario G Santos, Jingying Wang, Isabella P Carucci, Melis O Irfan, Alkistis Pourtsidou, Marta Spinelli, Laura Wolz, Paula S Soares, Chris Blake, Philip Bull, Brandon Engelbrecht, José Fonseca, Keith Grainge, Yin-Zhe Ma, H i intensity mapping with MeerKAT: power spectrum detection in cross-correlation with WiggleZ galaxies, Monthly Notices of the Royal Astronomical Society, Volume 518, Issue 4, February 2023, Pages 6262–6272, https://doi.org/10.1093/mnras/stac3060

##### The simulated data and the smoothing function (adapted from teletools.py) were from https://github.com/IntensityTools/MultipoleExpansion :
Steven Cunnington, Alkistis Pourtsidou, Paula S Soares, Chris Blake, David Bacon, Multipole expansion for H i intensity mapping experiments: simulations and modelling, Monthly Notices of the Royal Astronomical Society, Volume 496, Issue 1, July 2020, Pages 415–433, https://doi.org/10.1093/mnras/staa1524

##### The scikit-learn code for PCA was also used in the notebook analysing the simulated data:
Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V. and Vanderplas, J., 2011. Scikit-learn: Machine learning in Python, the Journal of machine Learning research, 12, pp.2825-2830, https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html

 @graciemcgill 
