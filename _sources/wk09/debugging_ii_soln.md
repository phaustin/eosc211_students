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

# Debugging II

## EOSC 211

**Week 9 Day 2**

**Learning Objectives: More practice with**  
1.  Dictionaries
2.  Functions
3.  Debugging

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
    RUNLENGTH calculates run lengths tatistics

    Inputs
    spd: a time series (1D numpy array or list) of track speeds
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

```{code-cell} ipython3
import numpy as np

# Catherine's soln
def runlength(spd, minspd, maxspd):
    """
    RUNLENGTH calculates run length statistics

    Inputs
    spd: a time series vector of track speeds
    minspd and maxspd: the lower and upper limits of speed for a run

    Outputs
    runs: a dictionary with runlengths as keywords and # runs as values
          only runlengths with a non-zero # runs are included  
    """
    N = len(spd)  # should be the length of spd, not minspd
    #runs = np.zeros(N)
    runlen = 0
    runs_dict = {}   # set up an empty dictionary
    isrun = False  # this should be a boolean, not an integer
    for speed in spd:  # use a consistent index variable, 'i' or 'k', don't forget the colon
        if speed >= minspd and speed <= maxspd:    # CJ pythonic for loop fix
            isrun = True
            runlen += 1   # CJ small pythonic fix
        elif (speed < minspd or speed > maxspd) and isrun:   # CJ pythonic for loop fix
            runs_dict[str(runlen)] = runs_dict.get(str(runlen),0) +1   # I want to hear set the new keyword in dictionary if doesn't exist
                                          # then set it's value to 1 or increment it if it already existed.
            runlen = 0
            isrun = False
    if isrun:
        runs_dict[str(runlen)] = runs_dict.get(str(runlen),0) + 1    # and obviously this will need a fix.
    return runs_dict  # the function needs a return statement


spd = np.array([5, 1, 5, 5, 5, 10, 5, 1, 5, 5, 5, 1, 2, 2, 5, 5])
minspd = 4
maxspd = 6
runlength(spd, minspd, maxspd)

# CJ: I made a couple of edits things c.f. above and also turned into a dictionary. 
# The dictionary is not "ordered" ie # runs by increasing runlength but this doesn't matter
# (obvious b/c I added an extra 5 for this test at end of speed array)
```
