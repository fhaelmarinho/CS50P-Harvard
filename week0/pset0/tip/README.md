# Tip Calculator - CS50P Problem Set 0

This exercise is part of **CS50P: Introduction to Programming with Python** at Harvard University, specifically from **Week 0: Functions, Variables**. It introduces functions, user input, string manipulation, and basic arithmetic by building a simple tip calculator.

## Problem Description
The task is to write a program that calculates the tip amount based on the meal cost and desired tip percentage. The program must:
- Prompt for the meal cost (e.g., "$50.00").
- Prompt for the tip percentage (e.g., "15%").
- Compute the tip as cost × (percentage / 100).
- Output the tip amount formatted as currency (e.g., "Leave $7.50").

## Code Explanation
The provided Python code implements this using functions for modularity:

```python
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$","")
    d = float(d)
    return(d)


def percent_to_float(p):
    p = p.replace("%","")
    p = float(p)/100
    return(p)


main()
```

- **main() Function**:  
  - Calls `dollars_to_float()` to convert user input for meal cost.  
  - Calls `percent_to_float()` to convert user input for tip percentage.  
  - Calculates `tip = dollars * percent`.  
  - Prints the result formatted to 2 decimal places using f-string formatting.

- **dollars_to_float(d)**:  
  - Removes the "$" symbol from the input string.  
  - Converts the cleaned string to a float and returns it.

- **percent_to_float(p)**:  
  - Removes the "%" symbol from the input string.  
  - Converts to float and divides by 100 to get the decimal percentage, then returns it.

- **Execution**: `main()` is called at the end to run the program.

## How It Works
1. Run the program.
2. Enter meal cost (e.g., "$50.00").
3. Enter tip percentage (e.g., "15%").
4. The program cleans the inputs, calculates tip = 50.00 * 0.15 = 7.50.
5. Outputs "Leave $7.50".

## Key Concepts Covered in CS50P
- **Functions**: Defining and calling custom functions (`main`, `dollars_to_float`, `percent_to_float`).
- **Input/Output**: Using `input()` and formatted `print()` with f-strings.
- **String Manipulation**: Removing characters with `replace()`.
- **Type Conversion**: Converting strings to floats.
- **Arithmetic**: Basic multiplication and division.
- **Best Practices**: Modular code with helper functions; error handling could be added for invalid inputs.

## Example Usage
```
How much was the meal? $50.00
What percentage would you like to tip? 15%
Leave $7.50
```

This exercise demonstrates practical programming by combining input processing, calculations, and output formatting. For the full problem set details, refer to the `problem_set.md` file in the same directory.