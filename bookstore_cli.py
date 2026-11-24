import sqlite3
db_name = "bookstore.db"

def pause() -> None:
    input("\nPress Enter/Return to go back to the menu...")

def print_menu() -> None:
    print("Welcome to the bookstore!")
    print("1. View all categories")
    print("2. View all books")
    print("3. View books in a category")
    print("4. Search books by title")
    print("5. Search books by author")
    print("6. Add a new book")
    print("7. Update a book price")
    print("8. Delete a book")
    print("9. Quit")

def view_categories(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        """
        SELECT *
        FROM category
        """
    )
    rows = cursor.fetchall()
    print()
    print("Categories:")

    if rows:
        for row in rows:
            print(row)
    else:
        print("No categories found.")


def view_books(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        """
        SELECT bookId, title, author, price, bookImage, readNow
        FROM book
        """
    )
    rows = cursor.fetchall()

    print()
    print("Books:")

    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found.")

def view_books_in_category(cursor: sqlite3.Cursor) -> None:
    category_name = input("Enter a category name: ").strip()

    cursor.execute(
        """
        SELECT book.bookId, book.title, book.author, book.price, book.bookImage
        FROM book
        JOIN category ON book.categoryId = category.categoryId
        WHERE LOWER(category.categoryName) = LOWER(?)
        ORDER BY book.title
        """,
        (category_name,)
    )
    rows = cursor.fetchall()

    print()
    print(f"Books in {category_name.capitalize()}:")

    if rows:
        for row in rows:
            print(row)
    else:
        print("Category does not exist or contains no books.")

def search_by_title(cursor: sqlite3.Cursor) -> None:
    keyword = input("Enter a title keyword: ").strip()

    cursor.execute(
        """
        SELECT bookId, title, author, price, bookImage
        FROM book
        WHERE title LIKE ?
        ORDER BY title
        """,
        (f"%{keyword}%",)
    )
    rows = cursor.fetchall()

    print()
    print("Matching books:")

    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found.")

def search_by_author(cursor: sqlite3.Cursor) -> None:
    author = input("Enter an author's name or keyword: ").strip()

    cursor.execute(
        """
        SELECT bookId, title, author, price, bookImage
        FROM book
        WHERE author LIKE ?
        ORDER BY author, title
        """,
        (f"%{author}%",)
    )
    rows = cursor.fetchall()

    print()
    print(f"Books by authors matching '{author}':")

    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found for that author.")

def add_book(cursor: sqlite3.Cursor) -> None:
    try:
        category_id = int(input("Enter category id: ").strip())
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        isbn = input("Enter ISBN: ").strip()
        price = float(input("Enter price: ").strip())
        image = input("Enter image filename: ").strip()
        read_now = int(input("Is the book currently being read? Enter 0 for no and 1 for yes): ").strip())

        cursor.execute(
            """
            INSERT INTO book (categoryId, title, author, isbn, price, bookImage, readNow)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (category_id, title, author, isbn, price, image, read_now)
        )

        print()
        print("Book added.")

    except ValueError:
        print()
        print("Invalid input.")
    except sqlite3.IntegrityError as error:
        print()
        print("Database error:", error)

def update_price(cursor: sqlite3.Cursor) -> None:
    try:
        book_id = int(input("Enter book id: ").strip())
        new_price = float(input("Enter the new price: ").strip())

        cursor.execute(
            """UPDATE book 
            SET price = ? 
            WHERE bookId = ?
            """,
            (new_price, book_id)
        )

        print()
        if cursor.rowcount == 0:
            print("No book was found, so no price was updated.")
        else:
            print("Price updated.")

    except ValueError:
        print()
        print("Invalid input.")

def delete_book(cursor: sqlite3.Cursor) -> None:
    try:
        book_id = int(input("Enter book id to delete: ").strip())

        cursor.execute(
            """
            DELETE 
            FROM book 
            WHERE bookId = ?
            """,
            (book_id,)
        )

        print()
        if cursor.rowcount == 0:
            print("No book was found.")
        else:
            print("Book deleted.")

    except ValueError:
        print()
        print("Invalid input.")

def main() -> None:

    with sqlite3.connect(db_name) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()

        while True:
            print_menu()
            choice = input("\nChoose an option (enter a value from 1-9): ").strip()

            if choice == "1":
                view_categories(cursor)
                pause()
            elif choice == "2":
                view_books(cursor)
                pause()
            elif choice == "3":
                view_books_in_category(cursor)
                pause()
            elif choice == "4":
                search_by_title(cursor)
                pause()
            elif choice == "5":
                search_by_author(cursor)
                pause()
            elif choice == "6":
                add_book(cursor)
                pause()
            elif choice == "7":
                update_price(cursor)
                pause()
            elif choice == "8":
                delete_book(cursor)
                pause()
            elif choice == "9":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
                pause()

if __name__ == "__main__":
    main()
