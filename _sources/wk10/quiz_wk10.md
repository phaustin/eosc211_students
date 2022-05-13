---
jupytext:
  formats: ipynb,md:myst
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

## Week 10 Quiz Solution:  Practice with Dictionaries and Functions

+++ {"tags": []}

### Code tracing

The function and calling cell below contain code to get some info on commuting data provided by students.  For each mode of transportation there is a time in minutes provided by each student that is their commute time to or from school.

The function is missing some helpful explanation as to what it does and what it returns.

In words what is returned by the function and what is/are the data types of any output variable(s)?

What would get printed to the screen by the print command in the second cell after the function has been run? (include any numbers).

```{code-cell} ipython3
import numpy as np

def get_commute_stats(*commute_modes,transport=None):
    """
    INPUTS:  modes: comma separated list of one or more of the modes
                     "car", "bus", "bike", "walk"
             transport:  dictionary containing transportation mode and 
             associated commute times for people who use this mode    
    
    OUTPUTS:  
    """

    var_out={}
    for the_mode in commute_modes:
        a1 = len(transport[the_mode])
        a2 = np.min(transport[the_mode])
        a3 = np.max(transport[the_mode])
        var_out[the_mode] = [a1,a2,a3,]
        
    return var_out
```

```{code-cell} ipython3
# placeholder results (not the actual survey)
commute2021 = {
    "car": [14, 2, 3, 4, 2, 15, 30],
    "bus": [34, 40, 18, 14, 3, 1],
    "bike": [21, 3, 4, 3, 4],
    "walk": [14, 30, 40, 1, 2],
}


output=get_commute_stats("bike","car","walk", transport=commute2021)
print(output)
```

### Solution

output: dictionary containing # of people and the min, max times for each commute mode.

```python
{'bike': [5, 3, 21], 'car': [7, 2, 30], 'walk': [5, 1, 40]}
```
