---
celltoolbar: Create Assignment
jupytext:
  cell_metadata_filter: all
  formats: ipynb,md:myst
  notebook_metadata_filter: all
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  codemirror_mode:
    name: ipython
    version: 3
  file_extension: .py
  mimetype: text/x-python
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
  version: 3.8.12
---

- **Name:**
- **Student number:**

+++

**Instructions**:  Answer all three questions

+++

## Q1  What does the following cell print?

```{code-cell} ipython3
for the_name in ['tom','lisa','joey','steph']:
    print(the_name)
    if the_name == 'joey':
        break
```

## Q2 What does the following cell print?

```{code-cell} ipython3
a = -1
while a < 3:
    a = a+1
    print(a)
```

## Q3 What does the following cell print?

```{code-cell} ipython3
for icount in range(3):
    jcount = 0
    while jcount < 2*icount:
        print(icount,jcount)
        jcount = jcount + 1
        
```

## Provide code that does the following

Use a while loop to print all numbers between 0 and 20 (inclusive) that
are divisible by 5

```{code-cell} ipython3
counter = 0
while counter <= 20:
    if counter % 5 == 0:
        print(counter)
    counter = counter + 1
```
