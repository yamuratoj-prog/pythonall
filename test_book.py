from expense_book import ExpenseBook


def test_add_and_total():
    book = ExpenseBook()
    book.add("такси", 3000)
    book.add("кофе", 1500)
    assert book.total() == 4500


def test_top():
    book = ExpenseBook()
    book.add("такси", 3000)
    book.add("кофе", 1500)
    assert book.top() == "такси"


def test_empty_book():
    book = ExpenseBook()
    assert book.total() == 0
    assert book.top() is None


def test_save_and_load(tmp_path):
    filename = tmp_path / "test.json"
    book = ExpenseBook()
    book.add("такси", 3000)
    book.save(filename)

    other = ExpenseBook()
    other.load(filename)
    assert other.total() == 3000