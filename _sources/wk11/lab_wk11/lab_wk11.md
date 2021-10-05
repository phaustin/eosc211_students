---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.2
      jupytext_version: 1.10.3
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region -->
# Lab Week 11

## EOSC 211

### Learning Objectives:

1. Interpolate data
2. Learn something cool about coastal upwelling and salitity/density gradients


### Intro 

During coastal upwelling, dense deep water is brought up over the shelf-break onto the shallow shelf. In theory, we
then see horizontal gradients of density - at the same depth, water is heavier inshore. Heavier water is usually more
saline, so we also see saltier water inshore. In this lab we are going to examine some salinity data from sections
south-west of Vancouver Island. Ultimately, we want to answer the question: Is water more saline on the shelf at
this time? There are two steps to this process:

* Interpolate data along oceanographic sections to a common distance from the shelf edge.
* Compare the mean profiles at a distance of 0 and 20 km from the shelf edge to see if they are statistically different.
<!-- #endregion -->

```python
from e211_lib import e211
import numpy as np
from matplotlib import pyplot as plt

from scipy import interpolate as itp
```

```python
# get the raw data
shiptrack_raw = e211.loadmat("lab_11_data.mat")  # track and data from the FK009A cruise
southVI_raw = e211.loadmat("SouthVI.mat")  # bathymetry of south vancouver island

shiptrack_raw.keys()
```

```python
# do some data scrubbing, repackage into straightforward dictionaries
southVI = {
    "lon": southVI_raw["SouthVI"]["lon"][0, 0].flatten(),
    "lat": southVI_raw["SouthVI"]["lat"][0, 0].flatten(),
    "depth": southVI_raw["SouthVI"]["depth"][0, 0]
}

shiptrack = {
    "depths": shiptrack_raw["depths"].flatten(),
    "lat": shiptrack_raw["lat"].flatten(),
    "lon": shiptrack_raw["lon"].flatten(),
    "lat200": shiptrack_raw["lat200"].flatten(),
    "lon200": shiptrack_raw["lon200"].flatten(),
    "saln": shiptrack_raw["saln"],
    "tempr": shiptrack_raw["tempr"].flatten(),
}
```

```python
## we could recycle the mean2d function from week 9 to smooth the data before plotting
```

```python
# make some plots to show the problem statement
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(15,4))

# mask the depth array, taking all land (i.e. depth > 0) elements to nan
southVI["depth"][southVI["depth"] > 0] = np.nan

# create 200 meter contours, spanning the whole range of depths
levels = np.arange(-3000, 200, 200)

cont = ax1.contourf(southVI["lon"], southVI["lat"], southVI["depth"], levels=levels, cmap="GnBu_r")
ax1.plot(shiptrack["lon"], shiptrack["lat"], color="black")
ax1.plot(shiptrack["lon200"], shiptrack["lat200"], color="black", linestyle=":")
ax1.set_title("Ship's Track for the FK009A Cruise")

sal = ax2.contourf(shiptrack["saln"], origin="upper", cmap="winter")
ax2.set_title("FK009A Measurements, Salinity as a Function of Depth")

plt.colorbar(cont, ax=ax1, label="Elevation/Depth (m)")
plt.colorbar(sal, ax=ax2, label="Salinity (parts per 1000 NaCl)")
```

The ship's track over the shelf is shown on the left, and the corresponding profiles of salinity as functions of depth. We would like to know about the salinity profiles in relation to the shelf rather than the somewhat arbitrary ship track. To do this, we will need to use *interpolation* to compensate for ship's data being unevenly spaced and not perfectly lining up with the map grid spacing.


First, define a function that calculates the distance between the ship's path and the track. Mathematically, we write  the distance between two points as

$$
d = \sqrt{\Delta x^2 + \Delta y^2}
$$

To convert from degrees to kilometers, use:

$$
\Delta x = \Delta lon \times 111 \times cos(lat)
$$

$$
\Delta y = \Delta lat \times 111
$$

Write a function `shortest_dist()` that takes in the ship track and shelf coordinates (the 200m depth contour line), and returns a 1D array containing the shortest distance from the each point along the ship track to the shelf. Make sure to include a docstring, and that your cosine function is in degrees, not radians

```python
# andrew's soln
def shortest_dist(pathlon, pathlat, linelon, linelat):
    """
    Finds shortest distance from a point to a line.
    Loops through each element in LAT and LON and finds the minimum
    distance from that point to the line given by 'linelat' and
    'linelon'. For example, if 'linelon' and 'linelat' specify the
    200 m contour, it returns a new array containing the shortest distance
    from each point given by lon and lat to that contour.
    """
    dist = np.empty_like(pathlon)
    
    for i in range(len(pathlon)):
        # convert to km and find the shortest path from each point in
        # path to line. save each shortest distance in dist
        deltax = (pathlon[i] - linelon) * 111.0 * np.cos(np.deg2rad(pathlat[i]))
        deltay = (pathlat[i] - linelat) * 111.0
        s_dist = np.min((deltax ** 2 + deltay ** 2) ** 0.5)
        dist[i] = s_dist
        
        # If the point is to the LEFT of the 200 m contour, write the
        # distance as a negative value
        ind = np.abs(pathlat[i] - linelat).argmin()
        if pathlon[i] < linelon[ind]:
            dist[i] *= -1
    return dist
```

```python
# test the function by visiualizing results. do they make sense? (yes)
shiptrack["dist_from_shelf"] = shortest_dist(
    shiptrack["lon"], shiptrack["lat"], shiptrack["lon200"], shiptrack["lat200"]
)
plt.plot(shiptrack["dist_from_shelf"])
```

Now that we have an array describing the ship's position in relation to the shelf, let's plot our data again, but this time with distance from shelf on the x axis and depth on the y axis:

```python
fig, ax = plt.subplots()

cont = ax.contourf(shiptrack["dist_from_shelf"], shiptrack["depths"], shiptrack["saln"], cmap="winter")
ax.set_xlabel("Distance from shelf (km)")
ax.set_ylabel("Depth (m)")

plt.gca().invert_yaxis()
plt.colorbar(cont, label="Salinity (parts per 1000 NaCl)")
```

We can start to see the horizontal salinity gradient we originally hypothesized, but there are obvious gaps and overlaps in the data. Ideally, we would like an evenly spaced grid with no missing (NaN) values. To do this, we need to interpolate. Check out the docs for the following scipy interpolation functions

[nearest neighbour](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.NearestNDInterpolator.html)

[polynomial](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.interpolate.interp2d.html)

```python

```
