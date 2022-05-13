---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: -all
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

# Week 13 Quiz 1 Solution:  Review with basic functions, loops, code tracing


### Name / Student id:
### Group:





### Import the packages we need

```{code-cell} ipython3
:trusted: false

import numpy as np
```

### The following function is called by questions 1-3.

```{code-cell} ipython3
:trusted: false

def myfun(n):
    """ function doc string which i deliberately have not written"""
    
    nfac = 1;
    for i in range(n,1,-1):     
        nfac = nfac*i
        print(i,nfac)
    
    return nfac
```

#### Question 1 - What is printed to the screen? Show your work (4 pts)

    'y1 = myfun(4)
    print(f"{y1=}")'

<br />
<br />

```{code-cell} ipython3
:trusted: false


```

#### Question 2 - What is printed to the screen? Show your work (2 pts)

    'y2 = myfun(-4)
    print(f"{y2=}")'

<br />
<br />

```{code-cell} ipython3
:trusted: false

```

#### Question 3 - What is printed to the screen? Show your work (2 pts)

    'y3 = myfun(np.pi)
    print(f"{y3=}")'

<br />
<br />

```{code-cell} ipython3
:trusted: false

```

#### Question 4 (3 pts)
I want to add together the numbers in an array 'x' until my sum exceeds the number in the variable target, then **stop** and return the sum and the number of elements that were summed.  You can assume that there are enough elements in x that I don't get to the end of the array before reaching the target.  I write the following code which has a semantics error not a syntax error (i.e. it runs but doesn't do what it was intended to do).  What is output to the screen? (Show your work).  

```
x = np.array([1, 0, -2, 7, 8, 1, 10, 21, -3, 5, -3])

target = 21

mysum = 0

for i in range(0, len(x)):

    if (mysum+x[i] <= target):
    
        mysum += x[i]
        
        nels = i
        
print (f"{mysum=},{nels=}")
```

<br />
<br />

<br />
<br />

<br />
<br />

<br />
<br />

```{code-cell} ipython3
:trusted: false

```

```{code-cell} ipython3
:trusted: true


```
