# Logical Operators

Logical operators are used to combine multiple conditions.

## and
Returns True only if both conditions are True.

Example:

```python
age >= 18 and has_id == "yes"
```

## or
Returns True if at least one condition is True.

Example:

```python
is_weekend or is_holiday
```

## not
Reverses a boolean value.

Example:

```python
not is_logged_in
```

## Order of if / elif

Always place the most specific condition first.

Example:

```python
if age >= 18 and has_id == "yes":
```

Then check simpler conditions:

```python
elif age < 18:
```

Finally use `else` for all remaining cases.

## What I learned

- Combine multiple conditions using `and` and `or`.
- Use `not` to reverse a boolean value.
- `else` executes when none of the previous conditions are True.
- The order of conditions affects the program's behavior.