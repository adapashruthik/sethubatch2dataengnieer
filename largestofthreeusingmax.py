# Program to determine the largest of three inputs without using the max() function.
# This program uses a nested ternary operator for finding the largest value.
print("--- Determine the Largest of Three Inputs ---")

# Function to get input and determine the largest using a nested ternary operator
def find_largest_of_three():
    try:
    # Get three inputs from the user
    # Using eval() for flexibility as inputs can be numbers, strings, lists, etc.
    # NOTE: eval() carries security risks if used with untrusted input.
    # For this homework, it's used to match the varied input types.
    input1_str = input("Enter the first input for largest of three: ")
    input2_str = input("Enter the second input for largest of three: ")
    input3_str = input("Enter the third input for largest of three: ")

    val1 = eval(input1_str)
    val2 = eval(input2_str)
    val3 = eval(input3_str)

    # Determine the largest using a nested ternary operator
    # Logic:
    # If val1 is greater than val2:
    #   Then compare val1 with val3. If val1 > val3, val1 is largest, else val3 is largest.
    # Else (val2 is greater than or equal to val1):
    #   Then compare val2 with val3. If val2 > val3, val2 is largest, else val3 is largest.
    largest = val1 if val1 > val2 else val2
    largest = largest if largest > val3 else val3

    # Alternatively, a single nested ternary (more compact but harder to read for complex logic):
    # largest = val1 if val1 > val2 and val1 > val3 \
    #           else (val2 if val2 > val1 and val2 > val3 else val3)
    # A simpler single line for three distinct values:
    # largest = val1 if val1 > val2 and val1 > val3 else \
    #           (val2 if val2 > val3 else val3)


    print(f"The inputs are: {val1}, {val2}, {val3}")
    print(f"The largest value is: {largest}")
except SyntaxError:
    print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text', [1,2]).")
