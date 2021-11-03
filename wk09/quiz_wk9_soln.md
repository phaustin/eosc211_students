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

## Solutions

### Q1:

```{code-cell} ipython3
:trusted: true

import numpy as np

def lat_lonbounds_to_indices(lons,lats,wlon,elon,slat,nlat):

    """  finds and returns the indices in lat, lon arrays that correspond
         to N/S and E/W bounds for a region.
    """
    bounds_dict={};
    iwest = np.min(np.argwhere(lons>=wlon))    #(2) w and e were switched
    ieast = np.max(np.argwhere(lons<=elon))
    isouth = np.min(np.argwhere(lats>=slat)) 
    inorth = np.max(np.argwhere(lats<=nlat))
    bounds_dict['lon_slice']=slice(iwest,ieast)
    bounds_dict['lat_slice']=slice(isouth,inorth)
                
    return iwest,ieast,isouth,inorth
                
              
lon = np.arange(0,360,30)
lat = np.arange(-90,91,10)
lon1 = 250
lon2 = 300
lat1 = 0
lat2 = 31                
                   
i1,i2,i3,i4 = lat_lonbounds_to_indices(lon,lat,lon1,lon2,lat1,lat2)   # (5) lon, lat, lon1, lon2, lat1, lat2, no def
sub_lons = lon[i1:i2+1]    # (2) switch i1 and i2 here or in output args
sub_lats = lat[i3:i4+1]

print(i1,i2,i3,i4)
print(lon,lat)
print(sub_lons,sub_lats)
```

    9 10 9 12
    [  0  30  60  90 120 150 180 210 240 270 300 330] [-90 -80 -70 -60 -50 -40 -30 -20 -10   0  10  20  30  40  50  60  70  80
      90]
    [270 300] [ 0 10 20 30]

+++

###  Q2:

```
i1,i2,i3,i4 = lat_lonbounds_to_indices(lons,lats,**lims_dict)
```
