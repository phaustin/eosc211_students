
# Week 08 Quiz: Functions basics

### The following code calls a function "poly3" for which the code is given:

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

3.  What helpful information is missing in the doc string?

<br />
<br />
<br />
<br />

```{code-cell}
print(f'myx = {myx} and has type {type(myx)}')
print(f'new = {new} and has type {type(new)}')
```

    myx = -2 and has type <class 'int'>
    new = 3 and has type <class 'int'>


```{code-cell}
# this command lists the variables in my workspace
%who

# np and poly 3 are the packages and function respectively so I was just looking for myx and new
```

    myx	 new	 np	 poly3	 


```{code-cell}
# so e.g. a0 is not here and if I type the following i will get an error
print(a0)
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    /var/folders/4r/t59g43td3c38d4338mgslkwh0000gr/T/ipykernel_4471/3057198155.py in <module>
          1 # so e.g. a0 is not here and if I type the following i will get an error
    ----> 2 print(a0)
    

    NameError: name 'a0' is not defined


### Better docstring
```
    """ POLY3: Evaluates the cubic polynomial y = a0 + a1*x+a2*x**2+a3*x**3
    using Horner's method, where a0=1, a1=-1, a2=2, a3=1.
    
    INPUTS: x  (type = int or float)
    OUTPUTS: y  (type = int or float)
    """
```
