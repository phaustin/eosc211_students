---
jupytext:
  cell_metadata_filter: all
  formats: ipynb,md:myst
  notebook_metadata_filter: all
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
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
  version: 3.8.10
---

- **Name:**
- **Student number:**

+++

**Instructions**:  Only one question this week

+++

# Week 7 quiz

+++

## Q1  Find the bugs


**This cell is supposed to find local minimums in the input time series, i.e. points that have values less than their neighbours on either side, and return their indices in `x`. But it has some bugs in it. Explain what they are and fix them.**

+++

```python
# fix this code
# y is a 1x100 array given as input
a = np.linspace(0,4*np.pi,100)
y = np.sin(a)
k = 0
while k < 100:
    if y[k] < y[k + 1] and y[k] > y[k - 1]:
        x[k] = k
    k = k - 1
```
