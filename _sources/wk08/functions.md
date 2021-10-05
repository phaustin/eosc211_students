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

# Functions

## EOSC 211

**Week 8 Day 1**

**Learning Objectives:**  
1. Implement functions in your code

Reading: https://phaustin.github.io/think_jupyter/functions.html

+++

## Question 1

**Write a function called `sqrtsum` that takes as input two arbitrary real numbers, `x1` and `x2` and returns two parameters: the sum of `x1` and `x2` and the square root of the sum of `x1` and `x2` (you can use ` ** 0.5` or `np.sqrt()` if you have imported the numpy package). Include a docstring that specifies what the function does, and what the input and output arguments are.**

**create the `sqrtsum` function by editing the code below:**

```{code-cell} ipython3
# Write the function definition line:
def a_function():
    # Write the docstring:
    """
    this is a docstring! tell me about your function
    """
    # Write the body of the function:
    ans = None
    # Write the return statement:
    return ans
```

```{code-cell} ipython3
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

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
mysum, rootsum = sqrtsum(255, 73.5)
print(mysum)
print(rootsum)
```

## Question 3

**Let's make our function a little more user friendly by anticipating a possible error. Modify `sqrtsum` to *raise* an exception if both of the function arguments aren't either integers or floats**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
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

## Question 4

**Now change your code in (3) to be a subfunction called `checkinput()` that does the exact same thing as in (3) and is called by your main function `sqrtsum`. `checkinput` should take all the input parameters passed to `sqrtsum`.**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
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

# its not really obvious why this is a desireable way to go about this... modify question?
```

## Question 5

**Continue writing the body of the function addn that takes three parameters n, summax and maxiter and adds n to itself while the sum is less than or equal to summax or if the number of iterations is less than or equal to maxiter and then returns the sum.**

```{code-cell} ipython3
def sum_n(n, summax, maxiter):
    """
    adds the n to itself until one of the
    two conditions is reached:
    1. Either sumn reaches summax, or
    2. maxiter iterations is reached
    """
    counter = 0
    sumn = n
    while sumn <= (summax):
        pass # your code here
```

```{code-cell} ipython3
def sum_n(n, summax, maxiter):
    """
    adds the n to itself until one of the
    two conditions is reached:
    1. Either sumn reaches summax, or
    2. maxiter iterations is reached
    """
    counter = 0
    sumn = n
    while sumn <= (summax) and counter <= maxiter:
        sumn += n
        counter += 1
    return sumn
```

## Question 6

**Why doesn't this work? Debug this code**

```{code-cell} ipython3
my_num = 5.1
y = cube_plus_one(my_num)


def cube_plus_one(x):
    """
    returns the cube of the input plus one
    """
    return x ** 3 + 1
```

```{code-cell} ipython3
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
