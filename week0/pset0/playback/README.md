# Playback Speed - CS50P Problem Set 0

This exercise is part of **CS50P: Introduction to Programming with Python** at Harvard University, specifically from **Week 0: Functions, Variables**. It focuses on string manipulation by simulating slowed-down speech through replacing spaces with ellipses, mimicking how speech might sound when played back at a slower speed.

## Problem Description
The task is to write a program that takes user input as a string and replaces each space with three periods ("...") to represent pauses, as if the text is being played back slowly.

## Code Explanation
The provided Python code implements this functionality concisely:

```python
phrase = input("Enter the phrase: ").strip().replace(" ", "...")
print(phrase)
```

- **Input Handling**: `phrase = input("Enter the phrase: ").strip().replace(" ", "...")`  
  Prompts the user for a string input, removes leading/trailing whitespace with `.strip()`, and replaces all spaces (" ") with "..." using `.replace()`. The methods are chained for efficiency.

- **Output**: `print(phrase)`  
  Displays the modified phrase directly.

## How It Works
1. Run the program.
2. Enter a phrase (e.g., "This is CS50").
3. The program strips whitespace and replaces spaces with "...".
4. Outputs the result (e.g., "This...is...CS50").

## Key Concepts Covered in CS50P
- **Strings**: Manipulating text with methods like `strip()` and `replace()`.
- **Input/Output**: Basic user interaction and output.
- **Method Chaining**: Applying multiple operations in sequence.
- **Best Practices**: The code is straightforward; for extensions, you could handle multiple spaces or add more complex replacements.

## Example Usage
```
Enter the phrase: This is CS50
This...is...CS50
```

This exercise demonstrates simple string replacement in Python, a building block for text processing tasks. For the full problem set details, refer to the `problem_set.md` file in the same directory.