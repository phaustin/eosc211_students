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

# Loops II solution

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
import numpy as np
# your code here
```

```python
# andrew's soln
for num in np.arange(2,101,2):
    print(num)
```

+++

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
# andrew's soln
B = np.empty(200)
k = 0 # create an index variable to loop over the elements of B
for i in np.arange(0,10):
    for j in np.arange(0,20):
        B[k] = i * j * A[i,j]
        k += 1
print(B) # instructor note: this question modified for python counting from 0 convention instead of matlab from 1       
```

```{code-cell} ipython3
# catherine's solution
import numpy as np

nrows = 10     # extra code lines here to define dimensions: avoids potential typos later and makes syntax clear
mcols = 20
A = np.ones((nrows,mcols))
B = np.empty(nrows*mcols)

for i in np.arange(0,nrows):    # i will be 1st index into A
    for j in np.arange(0,mcols):  # j will be 2nd index into A      
        B[i*mcols+j] = i * j * A[i,j]    # check for yourself that i*mcols+j is same as k in solution above

print(B)
```

## Question 3

**Given a variable `x = [1, 12, 53, 34, 61, 16, 17, 38, 20]`,  generate a new variable `y` whose elements are**

**a.	2 times the value of the corresponding element in `x` if the latter is even**

**b.	3 times the value of the corresponding element in `x` if the latter is odd**

```{code-cell} ipython3
# andrew's solution
x = [1, 12, 53, 34, 61, 16, 17, 38, 20]
y = np.empty_like(x)
for i in range(len(x)):
    if x[i] % 2 == 0: # check if x[i] is even
        y[i] = 2 * x[i]
    else:
        y[i] = 3 * x[i]
print(y)
```

```{code-cell} ipython3
# catherine's solution
x = [1, 12, 53, 34, 61, 16, 17, 38, 20]
y = np.empty(np.shape(x))     # see comment at end in print statement

for k in range(len(x)):
    if x[k]%2 == 0:
        y[k] = 2 * x[k]
    else:
        y[k] = 3 * x[k] 
        
message=f"""
   y contains {y}
   
   Note that here y has type float and in previous 
   solution using np.empty_like had type int (same as x)
   We saw this also in a question on the previous worksheet
   Depending on your problem you may or may not want to preserve type
   e.g. think about what happens if I wanted half the value of 
   the element of x when the latter is odd
   """

print(message)
```

## Question 4 

**Given a user’s input of some integer num, calculate the factorial of the input. Definition: n! = n(n-1)(n-2)...(3)(2)(1)**

+++

```python
# assigns user input to a variable `num`
num = int(input('Enter an integer: '))
# add your code here
```

+++

``` python
# assigns user input to a variable `num`
num = int(input('Enter an integer: '))  
# andrew's soln
fac = 1  
for n in range(num):  
    #print(n+1)  
    fac *= (n + 1) # remember pythons counting convention, add 1 to n to 
print(fac)
```

+++

``` python
# catherine's solution
num = int(input('Enter your favorite positive integer'))

my_fac = 1
for n in range(num,1,-1):   # goes from n down to 2 inclusive, multiplying by 1 does nothing
    my_fac = my_fac*n
    
print(my_fac)
```

+++

## Question 5

Modify the above factorial calculation to return an error message if num is negative or is not an integer. 
To exit and raise an error, include `raise Exception('Error message here')`, or  `raise TypeError('Error message here')`

```{code-cell} ipython3
# your code here
```

```python
# andrew's soln
num = int(input('Enter an integer: '))
print(type(num))

# my original solution already does this, if the input can't be 
# cast from str to int then it raises a ValueError
```

+++

```python
# catherine's solution

# casting into 'int' on input deals with cases that are not an integer
# however non-postive integers will still allow code to be run, but the print statement will return 1 
# as the loop condition is never met so my_fac contains its initialized value

# fixing this
num = int(input('Enter your favorite positive integer'))
if (num <= 0):
    raise TypeError('must enter positive integer')

my_fac = 1
for n in range(num,1,-1):   # goes from n down to 2 inclusive, multiplying by 1 does nothing
    my_fac = my_fac*n
    
print(my_fac)
```
