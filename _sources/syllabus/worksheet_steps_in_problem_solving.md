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

# Steps In Problem Solving

## EOSC 211

**Week 2 Day 1**

**Learning Objective:** Practice the steps in problem solving using earthquake data.

<img src="quakemap.png" width="500">

+++

### Question 1

**Write down the 3 steps in algorithm design mentioned in the text book OR write down some steps you think will be common to problem solving with python (you might have more than 3 steps):**

+++

1) 

2)

3)

4)

+++

### Question 2
**We want to find the largest earthquake in the Pacific Northwest region in the past year.  The data sheet gives all earthquakes in this area that have a magnitude of at least 4.0.**

```{code-cell} ipython3
from e211_lib import e211
e211.show_earthquake_data()
```

source: http://www.earthquakescanada.nrcan.gc.ca/

**A) We want to design an *algorithm* to find the largest earthquake. Describe in words the *input* and *output* of your algorithm**

+++

Input:

Output:

+++

**B).  Below, document the procedure you went through to get to your answer for the value of the output above.  <br> HINT:**  you need to think about what your brain actually does when it finds the largest # in a list

+++

your answer here

+++

### Question 3

**The following is a *Python* code snippet:**

```{code-cell} ipython3
mag1 = 4.9
mag2 = 5.3
if mag1 > mag2:
    max_mag = mag1
else:
    max_mag = mag2
```

**Identify the following:**

+++

A) Variable names:

B) Operators:

C) Reserved words:

D) Special characters:
