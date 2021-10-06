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

# Some Review Plus Built-In Functions, Arrays Preview

## EOSC 211

**Learning Goals:**

* Review variable assignment, structural elements of Python
* *Index* and *slice* list type variables
* Use built-in functions to do useful things

+++

### Question 1

The code snippet below was intended to calculate the surface area of the Earth and print the answer to the screen.  What is the actual output (describe the quantity in words) of the code snippet?

```{code-cell} ipython3
# radius of Earth in km
radius = 6371
area = 4 * 3.14 * radius ** 2
# radius of Moon in km
radius = 1739
area = 4 * 3.14 * radius ** 2
```

### Question 2

Identify in the code snippet:

* Variable names
* Functions
* Special characters
* Operators

+++

### Question 3

Write down what each line of code does

+++

### Question 4

What happens if we restart the kernel after executing this cell (the \[$\circlearrowright$\] or button)?

+++

### Question 5

Let's define the following variable `mags`

```{code-cell} ipython3
mags = [4.2000, 4.1000, 4.1000, 4.1000, 4.3000, 4.2000, 4.4000, 4.1000, 4.0000, 4.7000]
```

**A)** How could we access the third number from the left?

**B)** How to assign the last variable in this list to a new variable called `mags2`

+++

## Question 6

Describe what is happening on this one line of code (it's surprisingly a lot). List the steps in order

```{code-cell} ipython3
y3 = max(mags[3:8])
```
