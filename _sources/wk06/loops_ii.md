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

```{code-cell} ipython3
# andrew's soln
import numpy as np
for num in np.arange(2,101,2):
    print(num)
```

## Question 2

You are given the matrix $A$ which is size 10x20. The following code loops through each element $A_{ij}$ and calculates $i \cdot j \cdot A_{ij}$. Modify this code to store successive calculations in successive elements of a new variable `B` which will be size 1x200.

```{code-cell} ipython3
# modify this code
A = np.ones([10,20])

for i in np.arange(0,10):
    for j in np.arange(0,20):
        k = i * j * A[i,j]        
```

```{code-cell} ipython3
# andrew's soln
B = np.empty(200)
k = 0 # create an index variable to loop over the elements of B
for i in np.arange(0,10):
    for j in np.arange(0,20):
        B[k] = i * j * A[i,j]
        k += 1
print(B) # this question gets modified by pythons counting from 0 convention instead of matlab from 1       
```

## Question 3

**Given a variable `x = [1, 12, 53, 34, 61, 16, 17, 38, 20]`,  generate a new variable `y` whose elements are**

**a.	2 times the value of the corresponding element in `x` if the latter is even**

**b.	3 times the value of the corresponding element in `x` if the latter is odd**

```{code-cell} ipython3
x = [1, 12, 53, 34, 61, 16, 17, 38, 20]
y = np.empty_like(x)
for i in range(len(x)):
    if x[i] % 2 == 0: # check if x[i] is even
        y[i] = 2 * x[i]
    else:
        y[i] = 3 * x[i]
print(y)
```

## Question 4 

**Given a user’s input of some integer num, calculate the factorial of the input. Definition: n! = n(n-1)(n-2)...(3)(2)(1)**

```{code-cell} ipython3
# assigns user input to a variable `num`
num = int(input('Enter an integer: '))
# add your code here
```

```{code-cell} ipython3
# assigns user input to a variable `num`
num = int(input('Enter an integer: '))
# andrew's soln
fac = 1
for n in range(num):
    #print(n+1)
    fac *= (n + 1) # rememver pythons counting convention, add 1 to n to 
print(fac)
```

## Question 5

Modify the above factorial calculation to return an error message if num is negative or is not an integer. 
To exit and raise an error, include `raise Exception('Error message here')`, or  `raise TypeError('Error message here')`

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
num = int(input('Enter an integer: '))
print(type(num))

# my original solution already does this, if the input can't be 
# cast from str to int then it raises a ValueError
```

```{code-cell} ipython3

```
