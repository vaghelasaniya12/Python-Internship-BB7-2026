
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(book_name, "has been added successfully.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books are available.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print("-", book)

    def issue_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(book_name, "has been issued successfully.")
        else:
            print("Sorry! Book is not available.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(book_name, "has been returned successfully.")



def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Available Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_name = input("Enter book name: ")
            library.add_book(book_name)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            book_name = input("Enter book name to issue: ")
            library.issue_book(book_name)

        elif choice == "4":
            book_name = input("Enter book name to return: ")
            library.return_book(book_name)

        elif choice == "5":
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


main()
