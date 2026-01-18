# Meal Time - CS50P Problem Set 1

This exercise is part of **CS50P: Introduction to Programming with Python** at Harvard University, specifically from **Week 1: Conditionals**. It introduces functions, input validation, and conditional logic to determine meal times based on a 24-hour time input.

## Problem Description
The task is to write a program that prompts for a time (in HH:MM format) and outputs the corresponding meal time:
- Breakfast: 7:00 to 8:00
- Lunch: 12:00 to 13:00
- Dinner: 18:00 to 19:00
- No output for other times.

The program must convert the time to a float (e.g., "7:30" → 7.5) and handle valid minute values (0-59).

## Code Explanation
The provided Python code uses a main function and a helper function for time conversion:

```python
def main():
    now_time = input("What time's it? ").strip()

    # call function
    time = convert(now_time)

    # breakfast 7:00 and 8:00
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    # lunch 12:00 and 13:00
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    #dinner 18:00 and 19:00
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        pass

def convert(time):
    # Get hour and minute
    hours, minutes = time.split(":")

    # Avoid minutes > 59 and convert time into a float number
    minutes = int(minutes)
    if 0 <= minutes <= 59:
        time = float(hours)+float(minutes)/60

    # Return the result
    return time

if __name__ == "__main__":
    main()
```

- **main() Function**:  
  - Prompts for time input and calls `convert()` to get a float representation.  
  - Uses chained `if-elif` to check time ranges and print the meal.  
  - `else: pass` does nothing for non-meal times.

- **convert(time)**:  
  - Splits the input on ":" into hours and minutes.  
  - Validates minutes (0-59) and converts to float: `hours + minutes/60`.  
  - Returns the float; if minutes are invalid, `time` remains a string (potential issue, but assumes valid input).

- **Execution**: Uses `if __name__ == "__main__":` to run `main()` when the script is executed directly.

## How It Works
1. Run the program.
2. Enter a time (e.g., "7:30").
3. Converts to float (7.5).
4. Checks ranges: 7.0-8.0 → "breakfast time".
5. Outputs accordingly; no output for other times.

## Key Concepts Covered in CS50P
- **Functions**: Defining and calling `main()` and `convert()`.
- **Conditionals**: Range checks with `if-elif`.
- **Strings and Numbers**: Splitting strings, type conversion.
- **Input Validation**: Basic check for minutes.
- **Best Practices**: Modular code; could add error handling for invalid formats (e.g., non-numeric input).

## Example Usage
```
What time's it? 7:30
breakfast time

What time's it? 12:00
lunch time

What time's it? 15:00
(no output)
```

This exercise demonstrates converting and comparing times in Python. For the full problem set details, refer to the `problem_set.md` file in the same directory.