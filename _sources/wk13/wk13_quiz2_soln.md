---
jupytext:
  cell_metadata_filter: -all
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

# Week 13 Quiz 2 Solution:  Review with numpy arrays, basic logical indexing

+++

## Name / Student #:
## Group:

+++

## Import the packages we need

```{code-cell} ipython3
import numpy as np
```

## Use the variables defined in the following cell to answer all the questions below.  Show ALL your work.

```{code-cell} ipython3
n1=4
n2=2
pp = np.pi
c1 = [4,3,2,1]
mynum = -2

# define X and A
X = np.zeros([n2,n1])
X[:,n1-1]=mynum
A = X.T

# define Y and Z
Y = np.ones_like(A)
Y[3,-1] += mynum
Y[:,0]=c1
Y[-1,:] *= np.pi

Z = Y==np.pi

# define c1vec and hit
c1vec= np.array(c1)
hit = (c1vec % 2) == 0
```

## For questions 1- 7 what is printed?

+++

## Question 1 (2 pts): 

`print(X, X.shape)`

<br />
<br />
<br />
<br />
<br />

```{code-cell} ipython3
# Solution
print(f"{X = }, \n{X.shape=}")    #the \n just makes a new line for prettier formatting
```

## Question 2 (2 pts):

`print(np.shape(c1), type(c1))`

<br />
<br />
<br />
<br />

```{code-cell} ipython3
# Solution
print(np.shape(c1), type(c1))
```

## Question 3 (4 pts):

`print(Y, Y.shape)`

<br />
<br />
<br />
<br />
<br />
<br />
<br />

```{code-cell} ipython3
# Solution
print(f"{Y = }, \n{Y.shape=}")
```

## Question 4 (1 pt):

`print(f"{Z=}")`

<br />
<br />
<br />
<br />
<br />

```{code-cell} ipython3
# Solution
print(f"{Z=}")
```

## Question 5 (2 pts):

`print(f"{A[Z]=},{len(A[Z])=}")`

<br />
<br />
<br />
<br />
<br />
<br />
<br />

```{code-cell} ipython3
# Solution
print(f"{A[Z]=},{len(A[Z])=}")
```

## Question 6 (3 pts):

`print(c1vec[hit],'pha')`

<br />
<br />
<br />
<br />
<br />

```{code-cell} ipython3
# Solution
print(c1vec[hit],'pha')
```

## Question 7 (3 pts):

```
for jj in range(0,n2,1):
    print(jj,Y[jj,:],Z[:,jj])
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
# Solution
for jj in range(0,n2,1):
    print(jj,Y[jj,:],Z[:,jj])
```
