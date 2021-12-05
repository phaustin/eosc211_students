---
jupytext:
  formats: ipynb,md:myst
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

# Worksheet Solution: Review Exercises EOSC 211

## Week 13,  Worksheet 1

```{code-cell}
# import the packages we might need
import numpy as np
from matplotlib import pyplot as plt
import math
```

### Question 1 -  Practice with while versus for loops  
How would you improve the code in the last problem on the quiz to make it work properly using a while loop?  Here's the code you were given and (in words), what it was supposed to do:

+++

#### From quiz:  
I want to add together the numbers in an array 'x' until my sum exceeds the number in the variable target, then **stop** and return the sum and the number of elements that were summed.  You can assume that there are enough elements in x that I don't get to the end of the array before reaching the target.  I write the following code which has a semantics error not a syntax error (i.e. it runs but doesn't do what it was intended to do).  What is output to the screen? (Show your work).  

```{code-cell}
x = np.array([1, 0, -2, 7, 8, 1, 10, 21, -3, 5, -3])

target = 21

mysum = 0

for i in range(0, len(x)):

    if (mysum+x[i] <= target):
    
        mysum += x[i]
        
        nels = i
        
print (f"{mysum=},{nels=}")
```

```{code-cell}
# Catherine's solution

x = np.array([1, 0, -2, 7, 8, 1, 10, 21, -3, 5, -3])

target = 21
mysum = 0
i = 0  # 0.5 pt for counter here 
while (mysum+x[i] <= target):  # 0.5pt for while loop line; 0.5 pt line for ditching for and if.
    mysum += x[i]
    i = i+1    # 0.5 pt for incrementing counter
    print(i, mysum)
        
print (f"{mysum=},{i=}")
```

### Question 2: Basic function Practice
#### A)
Write a function `transp` that will take as input a 2-D array A, and return the array B where `B[i,j] = A[j,i]`. Do not use a built-in python function.

```{code-cell}
# your code here
```

```{code-cell}
# Catherine's solution

def trans(AA):

    """
    Computes transpose BB of matrix AA, i.e. BB[i,j] = AA[i,j]
    
    Input:  2-D matrix AA
    Output: 2-D matrix BB
    
    Assumes numpy has been imported
    """

    [n,m] = AA.shape    # same as np.shape(AA)
    # explicit double loop; alternatively inner loop could be replace by B[:,ii] = A[ii,:]
    BB = np.empty([m,n])
    for ii in range(0,n):
        for jj in range(0,m):
            BB[jj,ii] = AA[ii,jj]

    return BB
```

```{code-cell}
# Testing my solution

A1 = np.array([[2, 3, 0], [1, -1, 1]])
B1 = trans(A1)
print(f"\n{A1=} \n{B1=}")
```

#### B)
Add a check to the function code that will exit the function with an error message if A is not a 2-D array.

```{code-cell}
# Catherine's solution

def trans2(AA):

    """
    Computes transpose BB of matrix AA, i.e. BB[i,j] = AA[i,j]
    
    Input:  2-D matrix AA
    Output: 2-D matrix BB
    
    Assumes numpy has been imported
    """
    try:
        #--- ERROR CHECKING  -- catch and release
        if (not(isinstance(AA, np.ndarray))):
            raise TypeError("AA is not a ndarray")
        elif (A1.ndim != 2):
            raise ValueError("AA not 2D")
    except (ValueError,TypeError) as theError:
        print(f"caught error '{type(theError)}, '{theError}', returning None")
        return None
    #---

    [n,m] = AA.shape    # same as np.shape(AA)
    # explicit double loop; alternatively inner loop could be replace by B[:,ii] = A[ii,:]
    BB = np.empty([m,n])
    for ii in range(0,n):
        for jj in range(0,m):
            BB[jj,ii] = AA[ii,jj]

    return BB
```

```{code-cell}
# Testing my solution with a 1 D array

A1 = np.array([3,2,1])
B1 = trans2(A1)
```

```{code-cell}
# Testing my solution with a string

A1 = "hello"
B1 = trans2(A1)
```

