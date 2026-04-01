class Library:
    def _init_(self, books):
        self.books = books

    def show_books(self):
        print("\nAvailable books:")
        for book in self.books:
            print("-", book.title())

    def checkout(self):
        name = input("Enter the book you are looking for: ").lower()
        if name in self.books:
            print(f"Book '{name.title()}' is available")
        else:
            print("Book not available")

    def lend(self):
        name = input("Enter the book you want to borrow: ").lower()
        if name in self.books:
            self.books.remove(name)
            print("Book borrowed successfully")
        else:
            print("Book not available")

    def return_book(self):
        name = input("Enter the book you are returning: ").lower()
        if name in self.books:
            print("This book is already in the library")
        else:
            self.books.append(name)
            print("Book returned successfully")


books = ["harry potter", "money heist", "charleie"]
lib = Library(books)

while True:
    print("\n1 : Show books")
    print("2 : Check availability")
    print("3 : Lend book")
    print("4 : Return book")
    print("5 : Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.show_books()
    elif choice == "2":
        lib.checkout()
    elif choice == "3":
        lib.lend()
    elif choice == "4":
        lib.return_book()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
