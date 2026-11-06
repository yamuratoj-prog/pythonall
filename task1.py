class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.name}: {self.amount}"


def main():
    e = Expense("такси", 3000)
    print(e)
    print(e.name)
    print(e.amount)


if __name__ == "__main__":
    main()