Lauren Ng

My bookstore contains a small selection of books across five categories: 
Biography and Memoir, Literary Classics, Cooking and Food, Self-Help and History.
The books span a diverse range of authors and genres.
I've designed a bookstore management system that allows users to view all books
and categories, as well as browse books by category and author. Users can also
add new books, delete existing books and update book prices.

To create and populate the database, enter the following lines in the terminal:

sqlite3 bookstore.db < createTables.sql

sqlite3 bookstore.db < insertRows.sql

To run the Python program, enter the following line in the terminal:

python3 bookstore_cli.py 
