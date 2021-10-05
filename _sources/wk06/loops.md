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

# Loops

## EOSC 211

**Week 6 Day 1**

**Learning Objectives:**  
1. Use for and while loops to do useful things
2. Appreciate built in functions

**Write Python code to solve the following problems.  Do not use any built-in functions (unless explicitly allowed)**

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

## Exercise 5

**Use [pX,pY]=ginput(1) to get a point, and continue getting points until pX<0. Store the pX values in another variable SX, where SX(1) is the first point chosen, SX(2) is the second element, and SX(N) is the last element.**

```{code-cell} ipython3
## No python equivalent of ginput() without some exotic package. Revise question?
```

## Exercise 6

**A) Run the following cell. What is the output (descrive in words)**

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
