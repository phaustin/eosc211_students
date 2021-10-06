---
celltoolbar: Create Assignment
jupytext:
  cell_metadata_filter: all
  formats: ipynb,md:myst
  notebook_metadata_filter: all
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
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
  version: 3.8.12
nbsphinx:
  execute: never
toc:
  base_numbering: 1
  nav_menu: {}
  number_sections: true
  sideBar: true
  skip_h1_title: false
  title_cell: Table of Contents
  title_sidebar: Contents
  toc_cell: true
  toc_position:
    height: calc(100% - 180px)
    left: 10px
    top: 150px
    width: 182px
  toc_section_display: true
  toc_window_display: true
---

- **Name:**
- **Student number:**

+++

**Instructions**:  The five items on this page show the python code in individual cells in a  jupyter notebook.  For each of the five, write down what the cell would display if you ran it.

+++

# Week 3 quiz

## numpy arrays

* Q1)


      the_list=[4,7,10]
      the_list*2

$~~~~~~~~~$

+++

* Q2)

      import numpy as np
      the_list=np.array([4,7,10])
      the_list*2

+++

* Q3)

       a=np.array([[1,2,3],[4,5,6],[7,8,9]])
       a[1,:]

+++

* Q4)


       a=np.array([[1,2,3],[4,5,6],[7,8,9]])
       a[:,1]=9
       a

+++

* Q5) 

       a=np.array([[1,2,3],[4,5,6],[7,8,9]])
       b = -a
       a[:,1]=b[2,:]
       a
