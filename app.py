from nut import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """


def add_book ():
    name = input("Enter the new book name: ")
    author = input("Enter the new book author: ")

    database.add_book(name,author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] == '1' else 'NO'
        print(f"{book['name']} by {book['author']}, read: {book['read']}")


def read_book():
    name = input("Enter the name of the book you just finished reading: ")

    database.mark_book_as_read(name)


def delete_book():
    name = input("Enter the name of the book you want to remove: ")

    database.delete_book(name)


user_options = {
    "a" : add_book,
    "l" : list_books,
    "r" : read_book,
    "d" : delete_book
}

def menu():
    database.create_book_table()
    selection = input(USER_CHOICE)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(USER_CHOICE)

menu()