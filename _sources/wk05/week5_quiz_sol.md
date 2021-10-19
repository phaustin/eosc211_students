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

- **Name:**
- **Student number:**

+++

# Week 5 quiz solution

**Instructions**:  The three items on this page show the python code in individual cells in a  jupyter notebook.  For each of the three, write down what the cell would display if you ran it.

```{code-cell} ipython3
a=5
if a > 2:
    print(a)
if a < 6:
    print(a)
else:
    print("failed all tests")
```

```{code-cell} ipython3
a=7
if a <10 and a > 9:
    print(a)
elif a > 11:
    print(a)
else:
    print('failed all tests')
```

```{code-cell} ipython3
import numpy as np
a = np.arange(20,dtype=np.float64)
hit = np.logical_and(a > 8 , a < 13)
print(a[hit])
print(a.dtype)
```
