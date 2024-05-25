from swap import swap_numbers

a = int(input("Enter first number (0-3): "))
b = int(input("Enter second number (0-3): "))

swapped_a, swapped_b = swap_numbers(a, b)
print(f"The two swapped numbers are: {swapped_a} and {swapped_b}")