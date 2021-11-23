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

# Week 11 quiz solution: pandas

```{code-cell} ipython3
import pandas as pd
```

```{code-cell} ipython3
filepath = "enso_data.csv"
df = pd.read_csv(filepath)
```

```{code-cell} ipython3
df = pd.read_csv(filepath, index_col=0, parse_dates=True)
df_enso=df.tail(5)
df_enso = df_enso[['Nino12','Nino3','Nino4']]
```

## Given the following DataFrame:

```{code-cell} ipython3
df_enso
```

Write down the numerical values that would be printed for each of the following statements:

```{code-cell} ipython3
df_enso.loc['2021-02-01']
```

```{code-cell} ipython3
df_enso['Nino3']['2021-03-01']
```

```{code-cell} ipython3
df_enso.columns
```

```{code-cell} ipython3
df_enso.iloc[4,2]
```
