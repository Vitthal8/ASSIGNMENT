def factorial(n):

    if n < 0:
        return "Undefined for negative numbers"

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



try:
    # 1. Take input from the user to match the screenshot prompt
    user_input = int(input("Enter a number: "))

    # 2. Call the function
    calculated_factorial = factorial(user_input)


    print(f"Factorial of {user_input} is: {calculated_factorial}")

except ValueError:
    print("Please enter a valid integer.")