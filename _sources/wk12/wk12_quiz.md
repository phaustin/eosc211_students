---
jupytext:
  cell_metadata_filter: -all
  notebook_metadata_filter: -all
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
orig_nbformat: 4
---

### Name / Student #:
### Group:

+++

## Week 12 Quiz:  Review with numpy arrays, basic logical indexing, dictionary construction

### Import the packages we need

```{code-cell} ipython3
import numpy as np
```

### Use the variables defined in the following cell to answer all the questions below

```{code-cell} ipython3
pp = np.pi
ult_ans = 42
row1 = [1, 2, 3]

# set up array A
A = np.array([ row1, [-pp*row1[2], 0, pp/row1[1]] ]) 

# set up array B
B = np.ones_like(A)       # default dtype for array generators is floats
B[:,-1]*=ult_ans

# set up variables temp and rain
D = np.array([23.6, 22.5, 21.8, 24.9])
rain = np.array([0, 3, 0, 2, 1, 0, 5, 2])
temp = np.append(D,D)

#set up dictionary entries
t1=("phil",22175)
t2=("catherine",73480)
t3=("no-one",71111)
```

### For questions 1- 7 what is printed?

+++

### Question 1 (1pt): 

`print(f"{A=}")`

<br />
<br />

+++

### Question 2 (1 pt):

`print(f"{type(A[1,2])}")`

<br />
<br />

+++

#### Question 3 (1 pt):

`print(f"{A.shape}")`

<br />
<br />

+++

#### Question 4 (1 pt):

`print(f"{B.shape}")`

<br />
<br />

+++

### Question 5 (1 pt):

`print(f"{type(B)}  {B.dtype}")`

<br />
<br />

+++

### Question 6 (1 pt):

`print(f"{B.T[:,-1]=}")`

<br />
<br />

+++

### Question 7 (2 pts):

```
Tcut=23

print(f"Rainfall on days > {Tcut} C was {rain[temp>Tcut]} mm")
```

<br />
<br />

+++

### Question 8 (1 pt):  

Write a **single** line of code that will construct a dictionary called `telnos` from the following tuples

```python
t1=("phil",22175)
t2=("catherine",73480)
t3=("no-one",71111)
```

<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />

+++

### Question 9 (2 pts):  

Now assume that Phil moved into Catherine's office and Catherine decided to retire to a tropical island.  Write  **2 lines of code** to assign Catherine's # to Phil and remove Catherine's entry from the dictionary.

