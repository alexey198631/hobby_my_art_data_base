from nut import database

USER_CHOICE = """
Enter:
- 'a' to add a new artwork
- 'l' to list all artworks
- 'f' to mark a artwork as finished
- 'd' to delete an artwork
- 'q' to quit
Your choice: """


def add_artwork():
    name = input("Enter the new artwork name: ")
    author = input("Enter the new artwork author: ")

    database.add_artwork(name, author)


def list_artworks():
    artworks = database.get_all_artworks()
    for artwork in artworks:
        finished = 'YES' if artwork['finished'] == '1' else 'NO'
        print(f"{artwork['name']} by {artwork['author']}, finished: {artwork['finished']}")


def finish_artwork():
    name = input("Enter the name of the artwork you just finished: ")

    database.mark_artwork_as_finished(name)


def delete_artwork():
    name = input("Enter the name of the artwork you want to remove: ")

    database.delete_artwork(name)


user_options = {
    "a": add_artwork,
    "l": list_artworks,
    "f": finish_artwork,
    "d": delete_artwork
}

def menu():
    database.create_artwork_table()
    selection = input(USER_CHOICE)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(USER_CHOICE)

menu()