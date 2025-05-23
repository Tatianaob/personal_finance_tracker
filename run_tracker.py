from finance.tracker import FinanceTracker, Transaction

def main():
    tracker = FinanceTracker()

    while True:
        print("\n==== Personal Finance Tracker ====")
        print("1. Add transaction")
        print("2. View all transactions")
        print("3. Show summary")
        print("4. Filter by category")
        print("5. Filter by date")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Amount: "))
                category = input("Category: ")
                description = input("Description: ")
                transaction = Transaction(amount, category, description)
                tracker.add_transaction(transaction)
                print("✅ Transaction added.")
            except ValueError:
                print("❌ Invalid amount.")
        elif choice == "2":
            for t in tracker.list_transactions():
                print(f"{t.date} | ${t.amount:.2f} | {t.category} | {t.description}")
        elif choice == "3":
            summary = tracker.get_summary()
            print(f"Total transactions: {summary['count']}")
            print(f"Total spent: ${summary['total_spent']:.2f}")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
