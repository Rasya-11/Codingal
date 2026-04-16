# Write a program to create a menu-driven Library Management System that can do these four tasks - 
# display a book, lend or return a book and add a book. 
# Make use of OOPs concepts, loops and conditional statements wherever required.

# 1) Create a class for a Library system:
#    a) Store a list of books, library name, and a dictionary to track lent books.

class library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

# 2) Add methods in the class:
#    a) Display all available books.
#    b) Lend a book to a user (only if it is not already lent).
#    c) Add a new book to the books list.
#    d) Return a book (remove it from the lent dictionary).

    def displayBooks(self):
        print("These are the books available in the library", self.name)
        for i in self.booklist:
            print(i)
    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender book data base is updated, you can take the book.")
        else:
            print("Book is already being used.")
    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to the book list")
    def returnBook(self, book):
         #Handling books that are not borrowed and are not in the book list
        self.lendDict.pop(book)
        print("Book has been returned")

# 3) Create a Library object with some default books and a library name.

if __name__ == '__main__':
    books = library(["Harry Poter", "Rich Dad, Poor Dad", "Jack and the Beanstalk", "A Good Girl's guide to murder"], "Lets Upskill")

# 4) Run an infinite menu loop:
#    a) Show options: Display, Lend, Add, Return.
#    b) Take user input and validate the choice.

    while(True):
        print("Welcome to the Library", books.name, ".", "Enter your choice to continue.")
        print("1. Display books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        userChoice = input()
        if userChoice not in ['1', '2', '3', '4']:
            print("Please enter a valid option.")
            continue
        else:
            userChoice = int(userChoice)

# 5) Perform actions based on user choice:
#    a) If Display → call display method.
#    b) If Lend → take book + user name, then call lend method.
#    c) If Add → take book name, then call add method.
#    d) If Return → take book name, then call return method.

        if userChoice == 1:
            books.displayBooks()
        elif userChoice == 2:
            book = input("Enter the name of the book you want to lend.")
            user = input("Enter your name.")
            books.lendBook(user, book)
        elif userChoice == 3:
            book = input("Enter the name of the book you want to add.")
            books.addBook(book)
        elif userChoice == 4:
            book = input("Enter the name of the ook you want to return.")
            books.returnBook(book)
        else:
            print("Not a valid option")

# 6) Ask user to quit or continue:
#    a) If 'q' → exit the program.
#    b) If 'c' → continue the menu loop.

        print("Press 'q' to quit and 'c' to continue.")
        userChoice2 = ""
        while(userChoice2 != "c" and userChoice2 != "q"):
            userChoice2 = input()
            if userChoice2 == "q":
                exit()
            elif userChoice2 == "c":
                continue