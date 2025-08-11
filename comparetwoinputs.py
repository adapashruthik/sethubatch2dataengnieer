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