import json
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

DATA_FILE = Path("data/transactions.json")

class Transaction:
    def __init__(self, amount, category, description, date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        return Transaction(
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            date=data["date"]
        )

class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.load()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.save()

    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump([t.to_dict() for t in self.transactions], f, indent=2)

    def load(self):
        if DATA_FILE.exists():
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.transactions = [Transaction.from_dict(t) for t in data]

    def get_summary(self):
        total = sum(t.amount for t in self.transactions)
        return {
            "total_spent": total,
            "count": len(self.transactions)
        }

    def list_transactions(self):
        return self.transactions
    
    def filter_by_category(self, category):
        return [t for t in self.transactions if t.category.lower() == category.lower()]

    def filter_by_date(self, date_str):
        return [t for t in self.transactions if t.date == date_str]

    def category_summary(self):
        summary = {}
        for t in self.transactions:
            key = t.category.lower()
            if key not in summary:
                summary[key] = {"total": 0, "count": 0}
            summary[key]["total"] += t.amount
            summary[key]["count"] += 1
        return summary
    
    def plot_category_summary(self):
        summary = self.category_summary()
        if not summary:
            print("No transactions to visualize")
            return
        categories = list(summary.keys())
        totals = [summary[cat]["total"] for cat in categories]

        plt.figure(figsize=(10, 5))
        plt.bar(categories, totals, color="skyblue")
        plt.title("Spending by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Spent ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

