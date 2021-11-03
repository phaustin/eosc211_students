---
jupytext:
  cell_metadata_filter: all
  formats: ipynb,md:myst
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
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

# solution: More Functions & Debugging Practice


## EOSC 211

**Week 9 Day 1**

**Learning Objectives:**  
1.  Practice with function default arguments, keyword arguments
2.  Debugging - more practice with functions, for loops, indexing

+++

## Question 1

**Functions with default arguments**

How would I complete the following function code such that the following lines of code 

``` 
    print(f'The surface gravity is {surfgrav("Venus")} m/s^2')
    
    print(f'The surface gravity is {surfgrav()} m/s^2')
```

would print to the screen the surface gravity of Venus followed by the surface gravity of Earth.

```{code-cell} ipython3
:trusted: true

def surfgrav(planet):
    """ computes and returns surface gravity on my favorite inner solar system body
        INPUT:  planet/moon choice, default is Earth
        OUTPUT:  surface gravity in m/s^2
    """
    G = 6.67e-11   # gravitational constant [units]
    
    mass = {"Earth": 5.972e24, "Venus": 4.867e24, "Mercury": 3.301e23, "Moon": 7.348e22, "Mars": 3.390e03}
    radius = {"Earth": 6.371e06, "Venus": 6.0518e06, "Mercury": 2.440e06, "Moon": 1737e06}
    
    gsurf = G*mass[planet]/radius[planet]**2
```

```{code-cell} ipython3
:trusted: true

#  Solution
def surfgrav(planet="Earth"):    # needs default argument
    """ computes and returns surface gravity on my favorite inner solar system body
        INPUT:  planet/moon choice, default is Earth
        OUTPUT:  surface gravity in m/s^2
    """
    G = 6.67e-11   # gravitational constant [units]
    
    mass = {"Earth": 5.972e24, "Venus": 4.867e24, "Mercury": 3.301e23, "Moon": 7.348e22, "Mars": 6.417e23}
    radius = {"Earth": 6.371e06, "Venus": 6.0518e06, "Mercury": 2.440e06, "Moon": 1.737e06, "Mars": 3.390e06}
    
    gsurf = G*mass[planet]/radius[planet]**2
    
    return gsurf  # needs a return statement

print(surfgrav("Venus"))
print(surfgrav("Mercury"))
print(surfgrav("Moon"))
print(surfgrav("Mars"))
print(surfgrav())
```

## Question 2

### 2.a
What would be the output of the following code:

```{code-cell} ipython3
:trusted: true

# Francis question: 
import numpy as np


def radius_squared(x, y=2):
    print(x, y)
    r2 = x**2 + y**2
    print(r2)
        
        
radius_squared(2, 3)
radius_squared(2)
radius_squared(y=1, x = 3 )
radius_squared(y=3, 2)
```

___
*Solution:*

```
> 2 3
  13
> 2 2
  8
> 3 1
  10
> SyntaxError: positional argument follows keyword argument
----------------------------------------
```

+++

### 2.b


Which line number(s) of code will not work and why?

```{code-cell} ipython3
:trusted: true

def equilibrium_temp(F_sun=1366, distance=1, albedo=0.3):
    """
    prints the blackbody equilibrium temperature of a
    perfectly emitting planetary body (default values 
    for Earth-Sun) given inputs:
        - F_sun: solar flux from the star [Jm-2s-1].
        - distance: distance from the star [AU].
        - albedo: planetary albedo.
    """

    sigma = 5.57e-8  # stefan-boltzmann constant [Wm-2deg-4]
    # blackbody equilibrium temp:
    T_e = (F_sun * (1 - albedo) / (distance ** 2 * 4 * sigma)) ** (
        1 / 4
    )  
    print(f"Equilibrium temperature is {T_e:.2f} K")


equilibrium_temp()                                      # Line 1
equilibrium_temp(F_sun=1366, albedo=0.6, distance=1.2)  # Line 2
equilibrium_temp(F=1366, A=0.2, D=0.6)                  # Line 3
equilibrium_temp(albedo=0.2, distance=1.1);             # Line 4
equilibrium_temp(albedo=0.2, distance=0.6, 1366)        # Line 5
```

___
*Solution:*
1. Line 3: TypeError: equilibrium_temp() got an unexpected keyword argument 'F'
2. Line 5: SyntaxError: positional argument follows keyword argument

+++

## Question 3

**Decide what the code fragment is trying to do, and how to fix the error so it performs the required task.**

```{code-cell} ipython3
:trusted: true

import numpy as np
A = np.random.rand(10,5) # creates a 10x5 matrix containing random numbers

# debug this code

def rowsum():
    rowsum = 0
    for k in range(len(A)):
        rowsum = rowsum + A[:,k]
        
rowsum(A)
```

```{code-cell} ipython3
:trusted: true

# solution - same for Catherine and Andrew
import numpy as np
A = np.random.rand(10,5) # creates a 10x5 matrix containing random numbers

def rowsum(arr):                    # need to pass in `arr` as input
                                    # need doc string - not reqd for a debugging question
    """ takes in 2D array and sums the elements in each column        
        INPUT:  arr - numpy array of floats or ints:  shape is (N,M)         
        OUTPUT:  rowsum - numpy 1D array of floats or ints; shape is (N,)
    """
    rowsum = np.zeros(len(arr[0,:]))    # make 1D array; initialize sums to 0 to begin
    for k in range(len(arr[0,:])):      # need just len of second dimension of A
        rowsum[k] = np.sum(arr[:,k])    # previous version doesn't sum elements in a col
    return rowsum                       # need a return statement
        
rowsumA = rowsum(A)
print(rowsumA)
```

## Question 4

**This code is supposed to create a *running standard deviation*. Does it? If it doesn't, state why. If not, what is the problem?**

```{code-cell} ipython3
:trusted: true

x = np.random.rand(10)
y = np.empty_like(x)
# debug this code
for k in range(len(x)):
    y[k] = np.std(x[min(0, k - 3) : max(len(x), k + 3)])
```

**A) What do you think this code is trying to do (be specific). Write down the steps in words**

+++

your answer here

+++

**B) Fix the code to perform the intended operation**

```{code-cell} ipython3
:trusted: true

# your code here
```

```{code-cell} ipython3
:trusted: true

# Solution 
#
# this is supposed to call the function np.std (calculate the standard deviation) for x[k-3:k+3],
# i.e. the running standard deviation. The min and max function calls handle the cases at the beginning and 
# end of the array where k-3 is a negative number (which refers to indexes from the end of the array). 
# the error is that the min and max functions are switched! It should call the GREATER of (0,k-3) and the
# LESSER of (len(x),k+3)
#
x = np.random.rand(10)
y = np.empty_like(x)

for k in range(len(x)):
    y[k] = np.std(x[max(0, k - 3) : min(len(x), k + 3)])
y
```

## Question 5

**Below is a list of common types of errors. Define them in your own words**

+++

**A) Off-by-one error**:

+++

**B) Fencepost error:**

+++

## Question 6

**What do you see on the screen when you run this code (after fixing the error)?**

```{code-cell} ipython3
:trusted: true

x = 5
y = 3
for j in np.arange(0,5):
    y = y-1
    if j = 4:
        x +=4
```

```{code-cell} ipython3
:trusted: true

# your code here
```

```{code-cell} ipython3
:trusted: true

# Solution
x = 5
y = 4
for j in np.arange(0,5):
    y = y-1
    if j == 4:
        x +=4
        
x, y
```
