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
---

```{code-cell} ipython3
word = "program"
for i in word:
    print(i,end = '-')
```

```{code-cell} ipython3
test = list([word])
print(test)
print(list([1,2]))
a=["word"]
print(a)
list("word"),list(["word"])
```

```{code-cell} ipython3
for i in [word]:
    print(i)
    
for i in list(word):
    print(i)
```

```{code-cell} ipython3
list(range(5))
```

```{code-cell} ipython3
y=[1,2,3,4]
y[-1]
```
