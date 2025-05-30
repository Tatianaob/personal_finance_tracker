import unittest
from finance.tracker import Transaction, FinanceTracker

class TestFinanceTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = FinanceTracker()
        self.tracker.transactions = []  # avoid loading real data

    def test_add_transaction(self):
        t = Transaction(100, "Food", "Groceries")
        self.tracker.add_transaction(t)
        self.assertEqual(len(self.tracker.transactions), 1)
        self.assertEqual(self.tracker.transactions[0].amount, 100)

    def test_filter_by_category(self):
        t1 = Transaction(50, "Food", "Lunch")
        t2 = Transaction(200, "Rent", "April rent")
        self.tracker.transactions = [t1, t2]

        food = self.tracker.filter_by_category("Food")
        self.assertEqual(len(food), 1)
        self.assertEqual(food[0].description, "Lunch")

    def test_filter_by_date(self):
        date = "2025-05-24"
        t1 = Transaction(30, "Transport", "Bus", date=date)
        t2 = Transaction(60, "Transport", "Taxi", date="2025-01-01")
        self.tracker.transactions = [t1, t2]

        result = self.tracker.filter_by_date(date)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].description, "Bus")

    def test_category_summary(self):
        t1 = Transaction(10, "Food", "Snack")
        t2 = Transaction(20, "Food", "Dinner")
        t3 = Transaction(100, "Rent", "April")
        self.tracker.transactions = [t1, t2, t3]

        summary = self.tracker.category_summary()
        self.assertEqual(summary["food"]["count"], 2)
        self.assertEqual(summary["food"]["total"], 30)
        self.assertEqual(summary["rent"]["total"], 100)
    
    def test_empty_transaction_list(self):
        self.assertEqual(len(self.tracker.transactions), 0)
        self.assertEqual(self.tracker.category_summary(), {})

    def test_zero_and_negative_amounts(self):
        zero = Transaction(0, "Misc", "Zero cost")
        negative = Transaction(-50, "Refund", "Returned item")

        self.tracker.transactions = [zero, negative]
        self.assertEqual(self.tracker.transactions[0].amount, 0)
        self.assertEqual(self.tracker.transactions[1].amount, -50)

    def test_filter_by_nonexistent_category(self):
        t1 = Transaction(100, "Food", "Lunch")
        self.tracker.transactions = [t1]
        result = self.tracker.filter_by_category("Clothing")
        self.assertEqual(result, [])

    def test_filter_by_nonexistent_date(self):
        t1 = Transaction(200, "Rent", "April")
        self.tracker.transactions = [t1]
        result = self.tracker.filter_by_date("1999-01-01")
        self.assertEqual(result, [])

    def test_duplicate_transactions(self):
        t1 = Transaction(10, "Snacks", "Chips")
        t2 = Transaction(10, "Snacks", "Chips")  # identical
        self.tracker.transactions = [t1, t2]
        summary = self.tracker.category_summary()
        self.assertEqual(summary["snacks"]["count"], 2)
        self.assertEqual(summary["snacks"]["total"], 20)

if __name__ == '__main__':
    unittest.main()
