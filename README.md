# charge-density-fluctuations
This repository contains the source code related to my research into charge-density fluctuations
in graphene. For details see: 

T.P. Mehay, R. Warmbier, A. Quandt, Investigation of density fluctuations in graphene using the fluctuation-dissipation relations, In Computational Condensed Matter, 2017, , ISSN 2352-2143, https://doi.org/10.1016/j.cocom.2017.08.008.
(http://www.sciencedirect.com/science/article/pii/S2352214317301557)

# Explanation
This code computes the autocorrelation function associated with charge-density fluctuations. This is achieved using a form of the fluctuation-dissipation relations associated with the response of an electron gas to a test charge:

http://latex.codecogs.com/gif.latex?%5Cleft%20%5Clangle%20%5Crho_%7Bq%7D%28t%29%5Crho%5E%7B%5Cdagger%7D_%7Bq%7D%20%280%29%5Cright%20%5Crangle%20%3D%20%5Cfrac%7Bq%5E%7B2%7D%7D%7B2%20e%5E%7B2%7D%7D%20%5Cint%20d%5Comega%20e%5E%7Bi%20%5Comega%20t%7D%20%5Cfrac%7B%5CIm%20%5C%7B%5Cepsilon%5E%7B-1%7D%28%5Comega%2C%20%5Ctextbf%7Bq%7D%29%5C%7D%7D%7Be%5E%7B-%5Cbeta%20%5Chbar%20%5Comega%7D%20-%201%7D
