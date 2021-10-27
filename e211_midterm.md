---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.10.3
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

Name (Last, First):
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Student Number:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Signature:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

In-class Group:
\_\_\_\_\_

<!-- #region ctype="question" quesnum=4 answer="E" -->
Q1) Imagine we end up burning the rest of the available coal (2800 Gton
    carbon) **and** the oil and natural gas (200 Gton carbon), but we
    don’t burn any other fossil carbon. What will the atmospheric
    concentration of $CO_2$ be when we’re finished? Assume we
    burn everything instantaneously, that all of the emitted carbon
    stays in the atmosphere, and that today’s atmospheric $CO_2$
    concentration is 400 ppm.

   A) about 580 ppm  
   B) about 640 ppm  
   C) about 1050 ppm  
   D) about 1200 ppm  
   E) about 1830 ppm
<!-- #endregion -->

Answer E)  -- we know that there are 2.1 Gigatonnes per ppm so divide by this to find increase:

```python
new_concentration = 3000/2.1 + 400.
print(f"{new_concentration=:5.1f} ppm")
```

<!-- #region ctype="question" quesnum=5 answer=" " -->
Q2) For the figure below, pick the most accurate description of the
    rectangular region labeled (2).  Assume the instrument is looking down from the top of this atmosphere

  <img src="final_2018t2/media/image14.png" width="50%" > 

   A) The radiation emitted by the gas that reaches the top of the atmosphere  
   B) The radiation absorbed by the gas  
   C) The greenhouse effect from the gas in this wavenumber range  
   D) The surface radiation absorbed by the gas  gas  
   E) The radiation emitted by the gas that reaches the surface
<!-- #endregion -->

```
Answer C) -- this is top - bottom = greenhouse effect.
```


Q3) For this feedback loop:

<img src="final_2018t2/media/image16.png" width="50%" >

  Choose the best characterization, keeping in mind that feedbacks
  work in both directions.  ($R_{net}$ is the net downward radiation at the top of the atmosphere)

   A) Amplifying because increasing low clouds heat the surface through
      longwave emission  
   B) Stabilizing because increasing low clouds reduce the surface heat
      flux  
   C) Amplifying because increasing low clouds reflect more incoming
      shortwave  
   D) Amplifying because increasing low clouds increase atmospheric
      mixing  
   E) Stabilizing because increasing low clouds emit more radiation to
      space

<!-- #region ctype="question" quesnum=6 answer=" " -->
Answer C) Amplifying: if an increase in temperature reduces cloud fraction, and increasing clouds reflect more incoming shortwave
then decreasing clouds must reflect less, so the loops heats and amplify.

In the same way, if the perturbation was cooling, the the clouds would increase, amplifying the cooling
<!-- #endregion -->

<!-- #region ctype="question" quesnum=7 answer=" " -->
Q4) Consider the following shallow, nocturnal atmospheric layer with
    emissivity **$ε_a$=0.8** over ground with emissivity of ε=1. If
    the ground temperature $T_g$ is 300 K and the air
    temperature $T_a$ is 260 K, what is the heating/cooling rate
    **of the ground** in $W\,m^{-2}$?

   **(Note 250 $W\,m^{-2}$ in longwave flux is entering the layer from above)**

   **Shortcut:  $\sigma \times 300^4 = 460\ W\,m\,^2$**

      
   <img src="final_2018t2/media/image17.png" width="50%" /> 
   
      
   A) -251 $W\,m^{-2}$  
   B) -202 $W\,m^{-2}$  
   C) +101 $W\,m^{-2}$  
   D) +202 $W\,m^{-2}$  
   E) +251 $W\,m^{-2}$
<!-- #endregion -->

Answer: B) the first term is 250*transmission, the second is $\epsilon \sigma T_a^4$ and the third is $\sigma T_g^4$ -- with the upward flux negative and downward positive, this gives -202 $W/m^2$

```python answer=" " ctype="question" quesnum=7
sigma = 5.67e-8
hr=250*(1 - 0.8) + 0.8*sigma*260**4. - 460.  #B
print(f"heating rate at the ground is {hr=:5.1f} W/m^2")
```

