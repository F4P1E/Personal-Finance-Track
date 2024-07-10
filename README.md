
# Finance Tracker

This project is a simple finance tracker that allows users to input financial transactions, including income and expenses. The program collects the date, amount, category, and an optional description for each transaction.

## Features

- Input and validate transaction dates
- Input and validate transaction amounts
- Categorize transactions as income or expense
- Add optional descriptions to transactions

## Requirements

- Python 3.x

## Usage

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd finance-tracker
   ```

2. **Run the Program:**

   Run the `main.py` script to start the finance tracker.

   ```bash
   python main.py
   ```

3. **Enter Transaction Details:**

   - **Date:** Enter the date of the transaction in `dd-mm-yyyy` format. If no date is entered, the current date will be used by default (if allowed).
   - **Amount:** Enter the transaction amount as a positive, non-zero value.
   - **Category:** Enter the category of the transaction ('I' for Income or 'E' for Expense).
   - **Description:** Enter an optional description for the transaction.

## Functions

### `get_date(prompt, allow_default=False)`

Prompt the user for a date input and return the date in the specified format. If `allow_default` is `True` and the input is empty, the current date is returned.

### `get_amount()`

Prompt the user for an amount and ensure it is a non-negative, non-zero value.

### `get_category()`

Prompt the user to enter a category ('I' for Income or 'E' for Expense).

### `get_description()`

Prompt the user for an optional description of the transaction.

## Example

```python
from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)

    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()

def get_description():
    return input("Enter a description (optional): ")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
