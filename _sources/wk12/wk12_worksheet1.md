---
jupytext:
  formats: ipynb,md:myst
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
orig_nbformat: 4
---

# Week 12 Review Exercises

## EOSC 211

**Week 11 Day 1**

**Learning Objectives:**  
1. Solve problems with python code
2. Choose appropriate data structures to make your code neat and efficient

+++

## Question 1

**A) You have a cash register with \$20, \$10, \$5, \$2, \$1, \$0.25, \$0.10, \$0.05 bills or coins. Write code to make change usin the largest denominations possible – so that, for example, if someone gives you a \$10 bill for something costing \$6.55 the program will calculate that you get back \$3.45 in change consisting of a \$2, and \$1, a \$0.25, and 2 \$0.10**  

**The floor division `//` and modulo `%` operators are of use.**

**Store the denominations available in a dictionary `money={'twenties', 'tens', 'fives', 'toonies'...}`. The rest of the program is up to you.  There are many correct ways to solve this problem**

```{code-cell} ipython3
item_cost = 6.55  # dollars
cash_in = 10  # dollars
```

```{code-cell} ipython3
# your code here
```

**B) Turn this into a function called `getchange` that will take as input `item_cost`, `cash_in` and return `change`. Also, make your funtion raise an error if the customer does not give enough money to cover the cost of the purchase**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# testing my function

mychange = getchange(item_cost, cash_in)
mychange
```

**C) Edit get change to also take as input a dictionary `available_change` that contains the number of each denomination available in the cash register.  Use this to check that there are enough of each denomination to cover the change.  If any denomination is short make up the change with the next available largest bill.** 

e.g. in the above example \$3.45 is required in change, so ideally the \$3 part of the change would comprise 1 toonie and 1 loonie.  If no toonies are available then the \$3 would comprise 3 loonies, if only 2 loonies were available it would comprise 2 looonies and 4 quarters etc.

```{code-cell} ipython3
# testing my function
import numpy as np

whats_there = {
        "twenties": 10,
        "tens": 10,
        "fives": 10,
        "toonies": 0,
        "loonies": 0,
        "quarters": 0,
        "dimes": 0,
        "nickels": 10,
    } 

mychange = getchange(item_cost, cash_in, whats_there)
mychange
```

## Question 2:  Practice with indexing / code tracing

**A) For  `x1=[1, 7, -8, 2, -3, -9]`, what is contained in `y2` in each case after the code runs?  Do these three snippets of code do the same thing?  Show your work.**

+++

```python
#  Code Version A
import numpy as np
x1 = np.array([1, 7, -8, 2, -3, -9])
y2 = []
for i in range(len(x1)):
    if x1[i] < 0:
        y2.append(x1[i])
print(y2)
```

+++

```python
# Code Version B
del y2           # remove any previous version of y2 from memory
x1 = np.array([1, 7, -8, 2, -3, -9])
y2 = np.zeros_like(x1)
k = 0
for i in range(len(x1)):
    if x1[i] < 0:
        k = k + 1
        y2[k] = x1[i]
print(y2)
```

+++

```python
# Code Version C
del y2           # remove any previous version of y2 from memory
x1 = np.array([1, 7, -8, 2, -3, -9])
y2 = np.zeros_like(x1)
for i in range(len(x1)):
    if x1[i] < 0:
        y2[i] = x1[i]
print(y2)
```

+++

**B) Write code that produces the same result as A, but use vectorization instead of loops.**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3

```
