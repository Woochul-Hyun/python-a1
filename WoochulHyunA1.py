"""
This module is a program of a straightforward perusing list.
The program gets a some user input from the user to track books they want to peruse and book they have finished perusing.
The user can add books which user want to peruse to the perusing list and furthermore stamp books as finished.
In light of the user inputs, the perusing list will be refreshed with the perused and finished status of the books.

Author: Woochul Hyun
Student ID: 13377156
Date: 26th of August, 2017
Github repository: https://github.com/CP1404-JCUS/a1-reading-list-Woochul-Hyun
"""
from operator import itemgetter
FILENAME = "data.csv"
book_list = []


def main():
    """
    The main function reads the CSV file and prints a header containing the program's basic information.

    open the file,"FILENAME", to read and assign it a variable name "organized_file"
    for index, new_list in enumerate (organized_file.readlines ()):
        Use the strip function to remove the space of characters.
        Use the split function to split the data and assign it to a variable "new_data"
        append "book_list" using "new_data".
    closes the opened file.
    display the program name, who made it and number of books in the book list.
    call menu().
    """
    organized_file = open(FILENAME, "r")
    for index, new_list in enumerate(organized_file.readlines()):
        new_list = new_list.strip()
        new_data = new_list.split(",")
        book_list.append(new_data)
    book_list.sort(key=itemgetter(1, 2))
    organized_file.close()
    print("Reading List 1.0 - by Woochul Hyun\n{} books loaded from books.csv".format(len(book_list)))
    menu()

def menu():
    """
    This function receive user input(menu) from the user and connect to the next function that the user chooses.

    display the menu ("Menu:\nR - List required books\nC - List completed books"
                        "\nA - Add new book\nM - Mark a book as completed\nQ - Quit")
    Receive user_input from the user and convert it into uppercase.
    if user_input is "R" or "r":
        display "Required books:"
        call required_books()
    elif user_input is "C" or "c":
        display "Completed books:"
        call completed_books()
    elif user_input is "A" or "a":
        call book_add()
    elif user_input is "M" or "m":
        call mark_book()
    elif user_input is "Q" or "q":
        call add_book_list()
        display how many books saved in data.csv
        display "Have a nice day:"
        exit()
    else:
    display "Invalid menu choice"
    call menu()
    """
    print("Menu:\nR - List required books\nC - List completed books"
          "\nA - Add new book\nM - Mark a book as completed\nQ - Quit")
    user_input = input(">>>").upper()
    if user_input == "R":
        print("Required books:")
        required_books()
    elif user_input == "C":
        print("Completed books:")
        completed_books()
    elif user_input == "A":
        book_add()
    elif user_input == "M":
        mark_book()
    elif user_input == "Q":
        add_book_list()
        print("{} books saved to {}".format(len(book_list), FILENAME))
        print("Have a nice day:)")
        exit()
    else:
        print("Invalid menu choice")
        menu()


def required_books():
    """
    set initial value of unread to 0
    for order_num, new_list in enumerate(book_list):
        if new_list[-1] == "r":
            unread = unread + 1

    if unread == 0:
        display "No books"
    else:
        set initial value of chose_book to 0
        set initial value of pages to 0
        for order_num, new_list in enumerate(book_list):
            if new_list[-1] == "r":
                chose_book = chose_book + 1
                pages = pages + 1
                display the 'order number of book'. 'name of book' by 'author name' 'number of pages'
        display the total number of pages of all books
    call menu()
    """
    unread = 0
    for order_num, new_list in enumerate(book_list):
        if new_list[-1] == "r":
            unread += 1

    if unread == 0:
        print("No books")
    else:
        chose_book = 0
        pages = 0
        for order_num, new_list in enumerate(book_list):
            if new_list[-1] == "r":
                chose_book += 1
                pages += int(new_list[2])
                print(" {}. {:50s} by {:30s} {:<5} pages".format(order_num, new_list[0], new_list[1], new_list[2]))
        print("Total pages for {} books: {}\n".format(chose_book, pages))
    menu()

def completed_books():
    """
    set initial value of unread to 0
    for order_num, new_list in enumerate(book_list):
        if new_list[-1] == "c":
            unread = unread + 1

    if unread == 0:
        display "No books"
    else:
        set initial value of chose_book to 0
        set initial value of pages to 0
        for order_num, new_list in enumerate(book_list):
            if new_list[-1] == "c":
                chose_book = chose_book + 1
                pages = pages + 1
                display the 'order number of book'. 'name of book' by 'author name' 'number of pages'
        display the total number of pages of all books
    call menu()
    """
    unread = 0
    for order_num, new_list in enumerate(book_list):
        if new_list[-1] == "c":
            unread += 1

    if unread == 0:
        print("No  books")
    else:
        chose_book = 0
        pages = 0
        for order_num, new_list in enumerate(book_list):
            if new_list[-1] == "c":
                chose_book += 1
                pages += int(new_list[2])
                print(" {}. {:50s} by {:30s} {:<5} pages".format(order_num, new_list[0], new_list[1], new_list[2]))
        print("Total pages for {} books: {}\n".format(chose_book, pages))
    menu()

