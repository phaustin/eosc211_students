---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Loops II

## EOSC 211

**Week 6 Day 2**

**Learning Objectives:**  
1. More practice with loops
2. Write elegant, efficient code

**Write Python code to solve the following problems.**

+++

## Question 1

**Display the numbers of the series 2 4 6 8 10 12 …100 to the screen one by one.**

```{code-cell} ipython3
# your code here
```

## Question 2

You are given the matrix $A$ which is size 10x20. The following code loops through each element $A_{ij}$ and calculates $i \cdot j \cdot A_{ij}$. Modify this code to store successive calculations in successive elements of a new variable `B` which will have shape 1x200.

```{code-cell} ipython3
# modify this code
A = np.ones([10,20])

for i in np.arange(0,10):
    for j in np.arange(0,20):
        k = i * j * A[i,j]        
```

```{code-cell} ipython3
# your modified version here
```

## Question 3

**Given a variable `x = [1, 12, 53, 34, 61, 16, 17, 38, 20]`,  generate a new variable `y` whose elements are**

**a.	2 times the value of the corresponding element in `x` if the latter is even**

**b.	3 times the value of the corresponding element in `x` if the latter is odd**

```{code-cell} ipython3
# your code here
```

## Question 4 

**Given a user’s input of some integer num, calculate the factorial of the input. Definition: n! = n(n-1)(n-2)...(3)(2)(1)**

```{code-cell} ipython3
# assigns user input to a variable `num`
num = int(input('Enter an integer: '))
# add your code here
```

## Question 5

Modify the above factorial calculation to return an error message if num is negative or is not an integer. 
To exit and raise an error, include `raise Exception('Error message here')`, or  `raise TypeError('Error message here')`

```{code-cell} ipython3
# your code here
```
