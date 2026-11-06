import json


class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.name}: {self.amount}"


class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, name, amount):
        self.expenses.append(Expense(name, amount))

    def total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total

    def top(self):
        if not self.expenses:
            return None
        biggest = max(self.expenses, key=lambda e: e.amount)
        return biggest.name

    def save(self, filename):
        data = [{"name": e.name, "amount": e.amount} for e in self.expenses]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return
        self.expenses = [Expense(item["name"], item["amount"]) for item in data]