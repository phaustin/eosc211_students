---
jupytext:
  cell_metadata_filter: all
  formats: ipynb,md:myst
  notebook_metadata_filter: all
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  codemirror_mode:
    name: ipython
    version: 3
  file_extension: .py
  mimetype: text/x-python
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
  version: 3.8.10
---

- **Name:**
- **Student number:**

+++

**Instructions**:  Only one question this week

+++

# Week 7 quiz solution

+++

## Q1  Find the bugs


**This cell is supposed to find local minimums in the input time series, i.e. points that have values less than their neighbours on either side, and return their indices in `x`. But it has some bugs in it. Explain what they are and fix them.**

+++

```python
# fix this code
# y is a 1x100 array given as input
a = np.linspace(0,4*np.pi,100)
y = np.sin(a)
k = 0
while k < 100:
    if y[k] < y[k + 1] and y[k] > y[k - 1]:
        x[k] = k
    k = k - 1
```

```{code-cell} ipython3
# andrew's soln
import numpy as np
a = np.linspace(0,4 * np.pi,100)
y = np.sin(a)
x = [] # we need to create a list to add to
k = 1 # since we need to reference k-1, start at the second element of the array and end at the second last
while k < len(y)-1: # this is better than hardcoding the limits for k. what if y changes?
    if y[k] < y[k+1] and y[k] < y[k-1]:
        x.append(k) 
    k += 1 # iterate forward, not backward

print(x)
```
