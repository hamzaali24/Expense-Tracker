class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, item, amount, category):
        self.expenses.append({'item': item, 'amount': amount, 'category': category})

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        return total

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        print("Expense Tracker:")
        print("-----------------")
        for index, expense in enumerate(self.expenses, start=1):
            print(f"{index}. Item: {expense['item']}, Amount: ${expense['amount']}, Category: {expense['category']}")
        print("-----------------")
        print(f"Total Expenses: ${self.total_expenses()}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            item = input("Enter item name: ")
            amount = float(input("Enter amount spent: "))
            category = input("Enter category: ")
            tracker.add_expense(item, amount, category)
            print("Expense added successfully!")
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
