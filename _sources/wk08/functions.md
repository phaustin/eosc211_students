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

# Functions

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

## Question 2

**In the cell below, *call* your `sqrtsum` function if you want to find the “sqrtsum” of 255 and 73.5. Assign variables `mysum` and `rootsum` to the outputs `sqrtsum`**

```{code-cell}
# your code here
```

## Question 3

**Let's make our function a little more user friendly by anticipating a possible error. Modify `sqrtsum` to *raise* an exception if both of the function arguments aren't either integers or floats**

```{code-cell}
# your code here
```

## Question 4

**Now change your code in (3) to be a function called `checkinput()` that does the exact same thing as in (3) and is called by your main function `sqrtsum`. `checkinput` should take all the input parameters passed to `sqrtsum`.  `checkinput` is what is called a nested or inner function.**

```{code-cell}
# your code here
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
