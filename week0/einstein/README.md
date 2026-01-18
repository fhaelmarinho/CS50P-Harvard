# Einstein's Energy-Mass Equivalence (E = mc²) - CS50P Problem Set 0

This exercise is part of **CS50P: Introduction to Programming with Python** at Harvard University, specifically from **Week 0: Functions, Variables**. It introduces basic programming concepts like user input, variables, arithmetic operations, and output, while implementing Albert Einstein's famous equation for mass-energy equivalence.

## Problem Description
The task is to write a program that calculates the energy (E) equivalent to a given mass (m) using the formula **E = mc²**, where:
- **m** is the mass in kilograms.
- **c** is the speed of light (approximately 300,000,000 m/s).
- **E** is the energy in joules.

The program must prompt the user for the mass, perform the calculation, and display the result.

## Code Explanation
The provided Python code implements this calculation in a simple, straightforward manner:

```python
m = int(input("Enter the mass: ").strip())
c = 300000000
E = m * pow(c, 2)

print(E)
```

- **Input Handling**: `m = int(input("Enter the mass: ").strip())`  
  Prompts the user to enter a mass value as a string, removes any leading/trailing whitespace with `.strip()`, and converts it to an integer using `int()`. This assumes the input is a valid integer (e.g., no decimals or invalid characters, as per the problem constraints).

- **Constants**: `c = 300000000`  
  Defines the speed of light as a constant (300,000,000 meters per second). This value is hardcoded for simplicity.

- **Calculation**: `E = m * pow(c, 2)`  
  Computes the energy using the formula E = m * c². The `pow(c, 2)` function raises c to the power of 2 (equivalent to `c ** 2` or `c * c`).

- **Output**: `print(E)`  
  Displays the calculated energy value directly to the console.

## How It Works
1. Run the program.
2. Enter a mass value (e.g., `5` for 5 kg).
3. The program calculates E = 5 * (300000000)² = 5 * 90000000000000000 = 450000000000000000 joules.
4. Outputs the result (e.g., `450000000000000000`).

## Key Concepts Covered in CS50P
- **Variables**: Storing values like `m`, `c`, and `E`.
- **Input/Output**: Using `input()` for user interaction and `print()` for display.
- **Arithmetic**: Basic multiplication and exponentiation.
- **Data Types**: Converting strings to integers with `int()`.
- **Best Practices**: The code is concise, but in a full CS50P solution, you might add error handling (e.g., checking for non-integer inputs) or use more descriptive variable names.

## Example Usage
```
Enter the mass: 5
450000000000000000
```

This exercise demonstrates how programming can model real-world physics equations, building foundational skills for more complex problems in the course. For the full problem set details, refer to the `problem_set.md` file in the same directory.