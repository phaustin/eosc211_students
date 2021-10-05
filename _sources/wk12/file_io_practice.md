---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Practice with loops, if, strings,  file IO, logical indexing

## EOSC 211

**Week 11 Day 2**

**Learning Objectives:**  
1. Solve problems with python code
2. Choose appropriate data structures to make your code neat and efficient

<!-- #region -->
## Question 1

**You have a set of comma-separated value (csv) files containing pairs of measurements of magnetic field strength taken 20 times per second continuously.  The data are organized such that there is one file per day for every day in the year and each file contains two columns: time in seconds and magnetic field strength in nT.  You can call these variables TIME and BMAG.  Assume that the files are named as follows mag001.csv, mag002.csv … through to the file for Dec 31st, mag365.csv**

You want to do some analyses of data taken each day but only inside a time interval that is specific to each day.   e.g.,  you want to find the maximum magnetic field in a given time interval, and you want to output the day, the maximum field and the time (in seconds) at which this occurs, to a file called maxmag.out.  The time interval to be analyzed each day is given by a start time and end time that are kept in another file called crossings.dat. This has 3 columns of data:  the first contains the day-of-the-year i.e. 1 thru 365 (call this DOY), the second contains the start time (call this TIN) and 3rd contains the end time (call this TOUT) in seconds.


A.	First write down a procedure/algorithm for doing this.  Don’t write full matlab code – write a flow chart, or shorthand code or whatever works for you to map out your plan-of-attack…. Remember:  What are the inputs / outputs? What are the repetition / selection parts of this problem? 

HINT:  Often it helps to first solve a simpler problem – e.g. what if you had a data file for one day only?  Break the problem down into pieces and see if you can write the algorithm just for this one day of data.

<!-- #endregion -->

Cant decide how to approach this before having clear course objectives. I would do most of this with pandas (pd.read_csv('path/to/file.csv')) but this is an IO exercise. 
