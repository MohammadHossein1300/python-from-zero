# Nested Loops

## What is a Nested Loop?

A nested loop is a loop inside another loop.

The outer loop usually controls the rows.
The inner loop usually controls the columns.

---

## Syntax

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

## Common Uses

- Print patterns
- Tables
- Grids
- Matrix operations
- Games

---

## What I Learned

- The outer loop controls the number of rows.
- The inner loop controls what is printed in each row.
- `print(end=" ")` prints values on the same line.
- `print()` moves to the next line.
- `i` usually represents the row.
- `j` usually represents the column.