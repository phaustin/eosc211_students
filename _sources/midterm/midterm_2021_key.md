---
jupytext:
  cell_metadata_filter: all
  formats: ipynb,md:myst
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# e211 2021t1 midterm solutions

+++

Name (Last, First):
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Student Number:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Signature:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

In-class Group:
\_\_\_\_\_

+++

The exam is open-book, open-notes, but NO electronic accessories (e.g., calculators, phone, laptop, python, google, etc) are allowed.   

**This exam has 7 questions.** Complete all the questions.  The marks available for each question are indicated. The total number of marks available in this exam is 37 (plus 2 bonus). As a rough guide, you should expect to spend about 1 minute per mark.  

**SHOW YOUR WORK** and/or your reasoning as well as "the answer" - this allows us to assign something other than full or zero marks for a question.

For all questions you can assume that ```numpy``` and any other required packages have been imported, e.g.,
``` import numpy as np``` has been executed.

You will have 50 minutes to do the exam individually.  We will then collect your individual responses and you will have 20 minutes to do it in your group.

+++

## Question 1  (5 points)

An instrument that measures wind speed records the following data.  Note that np.isnan is a function
that returns ```True``` if a floating point number is np.nan, ```False``` if not.

```{code-cell} ipython3
:trusted: true

import numpy as np
vx = np.array([12, 10, 4, 1, 3, 2, 1, np.nan, np.nan, 4, 5, 3])

# Write out the values that would print for each of the following slices.

#a)  

print(f"a) {vx[:4]=}")



# b) 

print(f"b) {vx[4:9]=}")



# c)

print(f"c) {vx[9:]=}")


# d) 

print(f"d) {vx[vx > 8]=}")


# e) 

print(f"e) {(vx[np.isnan(vx) == False])=}")
```

## Question 2  (8 points)

a) (4 pts) The function `np.arange()` creates arrays using arguments `start, stop, step`. The function `np.linspace()` creates arrays using `start, stop, num`, where `num` is the number of elements in the array. Using each method, write 
the python command that would create the following array (i.e. write 2 lines of code that produce the same output):  

  [4,8,12,16,20,24]

```{code-cell} ipython3
:trusted: true

# soln
use_arange = np.arange(4,25,4) # 25 can be any number larger than 24
use_linspace = np.linspace(4,24,6)

print(f"using arange:   {use_arange}\nusing linspace: {use_linspace}")
```

b) (4 pts) Suppose you simultaneosly measure the speed and temperture of an object over time, and get the following
data points:

```
time = [10, 20, 30, 40, 50, 60, 70]  # seconds
speed = np.array([3.,5., 8., 6., 4., 3., 2.])  #meters/second
temperature = np.array([280., 283., 284., 287., 288., 286., 287.])  # Kelvins
```

Write python code that would use `np.logical_and` to find and print the times at which the object was moving
faster than 3 m/s and was warmer than 283 K.

```{code-cell} ipython3
:trusted: true

import numpy as np
time = np.array([10, 20, 30, 40, 50, 60, 70])  # seconds
speed = np.array([3.,5., 8., 6., 4., 3., 2.])  #meters/second
temperature = np.array([280., 283., 284., 287., 288., 286., 287.])  # Kelvins
hit = np.logical_and(speed > 3., temperature > 283.)
print(time[hit])
```

## Question 3 (8 points)

+++

The Fibonacci sequence $F_n$ is the sequence where each number in the sequence is the sum of its two preceeding numbers, where the first two numbers are:  


$$
F_{0}=0, \quad F_{1}=1
$$

For example, the first few numbers in the sequence are: 
$$ F_n = [0, 1, 1, 2, 3, 5, 8, 13, 21, ...]$$

and

$$
F_{n}=F_{n-1}+F_{n-2}
$$

for $n>1$.


Below we've provided a code that uses a for loop to calculate the Fibonacci sequence to a sequence length of $N$ (i.e., $N$ numbers). There are 4 distinct types of bugs (you might decide that one type appears more than once, depending on your choice of fixes). Circle each bug in the code below and correct them in your own copy.  If the same type of bug appears more than once, correct it everywhere it appears. 1 point per bug type identified, and 1 point for correction. (8 points). 

```
fibs = [0, 1]  # you can assume this line of code is ok.
n = 10.

for i in range(n-1):
     append.fibs((fibs[-1] + fibs[0])) 

print(fibs)
```

```{code-cell} ipython3
:trusted: true

# solution  -- note that you start with len(fibs) == 2
# which means your for loop needs to add 8 values
# 0, n-2 or 1, n-1 or 2,n  will all work

fibs = [0, 1]  
n = 10  # BUG 1: remove the . so it's not a float.

for i in range(n-2):  # BUG 2 need to stop 2 before end
    # append.fibs(fibs[-1] + fibs[0])  # BUG 3: should be fibs.append()
    fibs.append(fibs[-1] + fibs[-2])  # BUG 4: add last two in sequence
    # or with range(n-2)
    #fibs.append(fibs[i+1] + fibs[i]) 
    # or with range(1,n-1)
    # fibs.append(fibs[i] + fibs[i-1])
    # or with range(2,n)
    # fibs.append(fibs[i-1] + fibs[i-2])
    
    


print(fibs)
```

