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

# Dictionaries, F String Literals

## EOSC 211

**Week 10 Day 1**

**Learning Objectives:**  
1. ?

```{code-cell} ipython3
# placeholder results (not the actual survey)
transport = {
    "car": [14, 2, 3, 4, 2, 15, 30],
    "bus": [34, 40, 18, 14, 3, 1],
    "bike": [21, 3, 4, 3, 4],
    "walk": [14, 30, 40, 1, 2],
}
```

## Question 1

**`transport` is a dictionary containing the results from the poll in week 2. Write code to compute the following, and print your results using *f string literals*** 

**(you can import any packages you like. Keep your code succinct and well commented)**

**A) The median commuting time for people who drive**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
import numpy as np

drivemed = np.median(transport["car"])
print(f"The median commute time for people who drive is {drivemed} minutes")
```

**B) The number of people who ride bikes to UBC**

```{code-cell} ipython3
# your code here
```

```{code-cell} ipython3
# andrew's soln
cyclists = len(transport["bike"])

print(f"There are {cyclists} cyclists in EOSC211 this semester.")
```

## Question 2

!!!! no direct translation from matlab. formatted print statements are way less complicated in python.
