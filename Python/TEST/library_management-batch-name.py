class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book_name):
        self.books.append(book_name)
        print(book_name, "has been successfully added.")
        
    def display_books(self):
        if len(self.books) == 0:
            print("No books are available.")
        else:
            print(" Available Books:")
            for book in self.books:
                print(book)
                
     def menu():
         library = Library()
         
         print("===== LIBRARY MANAGEMENT SYSTEM =====")
         print("1. Add Book") 
         print("2. View Available Books")  
         print("3. Issue Book")
         print("4. Return Book")
         print("5. Exit")
         
         choice = input("Enter your choice")
         
         if choice == "1":
             book_name = input("Enter Book Name:")
             library.add_book(book_name)
         
         if choice == "2":
            library.display_book(book_name)