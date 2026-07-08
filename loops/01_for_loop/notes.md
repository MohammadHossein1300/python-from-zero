# For Loop

## What is a for loop?

A `for` loop is used to repeat a block of code for each item in a sequence.

---

## Syntax

```python
for item in sequence:
    # code
```

---

## Using range()

`range()` generates a sequence of numbers.

```python
range(start, stop)
```

Example:

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1
2
3
4
5
```

---

## Step

The third parameter of `range()` is called **step**.

```python
range(2, 21, 2)
```

Output:

```
2
4
6
8
10
12
14
16
18
20
```

---

## Key Points

- `for` repeats code.
- `range()` creates a sequence of numbers.
- The stop value is **not included**.
- The step value controls the increment.

---

## What I Learned

- How to use `for` loops.
- How to use `range()`.
- How to use the `step` parameter.
- How to combine `for` with `if`.

---

## My Mistakes

- I learned that `range()` does not include the last number.
- I learned that `range()` can take a third argument called `step`.