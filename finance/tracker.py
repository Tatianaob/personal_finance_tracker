import json
from datetime import datetime
from pathlib import Path

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
