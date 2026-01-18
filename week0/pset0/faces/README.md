# Faces - CS50P Problem Set 0

This exercise is part of **CS50P: Introduction to Programming with Python** at Harvard University, specifically from **Week 0: Functions, Variables**. It focuses on string manipulation, user input, and basic text processing by converting text-based emoticons to emoji representations.

## Problem Description
The task is to write a program that takes user input as a string and replaces text-based emoticons with their corresponding emoji:
- `:)` becomes `🙂` (smiling face)
- `:(` becomes `🙁` (frowning face)

The program should output the modified string with all occurrences replaced.

## Code Explanation
The provided Python code implements this functionality concisely:

```python
text = input("Enter the text: ").strip()
text = text.replace(":)", "🙂")
text = text.replace(":(", "🙁")
print(text)
```

- **Input Handling**: `text = input("Enter the text: ").strip()`  
  Prompts the user for a string input, removes any leading or trailing whitespace with `.strip()`, and stores it in the variable `text`.

- **Replacements**:  
  - `text = text.replace(":)", "🙂")` replaces all occurrences of `:)` with the smiling face emoji `🙂`.  
  - `text = text.replace(":(", "🙁")` replaces all occurrences of `:(` with the frowning face emoji `🙁`.  
  The `replace()` method is called sequentially on the same string, ensuring both replacements are applied.

- **Output**: `print(text)`  
  Displays the modified text to the console.

## How It Works
1. Run the program.
2. Enter a string containing emoticons (e.g., "Hello :) I am sad :(").
3. The program replaces `:)` with `🙂` and `:(` with `🙁`.
4. Outputs the result (e.g., "Hello 🙂 I am sad 🙁").

## Key Concepts Covered in CS50P
- **Strings**: Manipulating text data with methods like `replace()`.
- **Input/Output**: Using `input()` for user interaction and `print()` for display.
- **String Methods**: Understanding built-in methods for text processing.
- **Sequential Operations**: Applying multiple transformations to the same variable.
- **Best Practices**: The code is simple and effective; for robustness, you could handle case sensitivity or additional emoticons in extended versions.

## Example Usage
```
Enter the text: Hello :) I am sad :(
Hello 🙂 I am sad 🙁
```

This exercise illustrates basic string manipulation in Python, a fundamental skill for text processing tasks in programming. For the full problem set details, refer to the `problem_set.md` file in the parent directory.