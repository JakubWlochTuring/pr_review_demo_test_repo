class MathOperations:
    """A simple class for basic mathematical operations."""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

if __name__ == "__main__":
    print("Math Operations")
    print(f"2 + 3 = {MathOperations.add(2, 3)}")
    print(f"5 - 2 = {MathOperations.subtract(5, 2)}")
    print(f"4 * 3 = {MathOperations.multiply(4, 3)}")
    print(f"10 / 2 = {MathOperations.divide(10, 2)}")
