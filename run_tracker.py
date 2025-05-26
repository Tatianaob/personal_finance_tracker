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
        print("6. Category summary")
        print("7. Show category plot")
        print("8. Exit")

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
            category = input("Enter category to filter by: ")
            results = tracker.filter_by_category(category)
            if results:
                for t in results:
                    print(f"{t.date} | ${t.amount:.2f} | {t.category} | {t.description}")
            else:
                print("No transactions found for this category.")

        elif choice == "5":
            date = input("Enter date to filter by (YYYY-MM-DD): ")
            results = tracker.filter_by_date(date)
            if results:
                for t in results:
                    print(f"{t.date} | ${t.amount:.2f} | {t.category} | {t.description}")
            else:
                print("No transactions found for this date.")

        elif choice == "6":
            summary = tracker.category_summary()
            if summary:
                print("\nCategory Summary:")
                for cat, data in summary.items():
                    print(f"{cat.capitalize()}: {data['count']} transactions, ${data['total']:.2f}")
            else:
                print("No transactions to summarize.")

        elif choice == "7":
            tracker.plot_category_summary()
            
        elif choice == "8":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
