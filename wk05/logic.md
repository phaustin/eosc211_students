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

# Logic

## EOSC 211

**Week 5**

**Learning Objectives:**  

1. Use `if`, `elif`, `else` statements to write *non-linear code* (see this week's [reading](https://phaustin.github.io/Problem-Solving-with-Python/If-Else-Try-Except/Selection-Statements.html))
2. Apply logical flow control to an earth science problem


+++

## Question 1

**Assume you have two variables `X` and `Y`, which each hold a single number. Assign the smallest of the two numbers to the variable `sml` using `if` and `else`.**

```{code-cell} ipython3
# your code here
```

## Question 2
**Modify your code, so that `sml` contains `None` if the values `x` and `y` are the same. Print the values in `x`, `y`, `sml` and the type of the variable `sml`**

```{code-cell} ipython3
# your code here
```

## Question 3
**Modify your code in question 2, so that `sml` contains `NaN` if the values `x` and `y` are the same.**

```{code-cell} ipython3
# your code here
```

## Question 4

**Modify your code to put the smallest of the numbers in a 3-element list `X=[a, b, c]` into the variable SML.**

```{code-cell} ipython3
# your code here
```

## Question 5

**Modify your code in question 4 so that X is now a 1d vector.**

```{code-cell} ipython3
# your code here
```

## Question 6

**Longitudes “wrap around” the earth, so that any longitude may be given as a positive value between 0 and 360 degrees (going eastward), or a negative value between 0 and -360 degrees (going westward). The location of the “0” degree line is the same in both cases. But this means that a longitude of 355 and a longitude of -5 refer to the same place!
Given two arbitrary values LON1 and LON2 in the range -360 to +360, write a selection that decides whether these two values refer to the same point. Create a variable same that has a value of `True` if they refer to the same point and a value `False` if they refer to different points.**

**Does it work? - Test your code with pairs of numbers like (5,5), (5,-355), (5,355),(-5,355),(0,0),(360,360),(0,360), etc**

```{code-cell} ipython3
# your code here
```


```{code-cell} ipython3
# andrew's soln
lon1 = 355 # try messing with these values
lon2 = -5

lons = (lon1, lon2)

# use the sml function from q3
sml = min(lons)
big = max(lons)

if big - sml == 360:
    same = True
# catch the case where lon1 = lon2
elif big - sml == 0:
    same = True
else:
    same = False
    
print(same)
```
