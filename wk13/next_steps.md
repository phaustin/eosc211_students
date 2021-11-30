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

# Next steps

## Where to From Here?

We have reached the end of E211! We sincerely hope that you enjoyed the course, and gained some valuable skills to help you throughout the rest of your career at UBC and in the Earth Sciences.  

Below are a series of links and suggestions to help you continue building your coding skills beyond what we were able to cover in a single semester.

+++

## Python continuing education

How do you move from the course exercises we've been through to real-world programming in python?  The
main thing is to continue to write code, and read code others have written.   Some useful links:

* [Project Pythia](https://projectpythia.org/index.html#start-learning)  -- this website is hosted by the 
  [NCAR](https://ncar.ucar.edu/) to get scientists started in python programming for earth sciences applications
  
* [University of Helsinki Geopython course](https://geo-python-site.readthedocs.io/en/latest/) -- well organized
  with an emphasis on GIS remote sensing.
  
* [University of Colorado Earth Lab](https://www.earthdatascience.org/) -- lot's of remote sensing/GIS tutorials in python and R

## Python at UBC 

* [ATSC 409](https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=ATSC&course=409) -- Numerical methods

* [ATSC 301: Remote Sensing](https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=ATSC&course=301) -- offered January 2023.  Python based GIS/satellite remote sensing

* Courses in the [UBC Data Science minor](https://datascience.ubc.ca/minor)

## Developing Your Own Coding Workflow

### VScode and Other IDE's

In this course we relied exclusively on Jupyter notebooks and related infrastructure, chosen for simplicity, ease of use, and popularity in the research community. If you want a more fully-featured, customizable *integrated development environment* (IDE), you might consider using VScode or Spyder. With more complex IDE's you can add extentions like [variable explorers](https://visualstudiomagazine.com/articles/2019/04/24/vs-code-python-update.aspx), [debugging tools](https://code.visualstudio.com/docs/python/debugging), [version-control](https://code.visualstudio.com/docs/editor/github), [automatic code formatters](https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0) and more. You can also configure VScode to look and feel [very much like a jupyter notebook](https://code.visualstudio.com/docs/datascience/jupyter-notebooks). How you develop and manage your coding workflow is largely a matter of personal taste; You can write code with anything from a simple text editor to a super tricked-out IDE that took you years to configure.  

### Git/Github

For those interested in pursuing scientific programming as a career, we highly recommend incorporating Git into your programming flow. Git is a *version control system*, designed to allow you to backup many versions of your code as you develop more complex projects, as well as efficiently collaborate with teammates without making a mess (this is how 2 professors and 3 TA's manage all the material for a programming course). Profficiently using Git is a super useful skill sought after by employers -- if you are interested in learning more, send [Andrew](aloeppky@eoas.ubc.ca) an email, as he will be creating a series of tutorials on *git for earth science students and researchers* in the spring '22 semester.

>[git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - Version control software that lives in your computer and keeps track of changes to your code

>[github](https://github.com/) - An online platform designed for collaboratively developing *open source* code

### Other Programming Languages

Python is one of many high-level programming languages commmonly used today (currently the *most* commonly used). Either by choice or necessity, you may find yourself in the future needing to expand your horizons and work in another language. Learning a second programming language is much easier than the first, as they all tend to have much in common. Every language defines a number of data types, logical flow control statements, loops, etc.

* [Julia](https://julialang.org/) -- a high peformance scripting language that's fast enough to use for [Earth System Modelling](https://clima.github.io/ClimateMachine.jl/latest/)

* [R](https://education.rstudio.com/) -- the native language of most statisticians.  Used at UBC for DSCI 100 and all other stats courses.

* [Numba](https://numba.pydata.org/numba-doc/latest/user/5minguide.html) -- probably the easiest way to make python code go faster.

* [Cython](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html). Cython is a bridge to C and C++ in python.

* [Fortran](https://fortran-lang.org/)  -- Created in 1957, this is the one of the first programming languages, and still the dominate language for climate modeling work on supercomputers.

* [Rust](https://www.rust-lang.org/learn/get-started) -- A new language which can be used to accelerate python code via the [PyO3](https://pyo3.rs/v0.15.1/) module

* [Matlab](https://www.mathworks.com/) - Commonly used for engineering applications, syntactically very similar to Python. Free License through UBC

  * [Get a UBC license for MATLAB](https://it.ubc.ca/services/desktop-print-services/software-licensing/matlab)

+++

## Useful Python Packages for Geosciences

More stuff we wish we had time to cover in EOSC 211:

[Maintaining a Conda Environment](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c) - This is an important skill in Python programming. It is good practice to create separate coding environments for each project, and keep your environments as simple as possible (but not any simpler). Well-maintained environments lead to fewer bugs. Here is a [conda cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

[Scipy](https://scipy.org/) - Hardcore math stuff. Analytical equation solvers, linear algebra, statistics

```
$ conda install scipy
```

[Scikit-Learn](https://scikit-learn.org/stable/index.html) - Neural networks and machine learning models for novice programmers

```
$ conda install scikit-learn
```

[Xarray](http://xarray.pydata.org/en/stable/) - like Pandas, but for dense numpy arrays extended to 3D and beyond. Great for handling things like NetCDF data and displaying  Meteorological and Oceanographic vector fields. 

```
$ conda install -c conda-forge xarray dask netCDF4 bottleneck
```

[Geopandas](https://geopandas.org/en/stable/) - Like Pandas, but with expanded functionality to work with geographical information systems (GIS) data: KML, KMZ, shp, etc files can all be processed with Python. (I much prefer this approach over a graphical program like Qgis)

```
$ conda install -c conda-forge geopandas
```