## Question 4  (6 pts)

a) (2 pts) What is the value of `a` after executing the code block below? Explain why.

```
a = 7
if a > 1:
    a += 3
elif a > 3:
    a += 2
    if a >= 10:
        a /= 2
```

```{code-cell} ipython3
:trusted: true

# solution


a = 7
if a > 1:
    a += 3
elif a > 3:
    a += 2
    if a >= 10:
        a /= 2
print(a)
```

b) (2 pts)  What is printed when the following code is run and what is the final value (or values) contained in ```b```? 

```
a = [7, 3, 9, 2]
for i in range(2): 
    b = a[i] * a[i+1]
    print (b)
```

```{code-cell} ipython3
:trusted: true

# solution


a = [7, 3, 9, 2]
for i in range(2): 
    b = a[i] * a[i+1]
    print (b)
```

c) (2 pts) What are the outputs of each of the following print statements?  If the output would be an error. message, explain the cause of the error

```
list1 = ['abcd', 786, 1.68, 'anya']
print(list1)
print('My height is ' + list1[2] + 'metres.')
```

```{code-cell} ipython3
:trusted: true


# solution

list1 = ['abcd', 786, 1.68, 'anya']
print(list1)
try:
    print('My height is ' + list1[2] + 'metres.')
except TypeError as ex:
    print(ex)
    
```

## Question 5 (4 pts + 2 BONUS)

+++

a) (1 pt) What is the shape of the following numpy array? Provide your answer as a tuple: (rows, cols).  (1 point)

```{code-cell} ipython3
:trusted: true

heights = np.arange(0, 20).reshape(10,2)
```

```{code-cell} ipython3
:trusted: true

print(f"{heights.shape=}")
```

 
 
 b) (1 pt) In words, what does the following ```for``` loop accomplish? (1 point)
 ```
heights = np.arange(0, 20).reshape(10,2)
new_heights = []
for height in heights.flatten(): 
    if height%2 != 0:
        new_heights.append(height)             
 ```

+++

creates a list news_heights and fills it with the  odd heights

+++

 
 
 c) (1 pt) How many numbers are in `new_heights`? 
 
10
 
 d)(1 pt)  What is the type of the variable `new_heights`?  
 
list
 
 e) (BONUS: 2 pts) In one line of code total, make a new variable called even_heights which only contains
 the even values  in heights, and make even_heights a numpy array.

```{code-cell} ipython3
:trusted: true

import numpy as np
np.linspace(4,25,6)
np.arange(4,26,2)
```

```{code-cell} ipython3
:trusted: true

heights = np.arange(0, 20).reshape(10,2)
even_heights = heights[heights % 2 == 0]
print(even_heights)
```

## Question 6 (4 points)

What will be printed to the screen as a result of running each of the following code snippets? Show any work.  One point per question.

+++

(a) `print(math.ceil(np.pi))`

```{code-cell} ipython3
:trusted: true

import math
print(math.ceil(np.pi))
```

(b) `print(f'My new number is {int(100*np.pi)}')`

```{code-cell} ipython3
:trusted: true

print(f'My new number is {int(100*np.pi)}')
```

(c\)-(d) are based on the following lines of code
``` 
    a = 6+3.1
    b = -1
    c = 0.
    d = 2
    e = a*b+c*d
    f = a*c
```
(c\) `print(f'e={e}')`

```{code-cell} ipython3
:trusted: true

a = 6+3.1
b = -1
c = 0.
d = 2
e = a*b+c*d
f = a*c
print(f'e={e}')
```

(d) `print(f'The type of f is {type(f)}')`

```{code-cell} ipython3
:trusted: true

print(f'The type of f is {type(f)}')
```

## Question 7 (2 points)

+++

What is printed to the screen after running this code? 1 pt per question.

```
x1 = np.arange(1,10)
y1 = np.arange(100,1000,100)
i1 = -1*x1>-5
i2 = y1==900 
z3=y1[np.logical_or(i1,i2)]
z4=x1[np.logical_and(i1,i2)]
```

+++

(a) `print(f'z3 = {z3}')`

```{code-cell} ipython3
:trusted: true

x1 = np.arange(1,10)
y1 = np.arange(100,1000,100)
i1 = -1*x1>-5
print(i1)
i2 = y1==900 
print(i2)
z3=y1[np.logical_or(i1,i2)]
z4=x1[np.logical_and(i1,i2)]
print(f'z3 = {z3}')
```

(b) `print(f'z4 = {z4}')`

```{code-cell} ipython3
:trusted: true

print(f'z4 = {z4}')
```
