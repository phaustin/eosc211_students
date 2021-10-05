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

# More Complicated Logic

## EOSC 211

**Week 5**

**Learning Objectives:**  
1. Practice interpreting logical flow control 
2. Comment code to make it easier for humans to interpret

+++

## Question 1

**What is the value of `z` after you execute this script? Remember that `A % b` returns the remainder of the floor division operation `A // b`. Add comments to explain what is happening at each step.**

```{code-cell} ipython3
x=4
y=3

if x % 2 == 0:
    if x * y > 15:
        z = 1
    elif x * y > 10:
        z = 2
    elif x * y == 12:
        z = 3
else:
    z=0
```

## Question 2

**What is the value of z after you execute this script? Add comments to the code**

```{code-cell} ipython3
x = 4
y = 3

if x % 2 != 0:
    if x * y == 12:
        z = 3
else:
    z = 0
```

```{raw-cell}
# your answer here
```

## Question 3

**What is the value of z after executing this script? Add comments to the code**

```{code-cell} ipython3
x = -2
y = 3

if -4 < x < -1:
    z = x ** 2 / 2
elif -4 < x and x < -1:
    z = -x * y ** 2
    if z > 18:
        z = 0 * z
```

```{raw-cell}
# your answer here
```

**What is `z` after executing this script? What does this script do (in in 4 or 5 words)?**

```{code-cell} ipython3
x = [5, 3, 1, 2]
z = x[0] 

if  x[1] < x[0]:
    z = x[1]

if x[2] < z:
    z = x[2]
    
if x[3] < z:
    z = x[3]
```

```{raw-cell}
# your answer here
```
