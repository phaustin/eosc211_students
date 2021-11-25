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

# File IO

## EOSC 211

**Week 12 Day 2**

**Learning Objectives:** 

1. Convert python datatypes (arrays, datetime slices) into basic
   strings, lists, tuples, dicts that can be saved to a text file in json format
2. Write a function to open a json file and convert the file contents back
   into python objects.

+++

## Introduction

In this course we've usually started a worksheet or lab by reading a data file into python.  For example,
in [wk05_indexing](https://phaustin.github.io/eosc211_students/wk05/wk05_indexing.html) we used
`np.load` to read in a dictionary containing two numpy binary files containing the arrays `flux` and `temp`.
As I mentioned in that notebook, these files were written by  [np.savez](https://numpy.org/doc/stable/reference/generated/numpy.savez.html).  In [week 11](https://phaustin.github.io/eosc211_students/wk11/pythia_pandas.html) you used `pd.read_csv` to read in
a text file written in spreadsheet `comma separated value` format.  This [enso_data.csv](https://github.com/phaustin/eosc211_students/blob/e211_live_main/wk11/enso_data.csv) file was written
from a dataframe using [pandas.DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html).  

Writing binary numpy files and csv files from dataframes works: but there is a significant drawback,
you need numpy and some kind of spreadsheet to read the data.  How would you write a file
that any text editor or programming language could work with?

+++

## Background -- text vs. binary

What is the difference between a text file like `enso_data.csv` and a binary file like `temp_flux.npz`?  At the
machine level, there is no difference, like everything else on your computer, they consist only of a
long string of 1's and 0's.  The difference is in how a computer program interprets those 1's and 0's. 

In a text file, the 8 bit bytes are mapped to characters in a human language using a lookup table.
Python (and all modern programming languages) uses the [unicode character table](https://unicode-table.com/en/blocks/), which includes not only languages, but [math](https://unicode-table.com/en/blocks/mathematical-operators/), [emojis, musical notes and chess pieces](https://unicode-table.com/en/blocks/miscellaneous-symbols/) 

In a binary file, the bits are read into memory with no assumption about a mapping. You need to know
whether the bits were written as 64 bit floats, 32 bit ints, or 1 bit logical values.  This quickly gets
complicated -- there is a brief note about packages that write common binary data formats at the 
end of the worksheet.

+++

## A basic text file example

Here's basic  write of a numpy array to a text file using the folders we created in the week 11 lab.

```{code-cell} ipython3
from pathlib import Path
import numpy as np
myhome = Path.home()

# create the folder
text_dir = myhome / 'eosc211/week12'
text_dir.mkdir(parents=True, exist_ok=True)

# make some data and write it out
simple_vec = np.arange(3,40,2)
filename = text_dir / 'simplefile.txt'
with open(filename,'w') as outfile:
    for the_num in simple_vec:
        outfile.write(f"{the_num}\n")
```

The last block of code above uses `open` to open a file for writing (which will
overwrite anything that was already there) and then converts each floating point number into
a string and writes that to the file, including a newline `\n`.  The `with` statement
handles closing the file safely once you've left the `with context block`

Check that this works by launching a text editor to look at the file:

```
cd ~/eosc211/week12
start simplefile.txt  (for windows)
open simplefile.txt  (for macs)
```

or using the text file editor on our jupyterhub.

+++

## An easier way


That's quite a bit of work to write out a couple of numbers.  Python provides a variety of modules
that allow you to skip all this bookkeeping, as long as your data consists of basic python types:
`strings, lists, tuples, or dictionaries` and you want to save using a common format (like csv).
One very common general text file format is `json` (javascript object notation).  Here is the same
file written in json.  We'll try a 3-d array this time.  We need to first turn the array into
a list, then dump the list to the file using [json.dump](https://docs.python.org/3/library/json.html)

```{code-cell} ipython3
import json
#
# make a 3-d array
#
simple_vec = np.arange(0,100)
simple_vec = simple_vec.reshape(5,5,4)
#
# write out as a json list
#
json_file = text_dir / 'simplefile.json'
with open(json_file, 'w') as json_out:
    my_list = simple_vec.tolist()
    json.dump(my_list, json_out)
```

Take a look at that file, and double check that you can read it back in. Note that the
numpy `tolist` method correctly handles the nested rows, and the numpy `array` construct
correctly `round-trips` the list back to a numpy array.

```{code-cell} ipython3
with open(json_file) as json_in:
    new_vec = json.load(json_in)
new_vec = np.array(new_vec)
print(new_vec[:,:2,:2])
```

## Including metadata

You want to avoid writing out naked lists of raw numbers without extra information (called metadata) like
physical units, uncertainty estimates, etc.  You can do this with json using a dictionary that contains
your list along with other strings, lists and dictionaries if needed:

```{code-cell} ipython3
my_data = {}
my_data['units'] = 'deg C'
my_data['plot_title'] = "incubator temperature"
my_data['valid range'] = (-10,100)
my_data['missing_values'] = -999
my_data['comment']='first run incubator temperature test'
my_data['first_run'] = simple_vec.tolist()
```

```{code-cell} ipython3
meta_file = text_dir / 'metadata.json'
#
# indent 4 spaces
#
with open(meta_file,'w') as meta_out:
    json.dump(my_data, meta_out, indent=4)
```

Take a look at this file, and notice that the `indent=4` added nested spaces to make the various
levels more readable.  Since whitespace isn't significant in json files, those space will be ignored
when your read it back in:

```{code-cell} ipython3
with open(meta_file) as meta_in:
    new_dict = json.load(meta_in)
print(new_dict.keys())
```

## Summary

To write general data out to a text file you need to choose a text file format (we've seen csv and json, but
there are hundreds of different special formats) and then convert your data into datatypes that
the output file format can understand.  Since this is such a common task, almost all python objects have
some way to represent themselves as lists, dicts, or strings.

+++

## Question 1

Put the following items in a dictionary, and write that dictionary to a json file called
`parameters.json` in your week12 folder:

1) A list of 3 datetime objects -- with the key `the_dates`  
2) the start and stop values for a slice, with keys `start` and `stop`

One way to convert a datetime object into a string is to use the
[isoformat](https://docs.python.org/3/library/datetime.html) method.

```{code-cell} ipython3
# your code
```

## Question 2

Write a function called `process_params` that takes the filename (as a Path object) and returns a dictionary,
holding a list of datetime objects (dictionary key: `the_dates`) converted form their isoformat strings, and the
start and stop values converted to a slice object stored in dictionary key `the_slice`.  
The datetime module provides the function `datetime.datetime.fromisoformat`
to go from iso strings back to datetimes.

```{code-cell} ipython3
# your code
```

## Postscript: writing binary files

This is all fine for text files, but what if you need to write out 3 Mbytes of binary arrays?  Converting
all of that to and from text is a major waste of cpu time and disk space.   For this course, the choice would
be to write out an npz file, and accompanying that npz file with a json file holding whatever metadata
you want to include (especially the file name of the npz file, so you don't lose track).  Once you
get beyond this course however, it's good to know that there is common workflow. Specifically: 
we recommend the following steps:

1) Convert your numpy array to an [xarray Dataset](https://foundations.projectpythia.org/core/xarray/xarray.html)  
2) Use xarray to write out the data in a common binary format. The two most common binary data formats
   in the earth sciences are [netcdf](http://xarray.pydata.org/en/stable/generated/xarray.Dataset.to_netcdf.html)
   and [zarr](http://xarray.pydata.org/en/stable/generated/xarray.Dataset.to_zarr.html)
