class Book:
    def __init__(self, title, author, price):
        self.title=title
        self.author=author
        self.price=price
        if not self.is_valid_price(price):
            raise ValueError("Invalid Input.")
    
    @staticmethod
    def is_valid_price(amount):
        return amount>0 and isinstance(amount, (int,float))

    @classmethod
    def from_string(cls, new):
        try:
            title, author, price = new.split(";")
            return cls(title, author, float(price))
        except ValueError:
            raise ValueError("Invalid input string format. Expected format: 'title;author;price'")
    
    def discount_price(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Discount amount must be a non-negative number.")
        return self.price * (1 - amount / 100)
    

def main():
    books = []  # List to store created books

    while True:
        print("\n--- Book Management Menu ---")
        print("1. Add a new book")
        print("2. Add a book from a string")
        print("3. View all books")
        print("4. Apply discount to a book")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Add a new book
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            try:
                price = float(input("Enter book price: ").strip())
                book = Book(title, author, price)
                books.append(book)
                print(f"Book '{title}' added successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            # Add a book from a string
            book_string = input("Enter book details (format: title;author;price): ").strip()
            try:
                book = Book.from_string(book_string)
                books.append(book)
                print(f"Book '{book.title}' added successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            # View all books
            if not books:
                print("No books available.")
            else:
                print("\n--- Book List ---")
                for i, book in enumerate(books, start=1):
                    print(f"{i}. Title: {book.title}, Author: {book.author}, Price: {book.price}")

        elif choice == "4":
            # Apply discount to a book
            if not books:
                print("No books available to apply a discount.")
            else:
                print("\n--- Select a Book to Apply Discount ---")
                for i, book in enumerate(books, start=1):
                    print(f"{i}. Title: {book.title}, Author: {book.author}, Price: {book.price}")
                try:
                    book_index = int(input("Enter the book number: ").strip()) - 1
                    if 0 <= book_index < len(books):
                        discount = float(input("Enter discount percentage: ").strip())
                        discounted_price = books[book_index].discount_price(discount)
                        print(f"Discounted Price of '{books[book_index].title}': {discounted_price}")
                    else:
                        print("Invalid book number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        elif choice == "5":
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
