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

# Loops solution

## EOSC 211

**Week 6 Day 1**

**Learning Objectives:**  
1. Use for and while loops to do useful things
2. Appreciate built in functions

**Write Python code to solve the following problems.  Do not use any built-in functions (unless explicitly allowed).  It is really good practice to 'map out' your algorithm on paper/in your note-taking app first.  In other words, write what we call 'pseudo-code' or a flow chart.  This will almost always save you a LOT of time debugging later.**

+++

## Question 1

**Use a loop to multiply together all the values in a numpy array `x`, which has n points. The final product goes into a variable `total`.**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
import numpy as np

x = np.array([1,18,5,6]) # sample array for testing my code

total = 1
for num in x:
    total *= num
    
print(total)
```

## Question 2

**Use a loop to find the maximum (largest) value in `x`, writing the result into a variable `largest`.**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
largest = None
for num in x:
    if largest == None:
        largest = num
    else:
        if num > largest:
            largest = num
print(largest)
```

```{code-cell} ipython3
# catherine's solution:  I wanted to use numpy arrays not lists and replacing None by np.nan doesn't work

import numpy as np

x = np.arange(0,5*np.pi,np.pi)

largest=-9999    # choose something you know is much less than any number in your array
for num in x:
    if num > largest:
        largest = num
            
print(largest)
```

```{code-cell} ipython3
# catherine's second solution
# this one because you might not always know what is likely to be the min number in your numpy array

import numpy as np
import sys

x = np.arange(0,100,10)

largest=float("-inf")    # most negative float allowed: my x values all have to be larger than this.
print(f'largest before going into the loop is {largest}')

for num in x:
    if num > largest:
        largest = num
            
print(f'largest value in x is {largest}')
```

## Question 3

**Use a loop to count the number of values in a list `x` that appear before a 5. (i.e. if `x = [1, 12, 2.5, 5, 8, 4, 5]` we want  an answer of 3). Put this number into another variable `get_five`.**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
x = [1, 12, 2.5, 5, 8, 4, 5]

get_five = 0
while x[get_five] != 5:
    get_five += 1

print(get_five)
```

## Question 4

**Consider an MxN array `A`.  Use a double loop to form a new 1xN array `rowsum`, the k$^{th}$ element of which contains the sum of elements in the k$^{th}$ column of `A`. You may use the built in functions `range()` and `len()`.**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
A = np.array([[2,2,3],
              [4,2,6]]) # test array

rowsum = np.empty_like(A[0,:]) # initialize rowsum with the same number of columns as A
for j in range(len(A[0,:])): # loop over columns
    k = 0
    for i in range(len(A[:,0])): # loop over rows
        k += A[i,j] 
    rowsum[j] = k # assign k to rowsum
        
print(rowsum)
```

```{code-cell} ipython3
# catherine's solution
import numpy as np

A = np.array([[2,2,3],
              [4,2,6]]) # test array

# If allowed, I would have used shape to get # rows and cols
[mrows,ncols] = A.shape   # or [M,N] = shape(A) <-- use shape function with A as input or shape attribute of object A
                          # mrows is same as len(A[:,0]), and ncols is same as len(A[0,:])

rowsum = np.zeros(ncols)    # initialize rowsum to be a 1D array with N elements, all set to zero
for j in range(ncols):
    for i in range(mrows):
        rowsum[j] += A[i,j]

print(f'rowsum contains {rowsum} and has dimensions {rowsum.shape}')
print(f'\nCan you see a subtle difference between the two solutions? See also loops_ii qn 3')
```

## Exercise 5

**A) Run the following cell. What is the output (describe in words)**

```{code-cell} ipython3
x = np.array([0, 1])
for k in np.arange(2,20):
    x = np.append(x, x[k-1] + x[k-2])
```

your answer here

+++

**B) How many arrays have been created by the time the loop finishes? Is this code *efficient?* Why or why not?**

+++

your answer here
