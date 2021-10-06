---
jupytext:
  cell_metadata_filter: all
  formats: ipynb,md:myst
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Indexing worksheet

## Read in the data

This is a fake satellite image with longwave flux in a vector called "flux" and brightness temperature in a vector called "temp".  I've stored them in an [npz file](https://numpy.org/doc/stable/reference/generated/numpy.savez.html) using np.savez.  If you
are working on your laptop, you can download the npz file here: [temp_flux.npz]( https://github.com/phaustin/eosc211_students/blob/e211_live_main/wk05/temp_flux.npz)

In the cells below, you'll be asked to add new points to the figure, and then
redisplay using `display(fig)`

```{code-cell} ipython3
import numpy as np
from matplotlib import pyplot as plt
filename='temp_flux.npz'
the_data = np.load(filename)
flux = the_data['flux']
temp = the_data['temp']
fig, ax = plt.subplots(1,1)
ax.plot(flux,temp, 'b.');
```

you can redisplay a modfied figure like this:

```{code-cell} ipython3
ax.set_title('flux vs. temperature')
ax.set_xlabel('shortwave flux (W/m^2)')
ax.set_ylabel('temperature K')
display(fig)
```

## Q1 -- `logical_and` for flux

Find all pixels with flux values between 500 and 550 $W/m^2$ and color them yellow.

```{code-cell} ipython3
# your code here
```

## Q2 -- `logical_and` for temperature and flux

Now extend this by finding all pixels with fluxes between 500 and 550 $W/m^2$
and temperatures greater than 300 K and color those cyan.  Redisplay the figure.

```{code-cell} ipython3
# your code here
```

## Q3 -- argmax

Now find the index of the maximum temperature, and use that index to find the flux for that hottest pixel.
Make that pixel a large green dot with `ax.plot(the_flux,the_temp,'g.',markersize=20)`

```{code-cell} ipython3
# your code here
```
