# Skills Covered and Required Knowledge

This document enumerates the skills, concepts, tools, and professional habits required to complete the project.

Some skills are introduced directly in this project; others are assumed, reinforced, or practiced implicitly.

## 1. Python Files and Docstrings (Module-Level)

Professionals must be able to:

- Create Python source files using the `.py` extension
- Understand that a Python file is also called a _module_
- Place a **module-level docstring** at the very top of a file
- Use **triple-quoted strings** (`""" ... """`) for docstrings
- Write docstrings that describe:
  - the purpose of the file
  - how it is intended to be used
  - authorship and date (when required)
- Distinguish docstrings from comments
- Recognize that docstrings:
  - are documentation
  - are accessible via tools like `help()`
  - do not affect runtime behavior

## 2. Comments and Code Readability

Professionals must be able to:

- Write inline comments using `#`
- Distinguish between:
  - comments (for humans)
  - executable code (for the interpreter)
- Use comments to:
  - explain intent and rationale
  - clarify non-obvious logic
  - label logical sections of a file
- Follow conventions for:
  - spacing
  - indentation
  - visual structure
- Avoid redundant or obvious comments

## 3. Importing Code and Reuse

Skills covered include:

- Using `import` statements correctly
- Importing from:
  - the Python standard library
  - external packages
- Understanding that:
  - external packages must be declared in `pyproject.toml`
  - imports appear near the top of a file
- Reading and interpreting multi-line import statements
- Recognizing imports as explicit reuse of existing code

## 4. Variables and Assignment

Professionals must be able to:

- Declare variables using assignment (`=`)
- Choose descriptive, meaningful variable names
- Follow naming conventions:
  - `snake_case` for variables
- Understand common built-in data types:
  - `str`
  - `int`
  - `float`
  - `bool`
  - `list`
- Reason about variables as references to values

## 5. Type Hints

Skills covered include:

- Understanding what **type hints** are
- Knowing why type hints are used:
  - readability
  - correctness
  - tooling support
- Adding type hints to:
  - variables
  - function return values
- Understanding that type hints:
  - do not change runtime behavior
  - improve clarity and maintainability
- Using basic type hint syntax:
  - `name: str = "value"`
  - `values: list[float]`
  - `def func() -> str:`

## 6. Constants and Naming Conventions

Professionals must understand that:

- Some variables are intended not to change
- Such values are treated as **constants**
- Constants are conventionally written as:
  - `UPPER_CASE_WITH_UNDERSCORES`
- Constants are declared near the top of a module
- Constants improve:
  - readability
  - maintainability
  - correctness
- Constancy is a convention, not a language-enforced rule

## 7. Lists and Collections

Skills covered include:

- Creating lists using square brackets (`[]`)
- Storing multiple values in a list
- Understanding that lists are:
  - ordered
  - mutable
- Passing lists to functions
- Logging or displaying lists
- Using lists as inputs to computations

## 8. Formatted Strings (f-strings)

Professionals must be able to:

- Create formatted string literals using `f"..."` or `f"""..."""`
- Embed variables using `{}` placeholders
- Format numeric values for readability
- Prefer f-strings over:
  - string concatenation
  - older formatting approaches
- Use multi-line f-strings for structured output

## 9. Functions

Skills covered include:

- Defining functions using `def`
- Choosing clear, descriptive function names
- Writing function-level docstrings
- Understanding:
  - parameters
  - return values
- Using `return` to pass data back to the caller
- Calling functions from other functions
- Storing returned values in variables

## 10. Logging (Professional Output)

Professionals must understand:

- Why logging is preferred over `print`
- What a logger is and how it is obtained
- Logging messages at appropriate levels (e.g., INFO)
- That logging:
  - records program execution
  - supports debugging and diagnostics
- How to read and interpret logged output

## 11. Introductory Descriptive Statistics

Skills covered include:

- Working with numeric lists
- Computing basic descriptive quantities:
  - total (sum)
  - count
  - minimum
  - maximum
- Understanding:
  - mean (average)
  - standard deviation
- Using library functions for statistical computation
- Interpreting computed results

## 12. Control Flow and Conditionals

Professionals must be able to:

- Write `if` statements
- Use Boolean expressions
- Guard computations to prevent errors
- Understand how conditional logic controls execution

## 13. Program Structure and Entry Points

Skills covered include:

- Defining a `main()` function
- Understanding why programs use a main entry point
- Using the standard Python execution guard:
  ```python
  if __name__ == "__main__":
      main()
  ```
- Distinguishing between:
  - running a file as a script (e.g., the app files)
  - importing it as a module (e.g., datafun-toolkit)
- Recognizing this pattern as standard Python practice

## 14. Side Effects vs Returned Values

Professionals must understand:

- The difference between:
  - functions that return values
  - functions that produce side effects
- That logging is a side effect
- Why separating computation from output improves design

## 15. Following Constraints and Instructions

Skills covered include:

- Reading and following project instructions
- Running provided reference code without modification
- Using working examples as references
- Seeking clarification when behavior is unclear

## 16. Professional Habits Reinforced

This project reinforces:

- Careful reading of code
- Attention to detail
- Respect for conventions
- Incremental learning
- Observational debugging