### Question 3
The function $e^x$ can be calculated from the following formula:  $e^x = \Sigma_{k=0}^{\inf} \frac {x^k}{k!} = 1 + x + \frac {x^2} {2!} + \frac {x^3} {3!} + \cdots $.  You want to write a piece of code that will compute `y` = $e^x$, given a value for `x` using this series expansion, keeping all the terms until the difference between successive terms is less than some specified amount, contained in the variable `target_err`.

1.  Would you use a while loop or a for loop?  Give a reason for your answer.

2.  Complete the python code below to do this.  Also print the number of terms used to compute y.

```{code-cell}
x = 2
target_err = 0.1

# initialize some variables 
i = 0
y = 0
term = x**i/math.factorial(i)

# write your loop here


    
# write your print statement here
```

```{code-cell}
# Catherine's solution

x = 2
target_err = 0.1

# initialize some variables 
i = 0
y = 0
term = x**i/math.factorial(i)

# loop here
while (term>target_err):
    y += term
    i = i+1
    term = x**i/math.factorial(i)
    print(i, term, y)    # print out at end of each loop so is clear that i is lagging nterms by 1
    
truevalue = np.exp(x);
print(f"\n{y=} \nnterms = {i+1} \n{truevalue=}")  # note that my number of terms needed to be i+1
```

### Question 4:  code tracing, logical indexing,  for loops
What is in `y` after exectuing this code?

```{code-cell}
x=np.empty(8)
x[0]=1
x[1]=1
for k in range(2,len(x)):
    x[k]=x[k-1] + x[k-2]

y = x[np.logical_and(x>3,x%2==1)]
```

```{code-cell}
# your answer here
```

```{code-cell}
# Catherine's solution
print(f"{x=}\n{y=}")
```

### Question 5:  more practice with for loops / if, elif

The following code produces a uniform random sample of 3 numbers that lie between
0 and 10 (excluding 10 exactly).  Use this code to produce  
100  samples each of 3 numbers, and put the samples into one of two lists:  `accept_list` if one of the 
three numbers is greater than or equal to 9, and `reject_list` if all three numbers are less
than 9.  Bonus: How many samples do you think will be in each list?  Increase the sample size to 1000; 10,000;
100,000 -- do the lengths match your guess?

```{code-cell}
from numpy.random import random_sample
my_sample = random_sample([3])*10
```

```{code-cell}
# your code here
```

```{code-cell}
# phil's answer
accept_list = []
reject_list = []
for i in range(100000):
    my_sample = random_sample([3])*10
    hit = my_sample >= 9
    if np.sum(hit) > 0:
        accept_list.append(my_sample)
    else:
        reject_list.append(my_sample)
        
print(f"{len(accept_list)=}")
print(f"{len(reject_list)=}")
0.9**3
        
    
```

### Question 6 (harder):  Practice with *args

Turn the function in Question 1 into a function that will take as input an arbitrary number of 2-D arrays and return the transpose of each. 

The following resources are useful if you are confused about wrapping / unwrapping of arguments and keyword arguments:

1. https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/

2. https://shecancode.io/blog/unpacking-function-arguments-in-python

3. https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/

```{code-cell}
# Catherine's solution

def trans3(*args1):

    """
    Computes transpose BB of matrix AA, i.e. BB[i,j] = AA[i,j] for all matrices AA in the list specified by amats
    
    Input:  args1 =  tuple of 2-D matrices 
    Output: args2 =  list of 2-D matrices BB
    
    Assumes numpy has been imported
    """

    print(args1)
    print(f"{type(args1)=}")
    args2 = []
    for AA in (args1):   # unpack the input arguments by iterating thru the tuple
        [n,m] = AA.shape    # same as np.shape(AA)

        BB = np.empty([m,n])
        for ii in range(0,n):
            BB[:,ii] = AA[ii,:]    # implementing more efficient approach here
        args2.append(BB) 

    print(f"{type(args2)=}")
    return args2
```

```{code-cell}
# Testing my solution

A1 = np.array([[2, 3, 0], [1, -1, 1]])
A2 = np.array([[np.pi, 2*np.pi], [0, 0]])

# first pass in arguments explicitly from calling script, b/c we know how many of them we want to pass
B1, B2, B3, B4 = trans3(A1,A2,A1,A2)
print(f"\n{A1=} \n{B1=} \n{A2=} \n{B2=} \n{B3=} \n{B4=}")
```

### A few FAQ / comments about *args

