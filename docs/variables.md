# Variables and Variable Types

> Introduce Python variables and common value types.

WHY:
Programs are built from values.
Clear naming supports readable and maintainable code.

## What Is a Variable

In Python, a **variable** is a name that holds a value.

A variable associates a readable name with a piece of data
so it can be reused, updated, and inspected throughout a program.

## Common Variable Types

Examples of common value types:

- `str` – holds text
- `int` – holds a whole number
- `float` – holds a decimal number
- `bool` – holds either `True` or `False` (capitalized)
- `list[T]` – ordered collections of values
- `dict[K, V]` – key/value mappings

The letters inside square brackets (such as `T`, `K`, and `V`) are **type hints**.
They describe what kind of values the collection is expected to contain.

## Type Hints (Why We Use Them)

Type hints make variable types explicit.

```python
name: str = "Abbie"
age: int = 5
weight_lbs: float = 9.8
is_cat: bool = True
```

Benefits:

- clearer intent
- better editor feedback
- easier collaboration

Type hints do **not** change how Python runs.

## Numeric Values - Include the Units

Units matter when working with numbers.
Make units explicit to improve quality and clarity.

```python
weight_lbs: float = 9.8
height_ft: float = 2.4
```

## For currency, use Decimal

Working with currency, precision matters. Use a Decimal.

```python
from decimal import Decimal

adoption_fee_usd: Decimal = Decimal("35.50")
```

## Constants

Values that do not change are indicated by:

- the way we name it ALL_CAP_SNAKE_CASE
- adding `Final` to the type hint

Examples

```python
CAT_NAME: Final[str] = "Abbie"
```

## Why Variables Come First

Variables are introduced early because:

- programs are composed of values
- data analysis depends on naming data clearly
- readable variables make intent visible

## Where Variables Are Used

Variables appear throughout Python programs, including:

- calculations
- logging output
- reading data from files
- building summaries of results

Clear variable names reduce confusion and improve code quality over time.
