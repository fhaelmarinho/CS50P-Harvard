expression = input('Insert the math expression: ').strip()

x, y, z = expression.split()  # "1" "+" "1"
if y == "+":
    calc = int(x) + int(z)
elif y == "-":
    calc = int(x) - int(z)
elif y == "*":
    calc = int(x) * int(z)
elif y == "/" and (z != 0):
    calc = int(x) / int(z)
else:
    print("Error")
print(float(calc))
