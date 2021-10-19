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

# Midterm Review solution

## EOSC 211

**Week 7 Day 1**

```{code-cell} ipython3
import numpy as np
```

## Question 1

**If  `a = np.array([7, 6, 5, 4, 3, 2, 1])`, what would be the values of  `b` and `c` if:** 

`b = a[1:-1:2]`

`c = [a / 2]`

**Determine the output as well as the data type of the output**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
import numpy as np

a = np.array([7, 6, 5, 4, 3, 2, 1])
b = a[1:-1:2]
c = [a / 2]

for i in [a, b, c]:
    print(i, type(i))
```

## Question 2

**What is the result of the following expressions?**

**A)** `6 == 2 + 3 * 1`

**B)** `14 > np.arange(6,2,-1) * 3 + 1`

**C)** `3 ** 0 / 4 - -3 / np.array([4, 3])`

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
a = 6 == 2 + 3 * 1
b = 14 > np.arange(6,2,-1) * 3 + 1
c = 3 ** 0 / 4 - -3 / np.array([4, 3])

[print(letter) for letter in [a,b,c]];
```

## Question 3

**This cell is supposed to loop through a dataset and find values of -999 (often used for "no data", or "error".) and flag the times at which the bad measurement occured. Find and correct 4 bugs to make it run correctly.**

+++

```python
# fix this code
meas = np.array([-999, -999, 2, 16, 3, 4, 4, 4, -999, 31, 4, 5, -999]) 
time = np.arange(0,len(meas) * 60,60)  # seconds

print("measurements: {meas}")
print("time recorded: {time}")

print("bad data recorded at times:")
for i in range(len(meas)):
    if meas[j] = -999:
        print(time[i])
```

```{code-cell} ipython3
# soln
meas = np.array([-999, -999, 2, 16, 3, 4, 4, 4, -999, 31, 4, 5, -999])
time = np.arange(0,len(meas) * 60,60)  # seconds

print(f"measurements: {meas}") # need f's for f strings
print(f"time recorded: {time}")

print("bad data recorded at times:")
for i in range(len(meas)): # use consistent indexing variables (could change them all to j)
    if meas[i] == -999: # booleans need "==", not "="
        print(time[i])
```
