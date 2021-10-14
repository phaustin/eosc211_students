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

**Write Python code to solve the following problems.  Do not use any built-in functions (unless explicitly allowed).  It is really good practice to 'map out' your algorithm on paper/in your note-taking app first.  In other words, write what we call 'pseudo-code' or a flow chart.  This will almost always save you a LOT of time debugging later.**

+++

## Question 1

**Use a loop to multiply together all the values in a numpy array `x`, which has n points. The final product goes into a variable `total`.**

```{code-cell}
# your code here
```

## Question 2

**Use a loop to find the maximum (largest) value in `x`, writing the result into a variable `largest`.**

```{code-cell}
# your code here
```

## Question 3

**Use a loop to count the number of values in a list `x` that appear before a 5. (i.e. if `x = [1, 12, 2.5, 5, 8, 4, 5]` we want  an answer of 3). Put this number into another variable `get_five`.**

```{code-cell}
# your code here
```

## Question 4

**Consider an MxN array `A`.  Use a double loop to form a new 1xN array `rowsum`, the k$^{th}$ element of which contains the sum of elements in the k$^{th}$ column of `A`. You may use the built in functions `range()` and `len()`.**

```{code-cell}
# your code here
```

## Exercise 5

**A) Run the following cell. What is the output (describe in words)**

```{code-cell}
import numpy as np
x = np.array([0, 1])
for k in np.arange(2,20):
    x = np.append(x, x[k-1] + x[k-2])
```

your answer here

+++

**B) How many arrays have been created by the time the loop finishes? Is this code *efficient?* Why or why not?**

+++

your answer here
