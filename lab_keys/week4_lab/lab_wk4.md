---
celltoolbar: Create Assignment
jupytext:
  cell_metadata_filter: all
  formats: ipynb,md:myst
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Lab Week 4

## EOSC 211

### Learning Objectives:

1. Do math with python! 

2. Write structured code following input-process-output procedure

3. Develop code with the scaffolding technique 

4. More plots!

```{code-cell} ipython3
import numpy as np
from matplotlib import pyplot as plt 
import numpy.testing as testing
```

## Part 1: Computer Math and Writing Stylish Code (Tutorial)

+++

Below are the hydrostatic equations. They relate *atmospheric pressure* and *density* to height above sea level. The pressure and air density conditions we measure at the surface are due to the weight of the atmosphere above being pulled down by Earth's gravity. As we move higher into the atmosphere, there is less air above us (less weight pushing down), so the pressure decreases, as does the density (less pressure = less force squeezing the air molecules together). For air pressure $P$, we can express this as a mathematical function:

$$
P = P_0\cdot e^{-(a_P/T)\cdot z}\tag{Stull 1.9a†}
$$

similarly for density $\rho$ (represented by the greek letter *rho*):

$$
\rho = \rho_0\cdot e^{-(a_\rho/T)\cdot z}\tag{Stull 1.13a†}
$$

where $a_P=0.0342 K/m$ and $a_\rho=0.040K/m$ are constants. The average value for pressure and air density at sea level are $P_0=101325 Pa$, and $\rho_0=1.225kg/m^3$, respectively.   
   
Lets define our variables in a table:

| Symbol  | Variable      | SI Units   |
|:--------|:--------------|:------------|
| $P$     | Pressure      | $Pa$   |
| $\rho$  | Density      | $kg/m^3$   |
| $T$     | Temperature   | $K$ |
| $z$     | Height Above Sea Level   | $m$ |

We would like to write code to calculate atmospheric pressure and density at any given height. In lecture, we practiced using Python's built in mathematical operators `+ = * / **`. Now we will apply these skills to *mathematically describe the state of the atmosphere* and make some informative graphics to communicate our results. As always when tackling a more complex problem, keeping our code organized is incredibly helpful, especially when we need to circle back to either modify or debug our program.
___

### Tips on Writing Code With Style:

* Be very careful with unit conversion.  Humans usually like to express temperature in Celsius, but the thermodynamic equations require temperatures in Kelvin.  That means that you need to distinguish between two temperatures with names like `Tk` and `Tc`, where `Tk = Tc + 273.15`. Make sure that you convert to Kelvin as soon as you can. Do it only once at the start and (if necessary for output) once at the end.

* Choose good variable names. Don’t use single letters like `T` and `P` for variable names in a script. It makes it very hard to do search and replace with your editor when you want to change them, and the names aren’t very meaningful to others who might read your code. Remember that Python is *case sensitive* so `P` and `p` are two different variables. Also, it is super helpful to note the units of each variable with comments.

* As much as you can, separate your script into 4 parts IN THIS ORDER:

>**1.  INPUTS:**  These  are  variables  whose  values  you  might  want  to  change  if  you  run  the  program multiple times.

>**2.  INTERNAL DEFINITIONS or CONSTANTS:** These are variables that are defined as constants which you will never change, or some simple conversions (e.g. Celsius to Kelvin)

>**3.  CALCULATIONS:** This is where the complicated parts of the procedure go

>**4.  OUTPUTS:** What you do once the math is finished (e.g. plotting).

* It is useful to separate the parts by white space, and liberally comment your code. You can also separate each of these four parts into individual cells in a Jupyter Notebook, so you can run them individually, one at a time. Note that not all tasks in 2 and 3 are easily separated, and sometimes plotting happens earlier than the end of the program, but it’s a good idea to always approach problems this way initially.
___
### "Coding Up" the Hydrostatic Equations

Write python code to solve for pressure and density:

```{code-cell} ipython3
# inputs
Tc = 20  # temperature in Celcius [C]
height = 8849  # [m]

# internal definitions
Tk = Tc + 273.15  # temperature in Kelvin [K]
a_P = 0.0342  # [K/m]
a_rho = 0.040  # [K/m]
P0 = 101325  # surface pressure in Pascals [Pa]
rho_0 = 1.225  # density at z=0 [kg/m3]

# calculations
pres = P0 * np.exp(-a_P / Tk * height)  # eq 1.9a
dens = rho_0 * np.exp(-a_rho / Tk * height)  # eq 1.13a

# outputs
# print the result rounded to two decimal places: 
print(f'Pressure at {height}m is {pres:.2f} Pa')
print(f'Density is {dens:.2f} kg/m3')
```