except NameError as e:
    print(f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA').")
except TypeError as e:
    print(f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to print '>', '<', or '=' based on the comparison of two inputs.
# This program uses a ternary operator.
print("\n--- Compare Two Inputs ---")

def compare_two_inputs():
try:
    input1_str = input("Enter the first input for comparison: ")
    input2_str = input("Enter the second input for comparison: ")

    val1 = eval(input1_str)
    val2 = eval(input2_str)

    # Use a ternary operator to determine the comparison result
    result = '>' if val1 > val2 else ('<' if val1 < val2 else '=')

    print(f"Comparing {val1} and {val2}: {result}")

except SyntaxError:
    print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text', [1,2]).")
except NameError as e:
    print(f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA').")
except TypeError as e:
    print(f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to determine the sign of a number (+1, -1, or 0).
# This program uses a nested ternary operator.
print("\n--- Determine Number Sign ---")

def determine_sign():
try:
    num_str = input("Enter a number to determine its sign: ")
    num = float(num_str) # Convert to float to handle decimals and integers

    # Use a nested ternary operator to determine the sign
    # Logic:
    # If num > 0, result is 1
    # Else (num <= 0):
    #   If num < 0, result is -1
    #   Else (num == 0), result is 0
    sign = 1 if num > 0 else (-1 if num < 0 else 0)

    print(f"The sign of {num} is: {sign}")

except ValueError:
    print("Invalid input: Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to test if an input number is even or odd.
# This program uses a ternary operator.
print("\n--- Check Even or Odd Number ---")

def check_even_odd():
try:
    num_str = input("Enter an integer to check if it's even or odd: ")
    num = int(num_str) # Convert to integer

    # Use a ternary operator to determine if the number is even or odd
    # An even number is divisible by 2 (remainder is 0).
    # An odd number is not divisible by 2 (remainder is not 0).
    result = "Even" if num % 2 == 0 else "Odd"

    print(f"The number {num} is: {result}")

except ValueError:
    print("Invalid input: Please enter a valid integer number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to determine area and perimeter of a rectangle.
print("\n--- Calculate Rectangle Area and Perimeter ---")

def calculate_rectangle_properties():
try:
    length_str = input("Enter the length of the rectangle: ")
    breadth_str = input("Enter the breadth of the rectangle: ")

    length = float(length_str)
    breadth = float(breadth_str)

    if length < 0 or breadth < 0:
        print("Length and breadth cannot be negative.")
        return

    area = length * breadth
    perimeter = 2 * (length + breadth)

    print(f"For a rectangle with length {length} and breadth {breadth}:")
    print(f"Area = {area}")
    print(f"Perimeter = {perimeter}")

except ValueError:
    print("Invalid input: Please enter valid numbers for length and breadth.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to determine the volume of a sphere.
import math # Import math module for pi and power

print("\n--- Calculate Sphere Volume ---")

def calculate_sphere_volume():
try:
    radius_str = input("Enter the radius of the sphere: ")
    radius = float(radius_str)

    if radius < 0:
        print("Radius cannot be negative.")
        return

    # Volume of sphere formula: (4/3) * pi * r^3
    volume = (4/3) * math.pi * (radius ** 3)

    print(f"For a sphere with radius {radius}:")
    print(f"Volume = {volume}")

except ValueError:
    print("Invalid input: Please enter a valid number for the radius.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to determine simple interest and compound interest.
print("\n--- Calculate Simple and Compound Interest ---")

def calculate_interest():
try:
    principal_str = input("Enter the principal amount (P): ")
    time_str = input("Enter the time in years (T): ")
    rate_str = input("Enter the annual rate of interest (R, as a percentage): ")

    principal = float(principal_str)
    time = float(time_str)
    rate = float(rate_str)

    if principal < 0 or time < 0 or rate < 0:
        print("Principal, time, and rate cannot be negative.")
        return

    # Simple Interest Formula: (P * T * R) / 100
    simple_interest = (principal * time * rate) / 100

    # Compound Interest Formula: P * (1 + R / 100)^T - P
    # Note: (1 + R/100) is the growth factor per period
    compound_interest = principal * ((1 + rate / 100) ** time) - principal

    print(f"For Principal = {principal}, Time = {time} years, Rate = {rate}%:")
    print(f"Simple Interest = {simple_interest:.2f}") # Format to 2 decimal places
    print(f"Compound Interest = {compound_interest:.2f}") # Format to 2 decimal places

except ValueError:
    print("Invalid input: Please enter valid numbers for principal, time, and rate.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to swap values of two objects using a third object.
print("\n--- Swap Two Objects (using a third object) ---")

def swap_with_third_object():
try:
    # Get two inputs from the user
    # Using eval() for flexibility as inputs can be numbers, strings, lists, etc.
    # NOTE: eval() carries security risks if used with untrusted input.
    input_x_str = input("Enter the value for x: ")
    input_y_str = input("Enter the value for y: ")

    x = eval(input_x_str)
    y = eval(input_y_str)

    print(f"Before swap: x = {x}, y = {y}")

    # Perform the swap using a third temporary variable
    temp = x
    x = y
    y = temp

    print(f"After swap: x = {x}, y = {y}")

except SyntaxError:
    print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text', [1,2]).")
except NameError as e:
    print(f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA').")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# --- Call the functions to run the programs ---

# Call the function to run the largest of three program with user input
find_largest_of_three()

# Call the function to run the two input comparison program with user input
compare_two_inputs()

# Call the function to run the number sign determination program with user input
determine_sign()

# Call the function to run the even/odd check program with user input
check_even_odd()

# Call the function to run the rectangle properties calculation program with user input
calculate_rectangle_properties()

# Call the function to run the sphere volume calculation program with user input
calculate_sphere_volume()

# Call the function to run the interest calculation program with user input
calculate_interest()

# Call the function to run the swap with third object program with user input
swap_with_third_object()

