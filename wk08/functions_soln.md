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

# Functions -- solution

## EOSC 211

**Week 8**

**Learning Objectives:**  
1. Implement functions in your code
2. Understand argument passing

+++

## Question 1

**Write a function called `sqrtsum` that takes as input two arbitrary real numbers, `x1` and `x2` and returns two parameters: the sum of `x1` and `x2` and the square root of the sum of `x1` and `x2` (you can use ` ** 0.5` or `np.sqrt()` if you have imported the numpy package). Include a docstring that specifies what the function does, and what the input and output arguments are.**

**create the `sqrtsum` function by editing the code below:**

```{code-cell}
# Write the function definition line:
def a_function():
    # Write the docstring:
    
    
    
    # Write the body of the function:
    
    
    
    # Write the return statement:
    
```

```{code-cell}
# andrew's soln
def sqrtsum(x1, x2):
    """
    takes in two real numbers and returns a tuple y1, y2 with y1=x1+x2 and y2=(y1)^1/2
    """
    y1 = x1 + x2
    y2 = y1 ** 0.5
    return y1, y2
```

## Question 2

**In the cell below, *call* your `sqrtsum` function if you want to find the “sqrtsum” of 255 and 73.5. Assign variables `mysum` and `rootsum` to the outputs `sqrtsum`**

```{code-cell}
# your code here
```

```{code-cell}
# andrew's soln
mysum, rootsum = sqrtsum(255, 73.5)
print(mysum)
print(rootsum)
```

## Question 3

**Let's make our function a little more user friendly by anticipating a possible error. Modify `sqrtsum` to *raise* an exception if both of the function arguments aren't either integers or floats**

```{code-cell}
# your code here
```

```{code-cell}
# andrew's soln
def sqrtsum(x1, x2):
    """
    takes in two real numbers and returns a tuple y1, y2 with y1=x1+x2 and y2=(y1)^1/2
    """
    # check the inputs
    for x in x1, x2:
        if type(x) is not int and type(x) is not float:
            raise TypeError("make sure x1 and x2 are numeric values")

    # return values if inputs are correct
    y1 = x1 + x2
    y2 = y1 ** 0.5
    return y1, y2
```

```{code-cell}
# catherine's solution
import numpy as np

def sqrtsum(x1, x2):
    """
    takes in two real numbers and returns a tuple y1, y2 with y1=x1+x2 and y2=(y1)^1/2
    """
    
    # check the inputs
    for x in x1, x2:
        if not isinstance(x, int) and not isinstance(x,float):    # I googled to find isinstance
            raise TypeError("make sure x1 and x2 are numeric values")

    # return values if inputs are correct
    y1 = x1 + x2
    y2 = y1 ** 0.5
    return y1, y2  

# testing
a1=2.
a2=3

a_sum,a_sqrtsum = sqrtsum(a1,a2)
print(a1,a2,a_sum,a_sqrtsum)
```

## Question 4

**Now change your code in (3) to be a function called `checkinput()` that does the exact same thing as in (3) and is called by your main function `sqrtsum`. `checkinput` should take all the input parameters passed to `sqrtsum`.  `checkinput` is what is called a nested or inner function.**

```{code-cell}
# your code here
```

```{code-cell}
# andrew's soln
def sqrtsum(x1, x2):
    """
    takes in two real numbers and returns a tuple y1, y2 with y1=x1+x2 and y2=(y1)^1/2
    """
    def check_input(x1, x2):
    for x in x1, x2:
        if not isinstance(x, int) and not isinstance(x,float):    # I googled to find isinstance
            raise TypeError("make sure x1 and x2 are numeric values")
    
    # check the inputs
    check_input(x1, x2)
    
    # return values if inputs are correct
    y1 = x1 + x2
    y2 = y1 ** 0.5
    return y1, y2
```

```{code-cell}
# catherine's solution
# discuss scope here
#
# More on inner/nested functions:  
#     See section on Creating Inner Functions - second part of page is more advanced than we will cover in 211
# https://realpython.com/inner-functions-what-are-they-good-for/

def sqrtsum(x1, x2):
    """
    takes in two real numbers and returns a tuple y1, y2 with y1=x1+x2 and y2=(y1)^1/2
    """
    def check_input(x1, x2):
        for x in x1, x2:
            if type(x) is not int and type(x) is not float:
                raise TypeError("make sure x1 and x2 are numeric values")
    
    # check the inputs
    check_input(x1, x2)
    
    # return values if inputs are correct
    y1 = x1 + x2
    y2 = y1 ** 0.5
    return y1, y2
```

## Question 5

**Continue writing the body of the function addn that takes three parameters n, summax and maxiter and adds n to itself while the sum is less than or equal to summax or if the number of iterations is less than or equal to maxiter, and then returns the sum.**

```{code-cell}
def sum_n(n, summax, maxiter):
    """
    adds n to itself until one of the
    two conditions is reached:
    1. Either sumn exceeds summax, or
    2. maxiter iterations is exceeded.
    """
    counter = 0
    sumn = n
    while <your code here>:
        pass # your code here
```

```{code-cell}
# Andrew's and Catherine's solutions the same

def sum_n(n, summax, maxiter):
    """
    adds n to itself until one of the
    two conditions is reached:
    1. Either sumn exceeds summax, or
    2. maxiter iterations is exceeded.
    """
    counter = 0
    sumn = n
    while sumn <= (summax) and counter <= maxiter:
        sumn += n
        counter += 1
    return sumn
```

```{code-cell}
# Some extra things to discuss:  Catherine

import numpy as np    # I always add

def sum_n(n, summax, maxiter):
    """
    adds n to itself until one of the
    two conditions is reached:
    1. Either sumn exceeds summax, or
    2. maxiter iterations is exceeded.
    """
    counter = 0
    sumn = n
    while sumn <= (summax) and counter <= maxiter:
        sumn += n
        counter += 1
    return sumn

# 1.  Calling the function in the main script
a1=2
niter=150
maxsum=101

# calling the function
mysum=sum_n(a1,maxsum,niter)
print(a1,mysum)

# 2. if i modify n inside function, is a1 modified?
    # add these 3 lines to start of function code
    # print(f'n1 before modification={n}')
    # n=1
    # print(f'n1 after modification={n}')
    
# things to think about on your own:  
# tricky: how would i modify the function to return the last value of sumn that was <= summax?  
```

## Question 6

**Why doesn't this work? Debug this code**

```{code-cell}
my_num = 5.1
y = cube_plus_one(my_num)


def cube_plus_one(x):
    """
    returns the cube of the input plus one
    """
    return x ** 3 + 1
```

```{code-cell}
# andrew's soln
my_num = 5.1


def cube_plus_one(x):
    """
    returns the cube of the input plus one
    """
    return x ** 3 + 1


# we need to define the function BEFORE calling it
y = cube_plus_one(my_num)
```
