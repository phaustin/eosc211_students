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

# Debugging II

## EOSC 211

**Week 9 Day 2**

**Learning Objectives:**  
??

+++

## Question 1

**We have a record of speeds for a moving object (say, a drifter). We  want to see how long the object moves at a constant speed. In particular, we want to write code which will measure the length of time that the speed is less than `maxspd` and greater than `minspd` (call this a “run”). For example, if the speeds are stored in an array: `spd = np.array([5 1 5 5 5 10 5 1 5 5 5 1 2 2 5])` with `minspd=4` and `maxspd=6`, then we have 3 runs of length 1 and 2 runs of length 3, with no other runs. We would want to store this information in another variable in which the i$^{th}$ value was the number of runs of length i, i.e.:**

```
runs=[3 0 2 0 0 ...]
```

**Here is some code we have started to write to calculate runs in this way. However, there are 5 small bugs in this code - find and fix them.**

```{code-cell} ipython3
import numpy as np
# debug this code

def runlength(spd, minspd, maxspd):
    """
    RUNLENGTH calculstes run lengths tatistics

    Inputs
    spd: a time series vector of track speeds
    minspd and maxspd: the lower and upper limits of speed for a run

    Outputs
    runs: an array in which runs[i] is the number of runs of i points.
    """
    N = len(minspd)
    runs = np.zeros(N)
    runlen = 0
    isrun = 0
    for i in range(N)
        if spd[k] >= minspd and spd[k] <= maxspd:
            isrun=True
            runlen = runlen+1
        elif (spd[k] < minspd or spd[k] > maxspd ) and isrun:
            runs[runlen]=runs[runlen]+1
            runlen=0
            isrun=False
    if isrun:
        runs[runlen]=runs[runlen]+1
    
```

```{code-cell} ipython3
import numpy as np

# andrew's soln
def runlength(spd, minspd, maxspd):
    """
    RUNLENGTH calculstes run lengths tatistics

    Inputs
    spd: a time series vector of track speeds
    minspd and maxspd: the lower and upper limits of speed for a run

    Outputs
    runs: an array in which runs[i] is the number of runs of i points.
    """
    N = len(spd)  # should be the length of spd, not minspd
    runs = np.zeros(N)
    runlen = 0
    isrun = False  # this should be a boolean, not an integer
    for k in range(N):  # use a consistent index variable, 'i' or 'k', don't forget the colon
        if spd[k] >= minspd and spd[k] <= maxspd:
            isrun = True
            runlen = runlen + 1
        elif (spd[k] < minspd or spd[k] > maxspd) and isrun:
            runs[runlen] = runs[runlen] + 1
            runlen = 0
            isrun = False
    if isrun:
        runs[runlen] = runs[runlen] + 1
    return runs  # the function needs a return statement


spd = np.array([5, 1, 5, 5, 5, 10, 5, 1, 5, 5, 5, 1, 2, 2, 5])
minspd = 4
maxspd = 6
runlength(spd, minspd, maxspd)

# annoying indexing error that includes runs of length 0. rewrite this whole function less matlab-y?
```

## Question 2

**Now, to calculate the mean runlength, we have 3 runs of length 1 and 2 of length 3, so the mean is $(3*1 + 2*3)/(3 + 2)$. This piece of code is supposed to compute the mean runlength, but it doesn’t work. Fix the 3 small bugs.**

```{code-cell} ipython3
# andrew's soln (incomplete)

def mean_run_len(spd, minspd, maxspd):
    sumr=0
    rbar=0
    k = 0 # initialize k
    while k in range(N): # change loop structure
        rbar = rbar*k + runs(k)
        sumr = sumr   + runs(k)
        k += 1

    rbar = rbar-sumr
    return rbar
```
