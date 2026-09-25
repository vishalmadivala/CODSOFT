"""
Simple Calculator
CodSoft Python Programming Internship - Task 2

Prompts the user for two numbers and an operation, then performs the
calculation and displays the result. Supports repeated calculations
in a single session.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "1": ("Add (+)", add),
    "2": ("Subtract (-)", subtract),
    "3": ("Multiply (*)", multiply),
    "4": ("Divide (/)", divide),
}


def get_number(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Please try again.")


def show_menu():
    print("\nSelect an operation:")
    for key, (label, _) in OPERATIONS.items():
        print(f"  {key}. {label}")


def main():
    print("=" * 40)
    print("SIMPLE CALCULATOR".center(40))
    print("=" * 40)

    while True:
        show_menu()
        choice = input("Enter choice (1-4): ").strip()

        if choice not in OPERATIONS:
            print("Invalid operation choice. Please select 1-4.")
        else:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            label, func = OPERATIONS[choice]
            try:
                result = func(num1, num2)
                op_symbol = label.split("(")[1].strip(")")
                print(f"\nResult: {num1} {op_symbol} {num2} = {result}")
            except ZeroDivisionError as e:
                print(f"Error: {e}")

        again = input("\nPerform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for using the calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
