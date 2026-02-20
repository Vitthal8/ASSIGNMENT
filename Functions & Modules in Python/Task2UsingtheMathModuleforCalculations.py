import math

try:
    num = float(input("Enter a number: "))


    if num <= 0:
        print("Please enter a number greater than 0 to calculate the square root and natural logarithm.")
    else:
        # 2. Calculate using the math module
        square_root = math.sqrt(num)
        natural_log = math.log(num)
        sine_val = math.sin(num)  # math.sin naturally expects the input in radians


        print(f"Square root: {square_root}")
        print(f"Natural logarithm: {natural_log}")
        print(f"Sine: {sine_val}")

except ValueError:
    print("Invalid input! Please enter a valid numerical value.")