from swap import swap_numbers
from extras.desc import print_descending

def main():
    a = int(input("Enter first number (0-3): "))
    b = int(input("Enter second number (0-3): "))

    swapped_a, swapped_b = swap_numbers(a, b)
    print(f"The two swapped numbers are: {swapped_a} and {swapped_b}")

    n = int(input("Enter a number to print descending order: "))
    print("Natural descending order is:")
    print_descending(n)

if __name__ == "__main__":
    main()
