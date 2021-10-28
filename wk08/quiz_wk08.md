

# Week 08 Quiz: Functions basics

### The following code calls a function "poly3" for which the code is given:

```{code-cell}
import numpy as np

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

   Function name:
<br />
<br />

   Input argument(s):
<br />
<br />

   Output argument(s):
<br />
<br />

2.  After running the code what variables are in the workspace and what are the values of these variables?

<br />
<br />
<br />
<br />
<br />

3.  What helpful information is missing in the docstring?
