---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: md,ipynb
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---


# Week 08 Quiz: Functions basics -solution

## The following code calls a function "poly3" for which the code is given:

```{code-cell}
import numpy as np  # not needed in example below

def poly3(x):
    """ POLY3: Evaluates the cubic polynomial y = a0 + a1*x+a2*x**2+a3*x**3
    using Horner's method, where a0=1, a1=-1, a2=2, a3=1.
    """
    
    a0 = 1
    a1 = -1
    a2 = 2
    a3 = 1
    
    y = a0 + x*(a1 + x*(a2+x*a3))
    
    return y

myx = -2
new = poly3(myx)
```

1.  Identify the following elements of the code:

   Function name:  poly3
<br />
<br />

   Input argument(s): x
<br />
<br />

   Output argument(s): y
<br />
<br />

2.  After running the code what variables are in the workspace and what are the values of these variables?

<br />
<br />
myx = -2

new = 3
<br />
<br />
<br />


