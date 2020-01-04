import lottery

def print_blank():
    line = ""
    for _ in range(6):
        line = line + "," + ","
    print(line)
    print(line)
    print(line)

def print_book(book):
    result = ""
    for i in book:
        result = result + i + ","
    print(result.rstrip(','))
    print_blank()

for _ in range(24):
    book = lottery.get_book_of_tickets()
    print_book(book)

book = lottery.magic_book()
print_book(book)
