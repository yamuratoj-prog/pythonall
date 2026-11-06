from expense_book import ExpenseBook


def ask_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Введи целое число.")


def main():
    filename = "expenses.json"
    book = ExpenseBook()
    book.load(filename)

    while True:
        print("1. Добавить  2. Показать  3. Итог  4. Выход")
        choice = input("Выбор: ")
        if choice == "1":
            name = input("Название: ").strip().lower()
            amount = ask_int("Сумма: ")
            book.add(name, amount)
            book.save(filename)
        elif choice == "2":
            if not book.expenses:
                print("Трат пока нет")
            for expense in book.expenses:
                print(expense)
        elif choice == "3":
            print(f"Всего: {book.total()}")
            print(f"Самая дорогая: {book.top()}")
        elif choice == "4":
            break
        else:
            print("Нет такого пункта")


if __name__ == "__main__":
    main()