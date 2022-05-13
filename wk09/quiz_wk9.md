---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: -all
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Quiz Week 9:  Debugging with Functions solution

*Name*
*Student number*
*Group:*


## Question 1 

Identify and fix the up to 9 bugs (depends how you count them) in the following code.  You can assume the function declaration line has no bugs

```{code-cell} ipython3
:lines_to_next_cell: 2
:trusted: true

import numpy as np

def lat_lonbounds_to_indices(lons,lats,wlon,elon,slat,nlat):

    """  finds and returns the indices in lat, lon arrays that correspond
         to N/S and E/W bounds for a region.
         
         Note:  arghwere() returns the indices of all the points in the array 
         for which each condition is true.  See example below.
         
    """
    iwest = np.min(np.argwhere(lons>=elon))   
    ieast = np.max(np.argwhere(lons<=wlon))
    isouth = np.min(np.argwhere(lats>=slat)) 
    inorth = np.max(np.argwhere(lats<=nlat))
                
    return iwest,ieast,isouth,inorth
                
# can assume the next 6 lines are correct.             
lon = np.arange(0,360,30)
lat = np.arange(-90,91,10)
lon1 = 200
lon2 = 250
lat1 = 0
lat2 = 30                
                   
i2,i1,i3,i4 = def lat_lonbounds_to_indices(lons,lats,lon1,lat1,lon2,lat2) 
sub_lons = lon[i1:i2+1]   
sub_lats = lat[i3:i4+1]
```

```{code-cell} ipython3
:trusted: true

# example with np.argwhere
import numpy as np
x = np.array([ 0, 5, -9 ])
ix = np.argwhere(x<=0)
ix
```

## Question 2

In the following version of the code I am hoping to pass my lat, lon bounds as using keyword arguments specified by the dictionary, `lims_dict`.  How would I modify the input arguments to my function now to do this? 

```
lon = np.arange(0,360,30)
lat = np.arange(-90,91,10)   
lims_dict={"wlon":250,"elon":300,"slat":0,"nlat":31}
                   
i1,i2,i3,i4 = lat_lonbounds_to_indices(*enter your input arguments here*) 
```

