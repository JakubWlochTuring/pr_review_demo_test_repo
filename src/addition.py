def add_numbers(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b


def main():
    """Main function to get user input and display the result."""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
