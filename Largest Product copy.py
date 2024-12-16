#created by Mayank Parekh

from math import prod

# Get user's input for the digit sequence and series length
def largest_product():
    digits = input("Enter a sequence of digits to be analyzed: ")

    # Convert series length input to an integer
    try:
        length = int(input("Enter the length of the series to be analyzed: "))
    except ValueError:
        raise ValueError("Length input must be a valid integer")

    # Check if digit sequence or series length input is empty
    if not digits:
        raise ValueError("Digits input must not be empty")
    if length <= 0:
        raise ValueError("Length must be a positive integer greater than zero")
    if length > len(digits):
        raise ValueError("Length must not be greater than the length of the digit sequence")

    # Check if the digit sequence contains only digits
    if not digits.isdigit():
        raise ValueError("Digits input must only contain digits")

    max_product = 0

    # Iterate through the digit sequence to calculate the largest product
    for i in range(len(digits) - length + 1):
        series = digits[i:i+length]
        # Use prod to calculate the product of digits in the series
        product = prod(int(char) for char in series)
        max_product = max(max_product, product)
    
    print("The largest product is:", max_product)

# Run the function to prompt for user input
largest_product()
