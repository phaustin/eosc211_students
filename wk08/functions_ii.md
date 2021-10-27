---
jupytext:
  formats: ipynb,md:myst
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

# Functions II

## EOSC 211

**Week 8 Day 2**

**Learning Objectives:**  
1. Implement functions in your code
2. Understand the difference between a *fruitful* function (one that returns a variable) and void functions (one that performs an action but does not return anything

+++

## Question 1

**We have two input arrays, `x` which is distance and `tpro` which is elevation in kilometers (say, along a survey line). Both have shape (100,). Use a *loop* and an *if statement* to write out a new variable `tlow` that contains only the values in `tpro` when the elevation is less than -1.8km.**

```{code-cell}
import numpy as np

x = np.linspace(0, 1000, 100)  # km along the survey line
tpro = -1.5 + 0.5 * np.sin(x) # pretend topo

# your code here
```

## Question 2

**Turn the code snippet above into a function that returns an array `tlow` that is exactly the same as Q1, but that takes as input (1) `in_data` and (2) a variable called `cutoff` that contains an arbitrary cut-off for the elevation  (ie, I might want to select elevations below -2km or -1.8 km or -1.5km, so make this a variable).**

**Finally, call your function with tpro as the input data and a cutoff of -1.8 km**

```{code-cell}
# your code here
```

## Question 3

**Modify your function to return a *tuple* containing the elevations below `cutoff`, and the *indexes* of where those elements are found; ie `(tlow, tlow_ind)`.**

```{code-cell}
# your code here
```

## Question 4

**Finally, I need not have used a loop and an “if” statement in the function.  How would I rewrite the body of the function in Exercise 2 to use logical indexing?  Note that the function call and function definition line don’t need to be changed.**

```{code-cell}
# your code here
```