<!-- #region ctype="question" quesnum=5 answer=" " -->
Q6) Moist air on the western side of a mountain  has a temperature of 280 K and a vapor mixing ratio of 15 g/kg.   If it removes 5 g/kg during ascent from sea-level to 3 km, what will the temperature change $\Delta T$  be when it descends back to sea-level on the east side of the mountain?

  A) -15 K  
  B) -10 K  
  C) 0 K  
  D) 10 K  
  E) 15 K
<!-- #endregion -->

Answer E) 

The moist static energy can't change, so if we write after - before as $\Delta$ then:

$$
\begin{align}
\Delta h_m &= 0 = c_p \Delta T + l_v \Delta w_v\\
\Delta T &= -\frac{l_v \Delta w_v}{c_p}
\end{align}
$$

which is 15 K

```python
temp=280
cp = 1004.
lv=2.5e6
delta_wv = -6.e-3
delta_temp = -lv*delta_wv/cp
print(f"{delta_temp=:5.1f} K")
```

Q7) Based on the figure below, what would an aircraft flying at 70 km estimate for the temperature of the ocean surface?

  A) 220 K  
  B) 240 K  
  C) 275 K  
  D) 295 K  
  E) 305 K


<img src="quiz2_media/modtran_5level.png" width ="50%" />


Answer D) 295 K -- looking through the atmospheric window at 900 $cm^{-1}$ the brightness temperature is between
290 and 300 K.  Since we know the ocean is black in the longwave, that is the ocean surface temperature.


Q8) For the same figure, what is your best estimate of the air temperature at 5 km?

  A) 220 K  
  B) 240 K  
  C) 275 K  
  D) 295 K  
  E) 305 K


Answer C) 275 K 
In the CO2 band we can see that there are 4 temperature lines, with the surface coldest, so 5 km above the surface
is the next coldest.  It is showing a brightness temperature between 270 K and 280 K and since we
know CO2 is black at 666 $cm^{-1}$ that must be the actual temperature of the surrounding air.


Q9)  Given a solar constant of 1100 $W/m^2$, find the change in the equlibrium surface
temperature for a planet with no atmosphere if its shortwave albedo drops from $\alpha=0.7$ to $\alpha=0.5$.  Assume the surface is black in the longwave, and that it rotates once every 24 hours so that over time the radiative flux is spread evenly over
all longitudes.

  A) -15 K  
  B) -10 K  
  C) +10 K  
  D) +15 K  
  E) +25 K


Answer E) + 25 K.  We can rule out negative temperature drops since the albedo is decreasing so the downward flux
$I reaching the surface must be increasing. For a black surface the equations are:

$I = S_0(1 - \alpha)/4.$ and $I = \sigma T^4$.

```python
S0=1100
sigma = 5.67e-8
alpha_before = 0.7
alpha_after = 0.5
I_before = S0/4.*(1-alpha_before)
T_before = (I_before/sigma)**0.25
I_after = S0/4.*(1-alpha_after)
print(f"{I_before=:5.1f} W/m^2, {I_after=:5.1f} W/m^2")
T_after = (I_after/sigma)**0.25
print(f"{T_before=:5.1f} K, {T_after=:5.1f} K, so {(T_after - T_before)=:5.1f} K")
```

<!-- #region -->
Q10) Suppose we raise the CO2 concentration from the current 410 ppm to 600 ppm.  What is that in doublings?  Choose the closest answer.


  A) 0.2 doublings   
  B) 0.4 doublings  
  C) 0.6 doublings  
  D) 0.8 doublings   
  E) 1 doubling
<!-- #endregion -->

Answer C) 0.6 -- The definition of a doubling is 

$$
\ln \left ( \frac{newCO2}{oldCO2} \right ) / \ln 2
$$

So the numbers are:

```python
import numpy as np
doubling=np.log(600/410.)/np.log(2)
print(f"{doubling=:5.2f}")
```

# Quiz 2 constants

$$
\alpha = \beta
$$
