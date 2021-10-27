---
jupytext:
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

# Lab Week 8

+++

**Objectives:** This week's lab is about writing code that is reuseable, efficient and well-organized. How do we do this? Functions! The objective here is to take code from week 6 and re-package it in a better, more pythonic style. We will then test the code with a couple of datasets for the lab to make sure it can handle a range of input types and user-specified parameters, while still getting the right answer.

As an example of how we can reuse code, you will use what you write for this lab as a core function for assignment 1.

Datasets for this lab can be downloaded by clicking on the file names at:  https://github.com/phaustin/eosc211_students/tree/e211_live_main/wk08

+++

### As always, first import the packages you'll need

```{code-cell} ipython3
from e211_lib import e211
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: c95b19f7f7b1ef3f8fdac3e12e7a209f
  grade: false
  grade_id: cell-0f1bebfd15ae4946
  locked: false
  schema_version: 3
  solution: true
  task: false
---
# your posix_to_datetime function will go here (see below for details)

#
#  Remember to comment out the NotImplementedError exception from all the cells you need
#  to fill in.  Check to make sure your notebook runs cleanly before you upload to canvas
#

# YOUR CODE HERE
raise NotImplementedError()
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 93758c2ece8733d895ce25dd90048543
  grade: false
  grade_id: cell-0240c3fb29bf120a
  locked: false
  schema_version: 3
  solution: true
  task: false
---
# IN THIS CELL DEFINE TWO FUNCTIONS WITH THE FOLLOWING NAMES AND SIGNATURES

# check_inputs(winlen) return winlen

# running_mean(data, winlen) return running mean

# YOUR CODE HERE
raise NotImplementedError()
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: bc1fab99efa9e416f21cf21f7dfb4478
  grade: false
  grade_id: cell-5f6db024bb9d6991
  locked: false
  schema_version: 3
  solution: true
  task: false
---
# IN THIS CELL DEFINE YOUR RUNNING MEDIAN FUNCTION WITH THIS NAME AND SIGNATURE
#
# running_median(data, winlen=7)
# YOUR CODE HERE
raise NotImplementedError()
```

### Now get some data sets.  
Remind yourself of np.load and what `.npz` files contain from the week 6 lab. Also review the week 6 lab to remind yourself about datetime objects are and how to import dates/times into a numpy array of datetime objects.

```{code-cell} ipython3
# get the aircraft data again -- copy from week 6 solution
aircraft_gps = np.load("aircraft_gps.npz")
vel = aircraft_gps["vel"]
time = aircraft_gps["time"]

# very similar for a file with temperatures from Sand Heads, BC
sand_heads = np.load("sand_heads_temps.npz")
temp = sand_heads["temp"]
sand_time = sand_heads["time"]
```

### Setting up your first function
First define a function called `posix_to_datetime` that takes as input an array of POSIX times and returns a variable `dt` that is a numpy array of datetime objects.  To help you get started the function declaration line and the return statement are provided.  Complete the rest of the fucntion code, making sure to include the docstring.  The structure of your function will look something like this:  

```
def posix_to_datetime(time_array):
    """
    <docstring>
    """
    
    <function body code>
    
    return dt
```
Remember that any functions in your code need to be defined *before* they are used.  So they go at the top of your file, after importing the packages.

+++

### Testing your function
You can save yourself a lot of time by testing pieces of your code as you go along.  Test your `posix_to_datetime` function by loading the data sets, calling it and making test plots of each of the two data sets.  e.g., my test plot was made after calling posix_to_datetime, assigning the output to a variable called `fly_time` and making a plot with these code lines.
```
# quick and dirty plot to check everything is working ok
plt.plot(fly_time, vel)
plt.xlabel('time [units]')  # reminding myself to always include units
plt.xticks(rotation=70)     # rotate dates by 70 degrees so they don't overlap
plt.ylabel('vel [units]');  #add semicolon to suppress output
```

+++

### Running mean and running median functions
Now take your running mean code from the week6 lab and turn it into a function called `running_mean`.  If your week6 lab code did not work, you can use the solution posted on the course web page under week 6. `running_mean` should take as INPUT arguments `data` (the numpy array of data on which the running mean is to be performed) and `winlen` (the number of points in the running mean window) **in that order**. It should return a variable `z` that contains the running mean values.

Likewise take your running median code from the week6 lab and turn it into a function called `running_median` that takes as INPUT arguments `data` and `winlen` (again, in that order) and returns a variable `zm` that contains the running median values.

Again, test your functions by
1. calling them 
2. plotting the raw data and the running mean/median to check it all looks reasonable

+++

### Adding input parameter check
Now write code that will check that the window length is an odd number, and if it is not add 1 to the length and print a message to the screen informing the user the value of the window length that was passed in, the fact that it was even and the value that it has been corrected to.  Put this code in a function called `check_inputs` that takes as input `winlen`.  It must also return `winlen` either unmodified if it is odd, or modified if it is even.

Both the running mean and running median functions should call the `check_inputs` function. 
You can call functions from other functions, you just need to (a) keep track of which variables are passed where, and (b) scope (discussed in class).

Make sure to rerun your code that calls the running mean and running median to check (a) you didn't break anything, and (b) that `check_inputs` works.

+++

### What to turn in

1) define your posix_to_datetime in cell 2 (remove the exceptions in all fill-in cells)

2) define your check_inputs and running_mean functions in cell 3

3) define  your running_median function in cell 4 

Make sure your running_median function works when you test it by executing
code roughly similar to the cell below
for either the `aircraft` data set or the `temperature` dataset.  We will run
code similar to this, with a variety of window sizes and data sets.

+++

```
def main(data,tt):
    time=posix_to_datetime(tt)
    windows = choose some windows
    check various window sizes:
        filtered_data = running_median ...
        #
        # overlay the filtered data on the raw data
        #
        plt.plot(time,data,time,filtered_data)
        plt.xlabel('time')
        plt.xticks(rotation=70)
        plt.ylabel('y values')
        plt.show()
        
main(vel,time)
```

+++

## A quick sanity check

This code shows the raw data

```{code-cell} ipython3
# Sands Heads data
temp_time = posix_to_datetime(sand_time)

# quick and dirty plot to check everything is working ok
plt.plot(temp_time, temp)
plt.xlabel('time [units]')
plt.xticks(rotation=70)
plt.grid(True)
plt.ylabel('temperature [units]');   # I added semi-colon to suppress text output
```

The cell below tests window length 32 for the velocity data and 
compares the result at index = 231 with the answer we got with our
own running_median filter

```{code-cell} ipython3
import numpy.testing as nt
window=32
vel_median_filtered = running_median(vel, window)
testval = vel_median_filtered[231]
nt.assert_allclose(testval,1.95,rtol=1.e-2)
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: c6c8cae1ae106ee735375b3f9d497291
  grade: true
  grade_id: cell-70b0c8801298e72c
  locked: false
  points: 4
  schema_version: 3
  solution: true
  task: false
---
# You don't need to enter anything here  -- we have hidden the
# code we will use to check your functions in this cell
# Just comment out the exception so your notebook will run

# YOUR CODE HERE
raise NotImplementedError()
```
