# Bank - CS50P Problem Set 1

This exercise is part of **CS50P: Introduction to Programming with Python** at Harvard University, specifically from **Week 1: Conditionals**. It introduces conditional statements (if-elif-else) and string manipulation to simulate a bank's greeting-based tip system.

## Problem Description
The task is to write a program that determines the tip amount based on a user's greeting:
- If the greeting starts with "hello", the tip is $0.
- If the greeting starts with "h" (but not "hello"), the tip is $20.
- Otherwise, the tip is $100.

The program must handle case-insensitive input and ignore leading/trailing whitespace.

## Code Explanation
The provided Python code implements this logic using conditionals:

```python
def main():
    greetings = input("Greeting: ").strip().lower()
    if greetings[0:5] == "hello":
        print("$0")
    elif greetings[0] == "h":
        print("$20")
    else:
        print("$100")

main()
```

- **Input Handling**: `greetings = input("Greeting: ").strip().lower()`  
  Prompts for a greeting, removes whitespace, and converts to lowercase for case-insensitive comparison.

- **Conditionals**:  
  - `if greetings[0:5] == "hello"`: Checks if the first 5 characters are "hello" (exact match for the start).  
  - `elif greetings[0] == "h"`: If not "hello", checks if the first character is "h".  
  - `else`: Defaults to $100 for any other greeting.

- **Output**: Prints the corresponding tip amount.

- **Execution**: `main()` is called to run the program.

## How It Works
1. Run the program.
2. Enter a greeting (e.g., "Hello there").
3. The program processes the input: "hello there".
4. Checks conditions: starts with "hello" → outputs "$0".
5. For "Hi", starts with "h" but not "hello" → "$20".
6. For "Good morning" → "$100".

## Key Concepts Covered in CS50P
- **Conditionals**: Using `if`, `elif`, and `else` for decision-making.
- **Strings**: Slicing (`[0:5]`), `strip()`, and `lower()`.
- **Input/Output**: Basic user interaction.
- **Best Practices**: Case-insensitive handling; assumes input is at least 1 character (could add checks for empty strings).

## Example Usage
```
Greeting: Hello
$0

Greeting: Hi
$20

Greeting: What's up
$100
```

This exercise builds logical thinking with conditionals, essential for branching program flow. For the full problem set details, refer to the `problem_set.md` file in the same directory.