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

# Week 12 Quiz: solution



### Name / Student id:
### Group:


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
```

### For questions 1- 7 what is printed?

+++

### Question 1 (1pt): 

`print(f"{A=}")`

<br />
<br />

```{code-cell} ipython3
print(f"{A=}")
```

    A=array([[ 1.        ,  2.        ,  3.        ],
           [-9.42477796,  0.        ,  1.57079633]])

+++

### Question 2 (1 pt):

`print(f"{type(A[1,2])}")`

<br />
<br />

```{code-cell} ipython3
print(f"{type(A[1,2])}")
```

    <class 'numpy.float64'>

+++

### Question 3 (1 pt):

`print(f"{A.shape}")`

<br />
<br />

```{code-cell} ipython3
print(f"{A.shape}")
```

    (2, 3)

+++

### Question 4 (1 pt):

`print(f"{B.shape}")`

<br />
<br />

```{code-cell} ipython3
print(f"{B.shape}")
```

    (2, 3)

+++

### Question 5 (1 pt):

`print(f"{type(B)}  {B.dtype}")`

<br />
<br />

```{code-cell} ipython3
print(f"{type(B)}  {B.dtype}")
```

    <class 'numpy.ndarray'>  float64

+++

### Question 6 (1 pt):

`print(f"{B.T[:,-1]=}")`

<br />
<br />

```{code-cell} ipython3
print(f"{B.T[:,-1]=}")
```

    B.T[:,-1]=array([ 1.,  1., 42.])

+++

### Question 7 (2 pts):

```
Tcut=23

print(f"Rainfall on days > {Tcut} C was {rain[temp>Tcut]} mm")
```

<br />
<br />

```{code-cell} ipython3
Tcut=23
print(f"Rainfall on days > {Tcut} C was {rain[temp>Tcut]} mm")
```

    Rainfall on days > 23 C was [0 2 1 2] mm

+++

### Question 8 (1 pt):  

Write a **single** line of code that will construct a dictionary called `telnos` from the following tuples

```
t1=("phil",22175)
t2=("catherine",73480)
t3=("no-one",71111)
```

<br />
<br />
<br />
<br />

```{code-cell} ipython3
# Q8:  Answer
t1=("phil",22175)
t2=("catherine",73480)
t3=("no-one",71111)
telnos = dict([t1,t2,t3])
print(telnos)
```

    {'phil': 22175, 'catherine': 73480, 'no-one': 71111}

+++

### Question 9 (2 pts):  

Now assume that Phil moved into Catherine's office and Catherine decided to retire to a tropical island.  Write  **2 lines of code** to assign Catherine's # to Phil and remove Catherine's entry from the dictionary.

<br />
<br />
<br />
<br />
<br />
<br />

```{code-cell} ipython3
telnos = dict([t1,t2,t3])   # just in case run this cell out of order reset telnos to original
telnos["phil"]=telnos["catherine"]  
telnos.pop("catherine")   # use pop
print(telnos)

# add my phone # back and reset Phil's for second ways of doing this
telnos = dict([t1,t2,t3])

telnos["phil"]=73480    # works but error prone -- need to copy number by hand
del telnos["catherine"]    # using del (not in our text but might have seen online)
print(telnos)

# best: (also not in text) -- copy popped value, no need to hand enter
telnos = dict([t1,t2,t3])
telnos["phil"]=telnos.pop("catherine")
# 
# you can give pop an optional value to return
# if key is missing from dictionary
#
telnos = dict([t1,t2,t3])
telnos["phil"]=telnos.pop("katherine", None)
print(f"missing key: {telnos=}")
```

```{code-cell} ipython3
telnos=dict([t1,t2,t3])
del telnos['catherine']
telnos
```

    {'phil': 73480, 'no-one': 71111}
    {'phil': 73480, 'no-one': 71111}
