# File Extensions - CS50P Problem Set 1

This exercise is part of **CS50P: Introduction to Programming with Python** at Harvard University, specifically from **Week 1: Conditionals**. It uses conditional statements to determine the MIME type of a file based on its extension, simulating how web servers identify file types.

## Problem Description
The task is to write a program that takes a file name as input and outputs the corresponding MIME type based on the file extension:
- .gif → image/gif
- .jpg or .jpeg → image/jpeg
- .png → image/png
- .pdf → application/pdf
- .txt → text/plain
- .zip → application/zip
- Any other extension → application/octet-stream

The program must handle case-insensitive input.

## Code Explanation
The provided Python code implements this with chained conditionals:

```python
file = input('Insert file: ').strip().lower()

if file.endswith('.gif'):
    print('image/gif')
elif file.endswith('.jpg') or file.endswith(',jpeg'):
    print('image/jpeg')
elif file.endswith('.png'):
    print('image/png')
elif file.endswith('.pdf'):
    print('application/pdf')
elif file.endswith('.txt'):
    print('text/plain')
elif file.endswith('.zip'):
    print('application/zip')
else:
    print('application/octet-stream')
```

- **Input Handling**: `file = input('Insert file: ').strip().lower()`  
  Prompts for a file name, removes whitespace, and converts to lowercase for case-insensitive checks.

- **Conditionals**:  
  - Uses `if-elif-else` to check the file extension with `str.endswith()`.  
  - Note: There is a typo in the code: `file.endswith(',jpeg')` should be `file.endswith('.jpeg')` (comma instead of dot). This would cause incorrect behavior for .jpeg files.

- **Output**: Prints the MIME type based on the extension.

## How It Works
1. Run the program.
2. Enter a file name (e.g., "image.jpg").
3. The program checks the extension and outputs the MIME type (e.g., "image/jpeg").
4. For unknown extensions, defaults to "application/octet-stream".

## Key Concepts Covered in CS50P
- **Conditionals**: Chained `if-elif-else` for multiple options.
- **Strings**: `strip()`, `lower()`, and `endswith()` methods.
- **Input/Output**: Basic user interaction.
- **Best Practices**: Case-insensitive handling; fix the typo for correctness. Could use a dictionary for scalability.

## Example Usage
```
Insert file: cat.jpg
image/jpeg

Insert file: document.pdf
application/pdf

Insert file: unknown.xyz
application/octet-stream
```

This exercise demonstrates practical use of conditionals for file type detection. For the full problem set details, refer to the `problem_set.md` file in the same directory.