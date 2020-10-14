# Brian Wolfe                       Created: 09/14/2020

print("-------------------------------------------------------")
print("      Assignment 2A: Simple Calculating Program")
print("-------------------------------------------------------")
print()

operator = int(input("1) to add\n2) to subtract\n3) to multiply\n4) to divide\nEnter a choice: "))
x_value = float(input("\nEnter your first value: "))
y_value = float(input("\nEnter your second value: "))
print()

if operator == 1:
    result = x_value + y_value
elif operator == 2:
    result = x_value - y_value
elif operator == 3:
    result = x_value * y_value
elif operator == 4:
    result = x_value / y_value
else:
    print("Invalid choice entered.")

print(f"Results: {result}")