def book_add():
    """
    This function adds the books which user want to read to book_list using updated_list.

    Receive user_input for book title from the user
    while book_title == "":
        display "Input cannot be blank"
        Receive user_input for book_title from the user

    Receive user_input for Author from the user
    while author == "":
        display "Input cannot be blank"
        Receive user_input for author from the user

    Set pages_input to None
    while pages_input is None:
        Receive user_input for pages_input from the user
        if page_num == "":
            display "Input cannot be blank"
        else:
            try:
                Receive user_input for pages_input from the user
                if pages_input < 0:
                    display "Number must be >= 0."
                    Set pages_input to None
            except ValueError:
                display "Invalid input: enter a valid number"
    Set book_required to "r"
    Set updated_list to book_title, author, page_num, book_required
    append "book_list" using "updated_list"
    display 'book_title', 'author', 'page_num' is added to reading list
    call menu()
    """
    book_title = input("Title: ")
    while book_title == "":
        print("Input cannot be blank")
        book_title = input("Title: ")

    author = input("Author: ")
    while author == "":
        print("Input cannot be blank")
        author = input("Author: ")

    pages_input = None
    while pages_input is None:
        page_num = input("Pages: ")
        if page_num == "":
            print("Input cannot be blank")
        else:
            try:
                pages_input = int(page_num)
                if pages_input < 0:
                    print("Number must be >= 0.")
                    pages_input = None
            except ValueError:
                print("Invalid input: enter a valid number")

    book_required = "r"
    updated_list = [book_title, author, page_num, book_required]
    book_list.append(updated_list)
    print("{} by {}, ({} pages) added to reading list".format(book_title, author, page_num))
    menu()

def mark_book():
    """
    This function move book from required_books to completed_books.

    set initial value of unread to 0
    for order_num, new_list in enumerate(book_list):
        if new_list[-1] == "r":
            unread = unread + 1

    if unread == 0:
        display "No required books"
        call menu()
    else:
        display "Required books:"
        set initial value of chose_book to 0
        set initial value of pages to 0
        for order_num, new_list in enumerate(book_list):
            if new_list[-1] == "r":
                chose_book = chose_book + 1
                pages = pages + 1
                display the 'order number of book'. 'name of book' by 'author name' 'number of pages'
        display the total number of pages of all books
    Set input2 to False
    while not input2:
        try:
            Set book_name to ""
            Set author_name to ""
            Receive book_required_to_completed to move book from required_books to completed_books
            while book_required_to_completed < 0 or book_required_to_completed >= len(book_list):
                display "Invalid input; enter a valid number"
                Receive book_required_to_completed to move book from required_books to completed_books
            Set input2 to True

            for order_num, new_list in enumerate(book_list):
                if order_num == book_required_to_completed and new_list[-1] == "r":
                    Set new_list[-1] to "c"
                    Set book_name to new_list[0]
                    Set author_name to new_list[1]
                    display the message that 'book_name' by 'author_nam'e marked as completed
                elif order_num == book_required_to_completed and new_list[-1] == "c":
                    display "That book is already completed"
        except ValueError:
            display "invalid input; enter a valid number"
    call menu()
    """
    unread = 0
    for order_num, new_list in enumerate(book_list):
        if new_list[-1] == "r":
            unread += 1

    if unread == 0:
        print("No required books")
        menu()
    else:
        print("Required books:")
        chose_book = 0
        pages = 0
        for order_num, new_list in enumerate(book_list):
            if new_list[-1] == "r":
                chose_book += 1
                pages += int(new_list[2])
                print(" {}. {:50s} by {:30s} {:<5} pages".format(order_num, new_list[0], new_list[1], new_list[2]))
        print("Total pages for {} books: {}\n".format(chose_book, pages))
    input2 = False
    while not input2:
        try:
            book_name = ""
            author_name = ""
            book_required_to_completed = int(input("Enter the number of a book to mark as completed\n>>>"))
            while book_required_to_completed < 0 or book_required_to_completed >= len(book_list):
                print("Invalid input; enter a valid number")
                book_required_to_completed = int(input("Enter the number of a book to mark as completed\n>>>"))
            input2 = True

            for order_num, new_list in enumerate(book_list):
                if order_num == book_required_to_completed and new_list[-1] == "r":
                    new_list[-1] = "c"
                    book_name = new_list[0]
                    author_name = new_list[1]
                    print("{} by {} marked as completed".format(book_name, author_name))
                elif order_num == book_required_to_completed and new_list[-1] == "c":
                    print("That book is already completed")
        except ValueError:
            print("invalid input; enter a valid number")
    menu()

def add_book_list():
    """
    This function add new book whcih user add in data.csv file.

    open the file,"FILENAME", to write and assign it a variable name "updated_file"
    join the the book_list with "," using the 'map' function and assign it a variable file_join
    for each in file_join:
        display updated_file in data.csv file
    close updated_file

    """
    updated_file = open(FILENAME, "w")
    file_join = [','.join(map(str, i)) for i in book_list]
    for each in file_join:
        print(each, file=updated_file)
    updated_file.close()



main()