Try playing with the inputs to see if our pressure/density calculator is working properly. We know that at the surface (ie $z$=0m), the pressure should equal the reference $P_0$ of 101325 Pa. On the summit of Mt Everest (8849m), pressure is roughly a third of that value. Waaay up high, (try setting $z$ to a billion or something) the pressure should drop away to near 0 Pa. Is our calculation working properly? *It is **always** good practice to do some "common sense" checks like these wherever you can in writing code - they will save you a lot of time debugging later.*
___
### Math with Arrays

Now that you have working code for *scalar inputs* (and checked that it calculates the correct values), let's can apply it to a whole range of values by defining our inputs as numpy arrays instead of single variables (we could also use lists, tuples or most any *iterable data type* will work). Solving this equation by hand or with a calculator isn't that hard, but now we can solve it again and again as many times as we want for no extra cost! Let's compute the pressure for a bunch of different heights, then use Matplotlib to make an XY plot of our output variables over the specified range of inputs. 

**Remember:** Multiplying an array `A` by a scalar variable `b` multiplies every element of `A` by `b`. Multiplying an array `A` by another array `B` does the operation *element-wise*; i.e. the first element of `A` gets multiplied by the first element of `B`, the second element of `A` by the second of `B`, etc. This only works if the `A` and `B` are the same size and shape.

```{code-cell} ipython3
# change the "height" input to an array
height = np.arange(10000, 0, -1000)  # m

# this cell "knows" about the definitions from the previous cell, no need to repeat
# (unless we want to change something)

# calculations
pres = P0 * np.exp(-a_P / Tk * height)  # eq 1.9a
dens = rho_0 * np.exp(-a_rho / Tk * height)  # eq 1.13a

# output
print(f'Pressure: {pres}')
print(f'Density: {dens}')
```

___
### The `plt.subplots()` Method

The outputs from the previous cell don't exactly jump off the page. We could show our results much better with, you guessed it: *a scientific figure!* Unlike last week, we have 2 separate but related datasets, and ideally we would like to present them together as one figure. For this we can use a slightly different plotting syntax, which creates one big "figure" object, and "axes" objects which are displayed on the figure. We can create the axes individually, referencing them using *slicing* to mess around with their content, labels, colours etc. just like the plot we created last week. The syntax for creating subplots is as follows:

```{code-cell} ipython3
# create the figure with one row and two columns of plots, and
# also specify the two subplots to share the same y-axis.
fig, ax = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

# use slicing to assign what to plot where
ax[0].plot(pres, height)
ax[1].plot(dens, height, color="red")
fig.suptitle("Pressure and Density Variation with Altitude", fontsize=16)  # title for the whole figure
ax[0].set_xlabel("Pressure (Pa)")
ax[0].set_ylabel("Height (m)")  # because sharey=True, we only need this once
ax[1].set_xlabel("Density (kg/m3)");
```

Do we check all the boxes?

<div class="alert alert-block alert-info">
<b>Scientific Figure Checklist:</b> 

