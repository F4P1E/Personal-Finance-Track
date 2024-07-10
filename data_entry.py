from datetime import datetime

# Define the date format to be used throughout the program
date_format = "%d-%m-%Y"
# Define the categories for transactions, with 'I' for income, 'E' for expense
CATEGORIES = {"I": "Income", "E": "Expense"}


def get_date(prompt, allow_default=False):
    """
    Prompt the user for a date input and return the date in the specified format.
    If allow_default is True and the user enters an empty string, the current date will be returned.
    """
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)

    try:
        # Try to parse the input date string
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        # Handle invalid date format
        print("Invalid date frmat. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)


def get_amount():
    """
    Prompt the user for an amount and ensure it is a non-negative non-zero value.
    """
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        # Handle invalid amount input
        print(e)
        return get_amount()


def get_category():
    """
    Prompt the user to enter a category('I' for income or 'E' for expense).
    """
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    # Handle invalid category input
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()


def get_descriptipn():
    """
    Prompt the user for a description.
    """
    return input("Enter a description (optional): ")