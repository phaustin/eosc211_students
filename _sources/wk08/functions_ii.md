---
jupytext:
  formats: ipynb,md:myst
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

# Functions II

## EOSC 211

**Week 8 Day 2**

**Learning Objectives:**  
1. Implement functions in your code
2. Understand the difference between a *fruitful* function (one that returns a variable) and void functions (one that performs an action but does not return anything

+++

## Question 1

**We have two input arrays, `x` which is distance and `tpro` which is elevation in kilometers (say, along a survey line). Both have shape (99,). Use a *loop* and an *if statement* to write out a new variable `tlow` that contains only the values in `tpro` when the elevation is less than -1.8km.**

```{code-cell} ipython3
import numpy as np

x = np.linspace(0, 1000, 100)  # km along the survey line
tpro = 2 * np.sin(x)  # get some real topographical data here instead?

# your code here
```

```{code-cell} ipython3
# andrew's soln
tlow = np.array([])
for i in tpro:
    if i < 0.5:
        tlow = np.append(tlow,i)

print(tlow)
```

## Question 2

**Turn the code snippet above into a function that returns an array `tlow` that is exactly the same as Q1, but that takes as input (1) `tproin` and (2) a variable called `cutoff` that contains an arbitrary cut-off for the elevation  (ie, I might want to select elevations below -2km or -1.8 km or -1.5km, so make this a variable).**

**Finally, call your function with tpro as the input data and a cutoff of 1.8km**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
def select_elev(in_data, cutoff):
    """
    selects elements of a 1D np array in_data which are below the value cutoff.
    returns elements of in_data which are below cutoff
    """
    tlow = np.array([])
    for i in tpro:
        if i < cutoff:
            tlow = np.append(tlow, i)
    return tlow

select_elev(tpro, -1.8)
```

## Question 3

**Modify your function to return a *tuple* containing the elevations below `cutoff`, and the *indexes* of where those elements are found; ie `(tlow, tlow_ind)`.**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
def select_elev2(in_data, cutoff):
    """
    selects elements of a 1D np array in_data which are below the value cutoff.
    returns elements of in_data which are below cutoff
    """
    tlow = np.array([])
    tlow_ind = np.array([])
    for i in range(len(in_data)):
        if in_data[i] < cutoff: 
            tlow_ind = np.append(tlow_ind, i)
            tlow = np.append(tlow, in_data[i])
    return tlow, tlow_ind

low, ind = select_elev2(tpro, -1.5)
low, ind
```

## Question 4

**Finally, I need not have used a loop and an “if” statement in the function.  How would I rewrite the body of the function in Exercise 2 to use logical indexing?  Note that the function call and function definition line don’t need to be changed.**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
def select_elev3(in_data, cutoff):
    """
    selects elements of a 1D np array in_data which are below the value cutoff.
    returns elements of in_data which are below cutoff
    """
    return in_data[in_data < cutoff]
    
select_elev3(tpro, -1.8)
```

```{code-cell} ipython3

```
