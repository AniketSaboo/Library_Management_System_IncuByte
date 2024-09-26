from library import Library

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. List available books")
        print("6. List borrowed books")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            # publication_year=input("Enter the publication year")
            # publication_year=in
            publication_year=input("Enter the publication year")
            isbn = input("Enter book ISBN: ")

            book = library.add_book(title, author,publication_year,isbn)
            print(f"Book added: {book}")

        elif choice == '2':
            isbn = input("Enter book ISBN to remove: ")
            book = library.remove_book(isbn)
            if book:
                print(f"Book removed: {book}")
            else:
                print("Book not found.")

        elif choice == '3':
            isbn = input("Enter book ISBN to borrow: ")
            book = library.borrow_book(isbn)
            if book:
                print(f"Book borrowed: {book}")
            else:
                print("Book not available or not found.")

        elif choice == '4':
            isbn = input("Enter book ISBN to return: ")
            book = library.return_book(isbn)
            if book:
                print(f"Book returned: {book}")
            else:
                print("Book not found or already returned.")

        elif choice == '5':
            available_books = library.list_available_books()
            if available_books:
                print("Available books:")
                for book in available_books:
                    print(book)
            else:
                print("No available books.")

        elif choice == '6':
            borrowed_books = library.list_borrowed_books()
            if borrowed_books:
                print("Borrowed books:")
                for book in borrowed_books:
                    print(book)
            else:
                print("No borrowed books.")

        elif choice == '7':
            print("Thank you for using the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()