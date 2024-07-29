# LibraryManager.py

# Initialize an empty dictionary to store book details.
library = {}

def add_book(isbn, title, author, publisher, volume, year, isbn_number):
    """Add a book to the library."""
    library[isbn] = {
        'Title': title,
        'Author': author,
        'Publisher': publisher,
        'Volume': volume,
        'Year': year,
        'ISBN': isbn_number
    }
    print(f"Book with ISBN {isbn} added successfully.")

def remove_book(isbn):
    """Remove a book from the library by its ISBN."""
    if isbn in library:
        del library[isbn]
        print(f"Book with ISBN {isbn} removed successfully.")
    else:
        print(f"Book with ISBN {isbn} not found.")

def retrieve_book(isbn):
    """Retrieve and display the details of a book using its ISBN."""
    book = library.get(isbn)
    if book:
        return book
    else:
        return f"Book with ISBN {isbn} not found."

def search_books(query):
    """Search for books by title or author."""
    results = []
    for book in library.values():
        if query.lower() in book['Title'].lower() or query.lower() in book['Author'].lower():
            results.append(book)
    return results

def list_books():
    """List all books currently in the library."""
    return library.values()

def update_book(isbn, title=None, author=None, publisher=None, volume=None, year=None, isbn_number=None):
    """Update the details of an existing book."""
    if isbn in library:
        if title:
            library[isbn]['Title'] = title
        if author:
            library[isbn]['Author'] = author
        if publisher:
            library[isbn]['Publisher'] = publisher
        if volume:
            library[isbn]['Volume'] = volume
        if year:
            library[isbn]['Year'] = year
        if isbn_number:
            library[isbn]['ISBN'] = isbn_number
        print(f"Book with ISBN {isbn} updated successfully.")
    else:
        print(f"Book with ISBN {isbn} not found.")

def check_availability(isbn):
    """Check if a book is available in the library by its ISBN."""
    return isbn in library

# Sample usage:
if __name__ == "__main__":
    # Adding sample books
    add_book('001', 'Ignited Minds', 'A. P. J. Abdul Kalam ','Penguin Books Ltd. ', 1, 2002, '001')
    add_book('002', 'The Monk Who Sold His Ferrari', 'Robin Sharma', 'Pearson', 1, 1999, '002')
    add_book('003', 'It Ends with Us', 'Colleen Hoover', 'Atria Books', 2, 2016, '003')
    add_book('004', 'Thirteen Reasons Why', 'Jay Asher', 'RazorBill', 1, 2021, '004')
    add_book('005', 'Who Will Cry When You Die', 'Robin Sharma', 'JAICO BOOKS', 1, 1999, '005')


    # Listing all books
    print("All books in library:", list_books())

    # Retrieving details of a specific book
    print("Details of book with ISBN 003:", retrieve_book('003'))

    # Searching for books by title
    print("Books with title 'Data Structures':", search_books('It Ends With Us'))

    # Updating book details
    update_book('005', year=2022)

    # Checking availability of a book
    print("Is book with ISBN 002 available?", check_availability('002'))

    # Removing a book
    remove_book('004')
    print("All books in library after removal:", list_books())