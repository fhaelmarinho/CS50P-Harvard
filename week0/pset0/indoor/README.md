# Indoor Voice - CS50P Problem Set 0

This exercise is part of **CS50P: Introduction to Programming with Python** at Harvard University, specifically from **Week 0: Functions, Variables**. It emphasizes string manipulation and user input by converting text to lowercase, simulating the concept of speaking in an "indoor voice" (quietly).

## Problem Description
The task is to write a program that takes user input as a string and outputs it in all lowercase letters. This represents converting loud (uppercase) text to a softer, indoor-appropriate voice.

## Code Explanation
The provided Python code implements this functionality simply:

```python
text = input("Enter the text: ").strip().lower()
print("Your lower case text is:", text)
```

- **Input Handling**: `text = input("Enter the text: ").strip().lower()`  
  Prompts the user for a string input, removes leading/trailing whitespace with `.strip()`, and converts the entire string to lowercase using `.lower()`. The methods are chained for efficiency.

- **Output**: `print("Your lower case text is:", text)`  
  Displays a message followed by the modified text.

## How It Works
1. Run the program.
2. Enter a string (e.g., "HELLO WORLD").
3. The program strips whitespace and converts to lowercase.
4. Outputs the result (e.g., "Your lower case text is: hello world").

## Key Concepts Covered in CS50P
- **Strings**: Using methods like `strip()` and `lower()` for text processing.
- **Input/Output**: Handling user input and formatted output.
- **Method Chaining**: Applying multiple string operations in sequence.
- **Best Practices**: The code is concise; in a more robust version, you could handle empty inputs or add validation.

## Example Usage
```
Enter the text: HELLO WORLD
Your lower case text is: hello world
```

This exercise introduces basic string transformations in Python, essential for text handling in programming. For the full problem set details, refer to the `problem_set.md` file in the same directory.