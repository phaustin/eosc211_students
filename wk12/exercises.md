---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Exercises

## EOSC 211

**Week 11 Day 1**

**Learning Objectives:**  
1. Solve problems with python code
2. Choose appropriate data structures to make your code neat and efficient


## Question 1

**A) You have a cash register with \\$20, \\$10, \\$5, \\$2, \\$1, \\$0.25, \\$0.10, \\$0.05 bills or coins. Write a program to make change – so that, for example, if someone gives you a \\$10 bill for something costing \\$6.55 the program will calculate that you get back \\$3.45 in change consisting of a \\$2, and \\$1, a \\$0.25, and 2 \\$0.10**  

**You may find the floor division `//` and modulo ```%``` operators to be of use.**

**Store the denominations in a dictionary `denom={'twenties', 'tens', 'fives', 'toonies'...}`, The rest of the program is up to you. There are many correct ways to solve this problem**

```python
item_cost = 6.55  # dollars
cash_in = 10  # dollars
```

```python
# your code here
```

```python
# andrew's soln

# create a dictionary of bill names and values to loop over
money = {
    "twenties": 20,
    "tens": 10,
    "fives": 5,
    "toonies": 2,
    "loonies": 1,
    "quarters": 0.25,
    "dimes": 0.1,
    "nickels": 0.05,
}
denom = {}  # initialize an empty dictionary to put change into
change = cash_in - item_cost

for key in money.keys():
    denom[key] = change // money[key]  # add to denom dictionary
    change = change % money[key]  # get remaining chance owed

print(denom)
```

**B) Turn this into a function called `getchange` that will take as input `item_cost`, `cash_in` and return `change`. Also, make your funtion raise an error if the customer does not give enough money to cover the cost of the purchase**

```python
# your code here
```

```python
# andrew's soln
def change(item_cost, cash_in):
    money = {
        "twenties": 20,
        "tens": 10,
        "fives": 5,
        "toonies": 2,
        "loonies": 1,
        "quarters": 0.25,
        "dimes": 0.1,
        "nickels": 0.05,
    }
    denom = {}  # initialize an empty dictionary to put change into
    change = cash_in - item_cost
    if change < 0:
        raise ValueError('not enough cash to cover item cost')

    for key in money.keys():
        denom[key] = change // money[key]  # add to denom dictionary
        change = change % money[key]  # get remaining chance owed

    return denom
```

## Question 2

**A) For  `x1=[1, 7, -8, 2, -3, -9]`, what is contained in `y2` in each case after the code runs?  Do these three snippets of code do the same thing?  Show your work.**

```python
import numpy as np
x1 = np.array([1, 7, -8, 2, -3, -9])
y2 = []
for i in range(len(x1)):
    if x1[i] < 0:
        y2.append(x1[i])
print(y2)
```

```python
y2 = x1
k = 0
for i in range(len(x1)):
    if x1[i] < 0:
        k = k + 1
        y2[k] = x1[i]
print(y2)
```

not sure what the teachable is on this question... revisit later


**B) Write code that produces the same result as A, but use vectorization instead of loops.**

```python
# your code here
```

```python
# andrew's soln
y2 = x1[x1 < 0]
print(y2)
```