1.  What is the `*` doing in `def trans2(*args1):`?  The `*` or `splat` can be thought of as an operator.  It is operating on the function arguments and returning a tuple called `args1`:  see the output of  `print(f"{type(args1)=}")`
</br>

2.  We made `args2` a list of 2D arrays.  The function returns this which is then "unpacked" into the individual variables `B1`, `B2`, `B3` and `B4`.  This communicates to someone reading the code that you expect
exactly 4 items in the args2 list returned by trans2, and that you want to work with them as individual variables.
Python will raise a ValueError if the length of args2 is not 4.

</br>

3. One thing to remember is that tuple creation and unpacking is handled by the comma operator, so e.g.
```
    a = 1,2,3  # packs or creates the tuple, a
    x,y,z = a  # unpacks `a` into x,y,z; also called multiple assignment
```
</br>

4.  We've seen this tangentially before in references to multiple assignment in for loops. The last ref on the list above is really helpful in covering tuple, list unpacking and packing.  

```
person_dictionary = {'name': "CJ", 'university': "UBC"}

# one dictionary item at a time print key and value
print(f"Loop over items")
for item in person_dictionary.items():
    print(f"Key {item[0]} has value {item[1]}")

# Same thing but with multiple assignment (like multiple assignment with = operator)
print(f"\nMultiple assignment loop")
for key, value in person_dictionary.items():
    print(f"Key {key} has value {value}")
```    
</br> 

5.  Phil says:  "Handling an arbitrary number of function arguments is definitely useful, but in my own code I don't find myself using it very often, since I'd like the function signature to be as specific as possible.    I use kw expansion much more often, because all the keywords are specified in the function signature, and the creator of the dictionary that's going into `my_fun(**kw_dict)` knows what they put into the dictionary.  So you get the best of both worlds -- much less typing when you call the function, but complete documentation when you read the function signature."

+++

### Question 7:  Type / Dimensions Quickies

Use the following variable definitions to answer the questions below

```{code-cell}
a = np.array([[1, 2], [3, -1], [0, 1]])
b = np.arange(3, -3, -2)
b = np.expand_dims(b, axis=[0])
c = np.ones(3)
d = [10,11,12]
e = a*a
f = b*d
try:
    g = a*a.T
except ValueError as ve:
    print(f"caught ValueError: '{ve}'")
```

What is the shape of 
</br>

a) `a`
</br>
</br>

b) `b`
</br>
</br>

c) `c`
</br>
</br>

d) `d`
</br>
</br>

e) `e`
</br>
</br>

f) `f`
</br>
</br>

g) `g`
</br>
</br>

+++

What is the type of 
</br>

h) `b`
</br>
</br>

i) `d`
</br>
</br>

j) `e`
</br>
</br>

k) `f`
</br>
</br>

```{code-cell}
# Catherine's solution
print(f"{a=}\n{b=}\n{c=}\n{d=}\n{e=}\n{f=}")

print(f"\n---------")
print(f"{np.shape(a)=}\n{np.shape(b)=}\n{np.shape(c)=}\n{np.shape(d)=}\n{np.shape(e)=}\n{np.shape(f)=}")

print(f"\n---------")
print(f"{type(b)=}\n{type(d)=}\n{type(e)=}\n{type(f)=}")
```

```{code-cell}
# Catherine's solution
# g = a*a.T

# If what we wanted was to do the matric multplication we would do
np.matmul(a,a.T)
# or use the @ matrix multiply operator
g = a@a.T
print(f"{g=}")
```

### Question 8:  More quickies

#### A) Bugs...
What happens when you run the following code?  

```{code-cell}
A=np.array([1, 5, 3, 0, 1])
B=np.array([0, 5, 6, 0, 1])
C=A/B + 4
```

#### B) More bugs...
What happens when you run the following code? 

```{code-cell}
A=[1, 5, 3, 0, 1]
B=[0, 5, 6, 0, 1]
try:
    C=B/A + 4
except TypeError as te:
    print(f"{te}")
```

#### C)
What does `x` contain after running the following code? show your work.

```{code-cell}
a = 3.0;
x = [2**a+a*2+1, a**(np.sum(np.append(np.arange(2,-1,-1),-4)))]
```

```{code-cell}
# Catherine's solution

print(x)
```