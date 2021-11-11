---
jupytext:
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

+++ {"slideshow": {"slide_type": "slide"}}

# Notes for Thursday Oct. 7

## Week 5 lab

1.) Watch your brackets:

* `cosine(the_lat_radians)`  -- function evaluation
* `topo[i,j+1]`  -- indexing

2.) Simplify complex formulas by evaluating pieces separately

     numerator=(a + b)**3. - np.exp(c)  
     denom = cos(5z) - np.log(y)`  
     slope = np.arctan(umerator/denom)  

3.)  When in doubt about how row/colum relate to lat/lon on an image, draw a dot
     on your map

+++ {"slideshow": {"slide_type": "slide"}}

## Objects, instances, and types

* [A glossary](https://eli.thegreenplace.net/2012/03/30/python-objects-types-classes-and-instances-a-glossary)

* A type or class:  np.array or NoneType

* An instance or object:  np.array([5,6,7]) or None

+++ {"slideshow": {"slide_type": "slide"}}

## Untangling spaghetti code

1.) Comment your code to make your intent clear  
2.) For choosing one among many, use the `in` keyword

### Example: Find an item in a list

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
guestlist = ['tom','betty','ulma']
guest = 'ulma'
if guest in guestlist:
    print(f"Welcome {guest}!")
```

+++ {"slideshow": {"slide_type": "slide"}}

3.) Use dictionaries to hold functions and slices by keyword

+++ {"slideshow": {"slide_type": "subslide"}}

### Example:  return a slice from a dictionary

+++ {"slideshow": {"slide_type": "subslide"}}

Suppose that if our map projection is mercator, then our study region (Vancouver Island) is
located between row 10 and row 20 and column 100 and column 107 on a series of satellite images.
If our map projection is Lambert Azimuthal, then there's a different set of corners for the region.
How would we find the right slice without an if/else block?

Answer: store the slices in a dictionary and look them up by dictionary key

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# make a fake image

import numpy as np
numcols = 200
numrows = 100
fake_image = np.arange(0,numcols*numrows).reshape([numrows,numcols])
print(fake_image[0:10,0:5])
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# make a dictionary that has 'mercator' as its first key, and holds another dictionary with
# 'rows' and 'columns' keys for that map projection

row_slice = slice(10,20)  # 10:20
column_slice = slice(100,107)  # 100:107
corner_dict = dict()
corner_dict['mercator'] = {'rows': row_slice,'columns':column_slice}
## now use these slices on the fake_image

projection='mercator'
island_rows = corner_dict[projection]['rows']
island_columns = corner_dict[projection]['columns']
island_image = fake_image[island_rows,island_columns]
print(island_image)
```