- [ ] Title (Short and sweet is best)
- [ ] Axes labels with units (Don't forget the units!)
- [ ] Legend (Or anything that helps interpret the information presented)
- [ ] Does the figure *make sense* just by looking at it? The data should be clear without referencing anything outside the figure
- [ ] Does it *look good*? (Do the colors clash? does it look crowded/messy?)
</div>
___

+++

## Part 2: Clausius-Clapeyron Equation and the Atmospheric Equation of State

Over large spatial scales in the atmosphere (and ocean) we can attempt to predict the winds (or currents) by looking at spatial changes in the DENSITY. In air the density is a function of pressure, temperature, and the amount of water
vapour present - i.e.  the THERMODYNAMIC STATE*. Moist air is less dense than dry air, because H$_2$O gas is lighter than either N$_2$ or O$_2$ gas (which makes up most of the atmosphere). We often hear water vapour measurements given as a RELATIVE HUMIDITY (RH) which is the the ratio of the vapor pressure relative to the SATURATION LEVEL for a particular temperature.  The saturation level is the maximum amount of water vapour that air can hold in equilibrium (say, inside a closed bottle containing air and water, which you let sit for a long time).  A RH of 100% means it is foggy (saturated) and 0% means you are coughing and generating sparks every time you walk across a carpet! How do we get from RH to density?

First, define the following quantities:


| Symbol  | Variable      | SI Units   |
|:--------|:--------------|:------------|
| $\rho$  | Density       | $kg/m^3$ |
| $P$     | Pressure      | $Pa$ |
| $T$     | Temperature   | $K$ |
| $RH$    | Relative Humidity | $\%$ |
| $r$     | Mixing Ratio  | $\frac{kg \space water \space vapor}{kg \space dry \space air}$ |
| $e$     | Vapor Pressure | $Pa$ |
| $e_s$   | Saturation Vapor Pressure | $Pa$ |

Now,  it  would  be  nice  to  have  (say)  a  single,  perhaps  complicated, equation of state for density (as oceanographers do), but in fact atmospheric scientists define things using a chain of temporary variables†. It all begins with the *Clausius-Clapeyron* equation which relates the temperature and the saturation vapour pressure:

$$
e_s = e_0\cdot exp \left[ \frac{L}{R_v}\left(\frac{1}{T_0}-\frac{1}{T}\right)\right]\tag{1}
$$

where $e_0 = 611Pa$, $L= 2.5\cdot10^6J/kg$ is the latent heat of evaporation, $T_0= 273K$ is a constant (NOT $273.15K$), and $R_v= 461J/K/kg$ (Joules per kelvin per kilogram) is the gas constant for pure water vapour. Next we have

$$
e = e_s\frac{RH}{100}\tag{2}
$$

and then 

$$
r = \frac{\varepsilon e}{P - e}\tag{3}
$$

where $\varepsilon= 0.622\frac{kg_{vapour}}{kg_{dry\space air}} \space = \frac{R_d}{R_v}$, and finally

$$
\rho = \frac{P}{R_dT(1 + 0.61r)}\tag{4}
$$

where $R_d = 287J/K/kg$ is  the  ideal  gas  constant  for  dry  air.‡  

To  check  units,  remember  that  $1\space Pa  =1\space kg/m/s^2$, and $1\space J=1\space kg m^2/s^2$.

---

\* For oceanographers, density is a function of pressure, temperature, and salinity, and for geologists the density of (say) molten rock will depend on pressure, temperature, and its chemical composition. For this lab you just have to know that there *are* equations to figure out!

† See [Meteorology Today for Scientists and Engineers, R. Stull](https://www.eoas.ubc.ca/books/Practical_Meteorology/mse3.html)

‡ You may recognize some similarity between this last equation and the IDEAL GAS LAW $P V=nRT$ which is no coincidence - in fact the $0.61r$ is a correction for the non-ideal nature of moist air.
___

+++

### Your Task: Implementing the Clausius-Clapeyron Equation in Python

Write a code cell which defines variables for all the constants used (i.e. $L$, $R_v$, $T_0$, $e_0$) and then find $e_s$ for a single $T$. Be sure to invent good names for all of these symbols and include their units in the comments, e. g. `Lvap = 2.5e6  # J/kg`. Run the cell to find $e_s$ at a temperature of $T= 25^oC$.  Compare this number against a CHECK VALUE 3264.078 Pa. Be careful about operator precedence and make sure you get the correct answer!

**Study question** -- how would you determine the correct number of significant digits to keep in your answer?

```{code-cell} ipython3
---
nbgrader:
  grade: false
  grade_id: cell-f1b8b07be018c013
  locked: false
  schema_version: 3
  solution: true
  task: false
---
# your code here  -- make sure  your result has the four letter name --esat-- (case sensitive)
# also remember to remove the raise NotImplementedError() line when you implement your answer here

### BEGIN SOLUTION
# andrew's soln

# input
Tc = 25  # deg C

# internal definitions
Tk = Tc + 273.15  # K
e0 = 611  # Pa 
Lvap = 2.5e6  # J/kg
T0 = 273  # K
Rv = 461  # J/kg/K

# calculations
esat = e0 * np.exp((Lvap / Rv) * (1 / T0 - 1 / Tk))  # eqn 1

# outputs
print(esat)
### END SOLUTION
```

The cell below shows how we test your answer

```{code-cell} ipython3
---
nbgrader:
  grade: true
  grade_id: cell-b32bec3e32535415
  locked: true
  points: 0
  schema_version: 3
  solution: false
  task: false
---
testing.assert_almost_equal(esat,3264.078,decimal=3)
```

Now add a cell to calculate the air density at  𝑇=25𝑜𝐶,𝑅𝐻=50% , at surface pressure ( 𝑃=102000𝑃𝑎 ). The answer should be (to 7 decimal places) 1.1847106 kg/m 3  (or 1.184704 if  𝜀≡𝑅𝑑/𝑅𝑣 ). Note that increasing the humidity (i.e. adding more water vapour) decreases the density since H 2 O is displacing heavier N 2  and O 2  molecules.

**Again, how many significant digits would you trust in this answer?**

```{code-cell} ipython3
---
nbgrader:
  grade: false
  grade_id: cell-65b44ba43054e96e
  locked: false
  schema_version: 3
  solution: true
  task: false
---
# remove the exception and type your answer here 
# -- name your output variable rho

### BEGIN SOLUTION
# andrew's soln

# input
RH = 50  # %
pres = 102000  # Pa

# internal definitions (this cell knows about the variables defined in the cell above,
# so just add the new ones as needed)
epsilon = 0.622  # vap/air by mass
Rd = 287  # J/kg/K

# calculations
e_x = esat * RH / 100  # eqn 2
mixrat = epsilon * e_x / (pres - e_x)  # eqn 3
rho = pres / (Rd * Tk * (1 + 0.61 * mixrat))

# output
print(rho)
### END SOLUTION
```

```{code-cell} ipython3
---
nbgrader:
  grade: true
  grade_id: cell-818867e3c135f448
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
testing.assert_almost_equal(rho,1.1847,decimal=4)
```

Calculate and plot the saturation vapour pressure $e_s$ for temperatures ranging from -40$^o$C to 30$^o$C at surface pressure and RH of 50%. Be sure to stick to the format of *input, definitions, calulations, output*.  Name your 
output variable esat

```{code-cell} ipython3
---
nbgrader:
  grade: true
  grade_id: cell-27da51ca0fab5457
  locked: false
  points: 1
  schema_version: 3
  solution: true
  task: false
---
# your code

### BEGIN SOLUTION

# andrew's soln

# input
Tc = np.arange(-40, 31)

# definitions
Tk = Tc + 273.15  # K

# calculations
esat = e0 * np.exp((Lvap / Rv) * (1 / T0 - 1 / Tk))  # eqn 1

# output 
esat
### END SOLUTION
```

Next, calculate and plot the mixing ratio $r$ as a function of temperature for $RH= 100\%$ and $P= 90000Pa$ 
(about 1 km above the surface).

```{code-cell} ipython3
---
nbgrader:
  grade: true
  grade_id: cell-8e78d581cfbe5b17
  locked: false
  points: 1
  schema_version: 3
  solution: true
  task: false
---
# your code here

### BEGIN SOLUTION
# andrew's soln

# input
RH = 100  # %
pres = 90000  # Pa

# calculations
e_x = esat * RH / 100  # eqn 2
mixrat = epsilon * e_x / (pres - e_x)  # eqn 3

# output
mixrat
### END SOLUTION
```

Now, use the `plt.subplots` function to generate a scientific figure as follows:

* Two plots, the top one showing saturation vapour pressure and the bottom showing mixing ratio as functions of temperature (for $RH= 100\%$ and $P= 90000Pa$).

* "Temperature" on the x axis, in units of $^o$C, only labelled once for the whole figure

* Make sure that your figure checks all the boxes for creating a scientific figure

```{code-cell} ipython3
---
nbgrader:
  grade: true
  grade_id: cell-42bbc21bdb10e72b
  locked: false
  points: 1
  schema_version: 3
  solution: true
  task: false
---
# your code

### BEGIN SOLUTION
# andrew's soln
fig, ax = plt.subplots(2, figsize=(10, 5), sharex=True)
fig.suptitle("Saturation Vapour Pressure and Mixing Ratio as Functions of Temperature", fontsize=16)
ax[0].plot(Tc, esat)
ax[0].set_ylabel("Saturation Vapour Pressure (Pa)")

ax[1].plot(Tc, mixrat, color="lightgreen")
ax[1].set_xlabel("Temp ($^o$C)")
ax[1].set_ylabel("Mixing Ratio (kg/kg)");
### END SOLUTION
```
