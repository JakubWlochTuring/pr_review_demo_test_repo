def authenticate_user(username, password):
    """
    Authenticates a user using hardcoded credentials.
    Potential Issue:
    - Security Threat: Using hardcoded credentials and no password hashing.
    """
    if username == "admin" and password == "password":
        return True
    return False


def process_data(user_input):
    """
    Processes user input by evaluating it.
    Potential Issue:
    - Security Threat: Using eval() on untrusted input may allow code injection.
    """
    try:
        result = eval(user_input)
        return result
    except Exception:
        return None


def calculate_total(prices, tax_rate):
    """
    Calculates the total amount including tax.
    Potential Issue:
    - Logical Issue: Tax calculation is incorrect. Instead of multiplying the total
      by the tax rate, it incorrectly adds a fixed tax_rate/100 to the sum.
    """
    total = sum(prices)
    total_with_tax = total + (tax_rate / 100)  # Bug: should be total + (total * tax_rate / 100)
    return total_with_tax


def write_data_to_file(data, filepath):
    """
    Writes data to a specified file.
    Potential Issue:
    - Security Threat: No validation or sanitization of the filepath can lead to path traversal vulnerabilities.
    """
    try:
        with open(filepath, 'w') as file:
            file.write(data)
        return True
    except Exception:
        return False


# Example usage:
if __name__ == '__main__':
    print("Authentication:", authenticate_user("admin", "password"))
    print("Process Data:", process_data("2 + 3 * 4"))
    print("Calculate Total:", calculate_total([10, 20, 30], 10))
    print("Write to File:", write_data_to_file("Hello, world!", "test.txt"))
