from Expense import Expense

separator = "=" * 50

def main():
    print(f"""{separator}\n\n Running Expense Tracker!\n""")

    expense_file_path = "expenses.csv"

    #Get user input for expense.
    expense = get_user_expense()

    #Write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    #Read file and summarize expense.
    summarize_expenses(expense_file_path)

    #Repearing the process and continue adding data
    continue_input(expense, expense_file_path)

def get_use_expense():


def save_expense_to_file():


def summarize_expenses():


def continue_input():




if __name__ == "_main_":
    main()