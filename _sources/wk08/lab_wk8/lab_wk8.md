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

# Lab Week 8

for week 8 - all functions have return statements, even if its None
positional arguments (file), kwargs (winlen=7), docstrings, scope. 

sketch:

functions make code reproducable, so you dont have to repeat yourself with large blocks of code

we have been using functions this whole time 

parts of a function: definition, args, kwargs, docstring, body, return statement (just like input, process, output!)

take code from wk6, package it in functions like so:

```{code-cell} ipython3
def check_inputs(winlen):
    """
    checks that user inputs are an odd number and corrects them if not
    """
    pass


def running_mean(data, winlen=7):
    """
    filters data with a running mean with window length winlen
    """
    winlen = check_inputs(winlen) # what does this tell us about variable scope?
    pass

def running_median(data, winlen=7):
    """
    filters data with a running median, window length winlen
    """
    winlen = check_inputs(winlen)
    pass

```

both the running mean and running median functions should *call* the check_inputs function. You can use functions to call functions. Keep track of which variables are passed where. 

Final hand in: for a given dataset, (something with interesting variability at widely varying timescales) make a plt.subplots(2) graph with the running mean in one frame and running median in the other. plot the data with many different sized windows, such that it would be laborious to try to copy/paste the original code from lab6

```{code-cell} ipython3
# make 8 plots with 3 lines of code!
windows = [1,3,7,11,21,32,100,155]
for window in windows:
    ax.plot(running_median(some_data, winlen=window))
```
