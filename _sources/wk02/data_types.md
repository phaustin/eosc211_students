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

# Data Types

## EOSC 211

**Week 2**

**Learning Objectives:**  
1. Identify the following data structures: Int, Float, Boolean, String, List, Tuple, Dictionary
2. Identify special object data types, i.e. numpy array
3. Perform operations on each data type

Useful references:

[course text on data types](https://phaustin.github.io/Problem-Solving-with-Python/Data-Types-and-Variables/combine_data_types.html)

+++

### Question 1

**What is the *data type* of each of the following?**

```{code-cell} ipython3
var1 = 2
var2 = 3.4
var3 = True
var4 = "vogon poetry"
var5 = [var1, var2]
var6 = (var1, var2, var3)
var7 = {"answer":42, "question":False}
```

### Question 2

**What is the *data type* of each of the following? Explain in a sentence or two what is happening on each line**.  Hint - see [Reading for this week](https://phaustin.github.io/Problem-Solving-with-Python/Data-Types-and-Variables/combine_data_types.html)

```{code-cell} ipython3
var8 = 7 / 2
var9 = var2 == var4
var10 = var1 + var2
var11 = f"{var2}"
```
