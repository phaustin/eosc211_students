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
orig_nbformat: 4
---

<center><img src="https://github.com/pandas-dev/pandas/raw/master/web/pandas/static/img/pandas.svg" alt="pandas Logo" style="width: 800px;"/></center>

# Introduction to Pandas

+++

## Overview
1. Introduction to pandas data structures
1. How to slice and dice pandas dataframes and dataseries
1. How to use pandas for exploratory data analysis

## Credits

This notebook is part of the [Project Pythia foundations series](https://foundations.projectpythia.org/core/pandas/pandas.html) ([link to github repo](https://github.com/ProjectPythia/pythia-foundations)).  [LICENSE](https://github.com/ProjectPythia/pythia-foundations/blob/main/LICENSE)

* **Time to learn**: 60 minutes

+++

## Imports

+++

You will often see the nickname `pd` used as an abbreviation for pandas in the import statement, just like `numpy` is often imported as `np`.

```{code-cell} ipython3
:trusted: true

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
```

## The pandas [`DataFrame`](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe)...
... is a **labeled**, two dimensional columnal structure similar to a table, spreadsheet, or the R `data.frame`.

![dataframe schematic](https://github.com/pandas-dev/pandas/raw/master/doc/source/_static/schemas/01_table_dataframe.svg "Schematic of a pandas DataFrame")

The `columns` that make up our `DataFrame` can be lists, dictionaries, NumPy arrays, pandas `Series`, or more. Within these `columns` our data can be any texts, numbers, dates and times, or many other data types you may have encountered in Python and NumPy. Shown here on the left in dark gray, our very first `column`  is uniquely referrred to as an `Index`, and this contains information characterizing each row of our `DataFrame`. Similar to any other `column`, the `index` can label our rows by text, numbers, `datetime`s (a popular one!), or more.

## Sea surface temperature measurements

For this notebook we will be looking at temperature timeseries used to monitor the  El Niño Southern Oscillation (ENSO). The data are provided by  the US National Climatic Data Center.  You can read about the regions 
corresponding to the various sea surface temperatures (Nino12, Nino3 and Nino4) [at the NCDC website](https://www.ncdc.noaa.gov/teleconnections/enso/indicators/sst/).

[Here is an animation showing](https://drive.google.com/file/d/1Wf_FQglTU4fMZ5imAsHczAr0hcg4h1Ej/view?usp=sharing) the Southern Oscilation

We start by reading in the data, formated as comma separated values.  You can download the enso_data.csv file [at this dropbox link](https://www.dropbox.com/s/afxfi6a0odoyx9y/enso_data.csv?dl=0).  If you are on our jupyterhub, it will
already be in the same folder as this notebook.

```{code-cell} ipython3
:trusted: true

filepath = "enso_data.csv"
df = pd.read_csv(filepath)
```

If we print out our dataframe, you will notice that is text based, which is okay, but not the "best" looking output.  All numbers are temperatures in deg Celsius.  "anom" is short for anomaly, which is defined as the
fluctuation about the mean.

```{code-cell} ipython3
:trusted: true

print(df)
```

If we just use the pandas dataframe itself (without wrapping it in `print`), we have a nicely rendered table which is native to pandas and Jupyter Notebooks. See how much nicer that looks?

```{code-cell} ipython3
:trusted: true

df
```

The `index` within pandas is essentially a list of the unique row IDs, which by default, is a list of sequential integers which start at 0

```{code-cell} ipython3
:trusted: true

df.index
```

Our indexing column isn't particularly helpful currently. Pandas is clever! A few optional keyword arguments later, and...

```{code-cell} ipython3
:trusted: true

df = pd.read_csv(filepath, index_col=0, parse_dates=True)

df
```

```{code-cell} ipython3
:trusted: true

df.index
```

... now we have our data helpfully organized by a proper `datetime`-like object. Each of our multiple columns of data can now be referenced by their date! This sneak preview at the pandas `DatetimeIndex` also unlocks for us much of pandas most useful time series functionality. Don't worry, we'll get there. What are the actual columns of data we've read in here?

```{code-cell} ipython3
:trusted: true

df.columns
```

## The pandas [`Series`](https://pandas.pydata.org/docs/user_guide/dsintro.html#series)...

... is essentially any one of the columns of our `DataFrame`, with its accompanying `Index` to provide a label for each value in our column.

![pandas Series](https://github.com/pandas-dev/pandas/raw/master/doc/source/_static/schemas/01_table_series.svg "Schematic of a pandas Series")

The pandas `Series` is a fast and capable 1-dimensional array of nearly any data type we could want, and it can behave very similarly to a NumPy `ndarray` or a Python `dict`. You can take a look at any of the `Series` that make up your `DataFrame` with its label and the Python `dict` notation, or with dot-shorthand:

```{code-cell} ipython3
:trusted: true

df["Nino34"]
```

<div class="alert alert-block alert-info">
<b>Tip:</b> You can also use the `.` (dot) notation, as seen below, but this is moreso a "convenience feature", which for the most part is interchangeable with the dictionary notation above, except when the column name is not a valid Python object (ex. column names beginning with a number or a space)</div>

```{code-cell} ipython3
:trusted: true

df.Nino34
```

## Slicing and Dicing the `DataFrame` and `Series`

We will expand on what you just saw, soon! Importantly,

> **Everything in pandas can be accessed with its label**,

no matter how your data is organized.

+++

### Indexing a `Series`

Let's back up a bit here. Once more, let's pull out one `Series` from our `DataFrame` using its column label, and we'll start there.

```{code-cell} ipython3
:trusted: true

nino34_series = df["Nino34"]

nino34_series
```

`Series` can be indexed, selected, and subset as both `ndarray`-like,

```{code-cell} ipython3
:trusted: true

nino34_series[3]
```

and `dict`-like, using labels

```{code-cell} ipython3
:trusted: true

nino34_series["1982-04-01"]
```

These two can be extended in ways that you might expect,

```{code-cell} ipython3
:trusted: true

nino34_series[0:12]
```

<div class="admonition alert alert-info">
    <p class="admonition-title" style="font-weight:bold">Info</p>
    Index-based slices are <b>exclusive</b> of the final value, similar to Python's usual indexing rules.
</div>

+++

as well as potentially unexpected ways,

```{code-cell} ipython3
:trusted: true

nino34_series["1982-01-01":"1982-12-01"]
```

That's right, label-based slicing! Pandas will do the work under the hood for you to find this range of values according to your labels.

+++

<div class="admonition alert alert-info">
    <p class="admonition-title" style="font-weight:bold">Info</p>
    label-based slices are <b>inclusive</b> of the final value, different from above!
</div>

+++

If you are familiar with [xarray](../xarray), you might also already have a comfort with creating your own `slice` objects by hand, and that works here!

```{code-cell} ipython3
:trusted: true

nino34_series[slice("1982-01-01", "1982-12-01")]
```

### Using `.iloc` and `.loc` to index

Let's introduce pandas-preferred ways to access your data by label, `.loc`, or by index, `.iloc`. They behave similarly to the notation introduced above, but provide more speed, security, and rigor in your value selection, as well as help you avoid [chained assignment warnings](https://pandas.pydata.org/docs/user_guide/indexing.html#returning-a-view-versus-a-copy) within pandas.

```{code-cell} ipython3
:trusted: true

nino34_series.iloc[3]
```

```{code-cell} ipython3
:trusted: true

nino34_series.iloc[0:12]
```

```{code-cell} ipython3
:trusted: true

nino34_series.loc["1982-04-01"]
```

```{code-cell} ipython3
:trusted: true

nino34_series.loc["1982-01-01":"1982-12-01"]
```

### Extending to the `DataFrame`

These capabilities extend back to our original `DataFrame`, as well!

```{code-cell} ipython3
:tags: [raises-exception]
:trusted: true

df.loc["1982-01-01"]
```

They do! Importantly however, indexing a `DataFrame` can be more strict. A DataFrame has both rows and columns,
and pandas needs to know that you are asking for a row, which is why you need to access the row label by
using the `.loc` index.  If you give the DataFrame a single index, it will assume that you are asking
for a column (the default) and not a row.

```{code-cell} ipython3
:trusted: true

df["Nino34"]
```

You can also retrieve a row by its row number, but again, to remove the ambiguity between index labels (.loc)
and row numbers, you need to use the `.iloc` locater.

```{code-cell} ipython3
:tags: [raises-exception]
:trusted: true

df.iloc[0]
```

Knowing now that we can pull out one of our columns as a series with its label, plus our experience interacting with the `Series` `df["Nino34"]` gives us, we can chain our brackets to pull out any value from any of our columns in `df`.

```{code-cell} ipython3
:trusted: true

df["Nino34"]["1982-04-01"]
```

```{code-cell} ipython3
:trusted: true

df["Nino34"][3]
```

However, this is not a pandas-preferred way to index and subset our data, and has limited capabilities for us. As we touched on before, `.loc` and `.iloc` give us more to work with, and their functionality grows further for `df`.

```{code-cell} ipython3
:trusted: true

df.loc["1982-04-01", "Nino34"]
```

<div class="admonition alert alert-info">
    <p class="admonition-title" style="font-weight:bold">Info</p>
    Note the <code>[<i>row</i>, <i>column</i>]</code> ordering!
</div>

+++

These allow us to pull out entire rows of `df`,

```{code-cell} ipython3
:trusted: true

df.loc["1982-04-01"]
```

```{code-cell} ipython3
:trusted: true

df.loc["1982-01-01":"1982-12-01"]
```

```{code-cell} ipython3
:trusted: true

df.iloc[3]
```

```{code-cell} ipython3
:trusted: true

df.iloc[0:12]
```

Even further,

```{code-cell} ipython3
:trusted: true

df.loc[
    "1982-01-01":"1982-12-01",  # slice of rows
    ["Nino12", "Nino3", "Nino4", "Nino34"],  # list of columns
]
```

### Indexing summary

Here are some rules of thumb for all of these different ways of indexing into a pandas
dataframe:


1.  Use informative index labels for rows and columns if possible.  It's very
    useful to be able to write:

```{code-cell} ipython3
:trusted: true

df.loc["1982-01-01":"1982-5-01","Nino34"]
```

This is self-documenting, does the datetime to row number conversion for you,
and relieves you of worrying about what happens to the row and column
numbers if you add more dates (say a year before 1982) or additional columns, removing
a large number of potential bugs.

+++

2. Prefer `df.loc["1982-01-01":"1982-5-01","Nino34"]` to

   `df["Nino34"]["1982-01-01":"1982-5-01"]`
   
   Both statements return the same data frame, but the second version fetches the entire
   column, then gets the rows from that column.  This results in a 
   column,row indexing order that is reversed from
   the usual numpy row-major array indexing of row,column -- a potential source of confusion.

+++

3. Use iloc only when you have to

So given the two points above, why does pandas have iloc?  This is to cover a situation like
this: suppose you need to return a new dataframe with the 10 warmest Nino34 temperatures.  To do that you need 
to be able to access the sorted rows by number:

```{code-cell} ipython3
:trusted: true

#
# sort in descending order
#
sorted_df = df.sort_values('Nino34',axis=0,ascending=False)
#
# get the top five temperatures, all columns
#
big_temps = sorted_df.iloc[:5,:]
big_temps
```

<div class="admonition alert alert-info">
    <p class="admonition-title" style="font-weight:bold">Info</p>
    For a more comprehensive explanation, which includes additional examples, limitations, and compares indexing methods between DataFrame and Series see <a href="https://pandas.pydata.org/docs/user_guide/indexing.html">pandas' rules for indexing.</a>
</div>

+++

## Exploratory Data Analysis

### Get a Quick Look at the Beginning/End of your `Dataframe`
Pandas also gives you a few shortcuts to quickly investigate entire `DataFrame`s.

```{code-cell} ipython3
:trusted: true

df.head()
```

```{code-cell} ipython3
:trusted: true

df.tail()
```

### Quick Plots of Your Data
A good way to explore your data is by making a simple plot. Pandas allows you to plot without even calling `matplotlib`! Here, we are interested in the `Nino34` series. Check this out...

```{code-cell} ipython3
:trusted: true

ax0 = df.Nino34.plot(label='Nino34')
```

Since we've kept the matplotlib axis handle returned by pandas, we can customize it and redraw
the figure:

```{code-cell} ipython3
:trusted: true

ax0.set(ylabel='temperature (degC)')
ax0.grid(True)
ax0.legend(loc='lower right')
display(ax0.figure)
```

Before, we called `.plot()` which generated a single line plot. This is helpful, but there are other plots which can also help with understanding your data! Let's try using a histogram to understand distributions...

The only part that changes here is we are subsetting for just two `Nino` indices, and after `.plot`, we include `.hist()` which stands for histogram

```{code-cell} ipython3
:trusted: true

axhist = df[['Nino12', 'Nino34']].plot.hist()
axhist.set(xlabel='temperature (degC)');
```

We can see some clear differences in the distributions, which is helpful! Another plot one might like to use would be a `boxplot`. Here, we replace `hist` with `box`

```{code-cell} ipython3
:trusted: true

df[['Nino12', 'Nino34']].plot.box();
```

Here, we again see a clear difference in the distributions. These are not the only plots you can use within pandas! For more examples of plotting choices, check out [the pandas plot documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)

+++

#### More on customizing your plot -- use an existing figure with plt.subplots

Pandas DataFrame `plot()` methods are just wrappers around matplotlib, so you always have the option to use matlplotlib directly
instead of calling it through pandas.  Suppose you want the Nino34 graph to be one of four separate plots
in a figure?  In that case, you can create a 2 x 2 set of axes with `plt.subplots`, 
and pass that axis to use:

```{code-cell} ipython3
:trusted: true

fig, ax1 = plt.subplots(1,1, figsize=(8,6))
#
# pass dataframe an existing matplotlib axis to draw on
#
df.Nino34.plot(ax=ax1,color='black',linewidth=2)
ax1.set(xlabel='Year',
       ylabel = 'ENSO34 Index (degC)',label='Nino34')
ax1.legend(loc='lower right')
ax1.grid(True);
```

Alternatively, from matplotlib you can plot the dataframe in an axis using the matplotlib `data` keyword:

```{code-cell} ipython3
:trusted: true

fig, ax2 = plt.subplots(1,1, figsize=(8,6))
#
# any dictionary-like object with keys and data will
# work here, if it's passed using the data keyword and
# the key is in the dicitonary
#
ax2.plot('Nino34',data = df);
ax2.set(xlabel='Year',
       ylabel = 'ENSO34 Index (degC)',label='Nino34')
ax2.legend(loc='lower right')
ax2.grid(True)
```

**Bottom line**:  Do you want pandas or matplotlib to be in control of your plotting?  We've shown you multiple
ways to plot a figure.

1. Simplest -- pandas.DataFrame.plot(), put pandas in control of your figure and axis.

2. More flexible -- have matplotlib control the figure and axis, and pass that axis to pandas for plotting using the `ax` keyword in pandas.DataFrame.plot()

3. Matplotlib in control -- pass the DataFrame to the ax.plot function directly using the `data` keyword in matlotlib.axis.plot()

Which to choose depends on how much customization you need -- using pandas plot functions
may be easier, but they also add an extra layer on top of matplotlib that could potentially make your
code more opaque.

+++

Next: graphs are a great way to get a feel for your data, but what if you wanted a more ***quantitative*** perspective? We can use the `describe` method on our `DataFrame`; this returns a table of summary statistics for all columns in the `DataFrame`

### Basic Statistics

By using the `describe` method, we see some general statistics! Notice how calling this on the dataframe returns a table with all the `Series`

```{code-cell} ipython3
:trusted: true

df.describe()
```

You can look at specific statistics too, such as mean! Notice how the output is a `Series` (column) now

```{code-cell} ipython3
:trusted: true

df.mean()
```

If you are interested in a single column mean, subset for that and use `.mean`

```{code-cell} ipython3
:trusted: true

df.Nino34.mean()
```

### Subsetting Using the Datetime Column

You can use techniques besides slicing to subset a `DataFrame`. Here, we provide examples of using a couple other options.

Say you only want the month of January - you can use `df.index.month` to query for which month you are interested in (in this case, 1 for the month of January)

```{code-cell} ipython3
:trusted: true

# Uses the datetime column
df[df.index.month == 1].head()
```

You could even assign this month to a new column!

```{code-cell} ipython3
:trusted: true

df['month'] = df.index.month
```

Now that it is its own column (`Series`), we can use `groupby` to group by the month, then taking the average, to determine average monthly values over the dataset

```{code-cell} ipython3
:trusted: true

df.groupby('month').mean().plot();
```

#### Pandas style hint:  method chaining

The cell above "chains" two methods (mean and plot) together, without creating an intermediate result.  It's equivalent to:

```{code-cell} ipython3
:trusted: true

month_groups = df.groupby('month')
month_mean = month_groups.mean()
the_axis = month_mean.plot()
```

It's very common in pandas to see chained methods written  one methoc per line-- can you explain why this works?

```{code-cell} ipython3
:trusted: true

the_ax = (df.groupby('month')
          .mean()
          .plot())
```

#### Your turn

Add a grid, title and a yaxis label to this plot using the `the_ax` axis.  See the [matplotlib gallery](https://matplotlib.org/stable/gallery/index.html) for some examples.

+++

### Turning a groupby result into a dictionary



Here is an incantation that turns a groupby object into a dictionary:

```{code-cell} ipython3
:trusted: true

month_groups = df.groupby('month')
month_groups = dict(tuple(month_groups))
month_groups.keys()
```

#### Your turn

What steps would you take to figure out why `dict(tuple(month_groups))` works the way it does?  Here's a good
[overview of dicitionaries](https://realpython.com/iterate-through-dictionary-python/)

+++

### Investigating Extreme Values

+++

You can also use ***conditional indexing***, such that you can search where rows meet a certain criteria. In this case, we are interested in where the Nino34 anomaly is greater than 2

```{code-cell} ipython3
:trusted: true

df[df.Nino34anom > 2]
```

You can also sort columns based on the values!

```{code-cell} ipython3
:trusted: true

df.sort_values('Nino34anom')
```

Let's change the way that is ordered...

```{code-cell} ipython3
:trusted: true

df.sort_values('Nino34anom', ascending=False)
```

### Resampling
Here, we are trying to resample the timeseries such that the signal does not appear as noisy. This can helpfule when working with timeseries data! In this case, we resample to a yearly average (`1Y`) instead of monthly values

```{code-cell} ipython3
:trusted: true

df.Nino34.plot();
```

#### Your turn

How would you plot the original timeseries on top of the one year resample?

+++

### Applying operations to a dataframe

Often times, people are interested in applying calculations to data within pandas `DataFrame`s. Here, we setup a function to convert from degrees Celsius to Kelvin

```{code-cell} ipython3
:trusted: true

def convert_degc_to_kelvin(temperature_degc):
    """
    Converts from degrees celsius to Kelvin
    """

    return temperature_degc + 273.15
```

Now, this function accepts and returns a single value

```{code-cell} ipython3
:trusted: true

# Convert a single value
convert_degc_to_kelvin(0)
```

But what if we want to apply this to our dataframe? We can subset for Nino34, which is in degrees Celsius

```{code-cell} ipython3
:trusted: true

nino34_series
```

Notice how the object type is a pandas series

```{code-cell} ipython3
:trusted: true

type(df.Nino12[0:10])
```

If you call `.values`, the object type is now a numpy array. Pandas `Series` values include numpy arrays, and calling `.values` returns the series as a numpy array!

```{code-cell} ipython3
:trusted: true

type(df.Nino12.values[0:10])
```

Let's apply this calculation to this `Series`; this returns another `Series` object.

```{code-cell} ipython3
:trusted: true

convert_degc_to_kelvin(nino34_series)
```

If we include `.values`, it returns a `numpy array`

+++

<div class="admonition alert alert-warning">
    <p class="admonition-title" style="font-weight:bold">Warning</p>
    We don't usually recommend converting to NumPy arrays unless you need to - once you convert to NumPy arrays, the helpful label information is lost... so beware! 
</div>

```{code-cell} ipython3
:trusted: true

convert_degc_to_kelvin(nino34_series.values)
```

We can now assign our pandas `Series` with the converted temperatures to a new column in our dataframe!

```{code-cell} ipython3
:trusted: true

df['Nino34_degK'] = convert_degc_to_kelvin(nino34_series)
```

```{code-cell} ipython3
:trusted: true

df.Nino34_degK
```

Now that our analysis is done, we can save our data to a `csv` for later - or share with others!

```{code-cell} ipython3
:trusted: true

df.to_csv('nino_analyzed_output.csv')
```

```{code-cell} ipython3
:trusted: true

pd.read_csv('nino_analyzed_output.csv', index_col=0, parse_dates=True)
```

## Summary
* Pandas is a very powerful tool for working with tabular (i.e. spreadsheet-style) data
* There are multiple ways of subsetting your pandas dataframe or series
* Pandas allows you to refer to subsets of data by label, which generally makes code more readable and more robust
* Pandas can be helpful for exploratory data analysis, including plotting and basic statistics
* One can apply calculations to pandas dataframes and save the output via `csv` files


## Resources and References
1. [NOAA NCDC ENSO Dataset Used in this Example](https://www.ncdc.noaa.gov/teleconnections/enso/indicators/sst/)
1. [Software carpentry pandas lesson](https://swcarpentry.github.io/python-novice-gapminder/08-data-frames/index.html)
1. [Getting Started with Pandas](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)
1. [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)
1. [Modern Pandas](https://tomaugspurger.github.io/modern-1-intro)
1. [Python dictionaries](https://realpython.com/iterate-through-dictionary-python/)
1. [Matplotlib gallery](https://matplotlib.org/stable/gallery/index.html)
