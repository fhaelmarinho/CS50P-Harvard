# Deep Thought - CS50P Problem Set 1

This exercise is part of **CS50P: Introduction to Programming with Python** at Harvard University, specifically from **Week 1: Conditionals**. It uses conditional statements to check user input against the answer to the "Great Question of Life, the Universe, and Everything" from Douglas Adams' *The Hitchhiker's Guide to the Galaxy*, where the answer is 42.

## Problem Description
The task is to write a program that prompts the user for the answer to the great question and responds with "Yes" if the input matches "42", "forty two", or "forty-two" (case-insensitive), otherwise "No".

## Code Explanation
The provided Python code implements this with a simple conditional check:

```python
def main():
    response = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    if (response == "42") or (response == "forty two") or (response == "forty-two"):
        print("Yes")
    else:
        print("No")

main()
```

- **Input Handling**: `response = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()`  
  Prompts for the answer, removes whitespace, and converts to lowercase for case-insensitive comparison.

- **Conditionals**:  
  - Checks if the response exactly matches "42", "forty two", or "forty-two" using `or` for multiple conditions.  
  - If true, prints "Yes"; otherwise, "No".

- **Execution**: `main()` is called to run the program.

## How It Works
1. Run the program.
2. Enter an answer (e.g., "42" or "Forty-Two").
3. The program normalizes the input and checks against the valid answers.
4. Outputs "Yes" for matches, "No" otherwise.

## Key Concepts Covered in CS50P
- **Conditionals**: Using `if` with `or` for multiple conditions.
- **Strings**: `strip()` and `lower()` for input normalization.
- **Input/Output**: User prompts and responses.
- **Best Practices**: Case-insensitive handling; the code is concise but could be extended with more answers or error handling.

## Example Usage
```
What is the Answer to the Great Question of Life, the Universe, and Everything? 42
Yes

What is the Answer to the Great Question of Life, the Universe, and Everything? forty-two
Yes

What is the Answer to the Great Question of Life, the Universe, and Everything? 41
No
```

This exercise playfully introduces conditional logic while referencing pop culture. For the full problem set details, refer to the `problem_set.md` file in the same directory.