import json
import os

# File path for saving the library
data_file = 'library-manager.txt'

# Load the library if file exists
def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []  # Return empty list if file doesn't exist

# Save the library to the file
def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)  # Added indent for readability

# Add a new book to the library
def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    readStatus = input('Have you read the book? (yes/no): ').lower() == "yes" 

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "readStatus": readStatus
    }

    library.append(new_book)  # Add book to the library
    save_library(library)     # Save updated library
    print(f"Book '{title}' added successfully!")

def library_remove(library):  # Removes book from the library
    title = input("Enter the title of the book to remove from the library: ")
    initial_length = len(library)

    # Filter out the book with the matching title (case-insensitive)
    library[:] = [book for book in library if book['title'].lower() != title.lower()]

    if len(library) < initial_length:
        save_library(library)
        print(f"Book '{title}' removed successfully!")
    else:
        print(f"Book '{title}' not found in the library!")

def library_search(library):
    search = input("Enter the title or author of the book to search: ").lower()
    results = [book for book in library if search in book['title'].lower() or search in book['author'].lower()]

    if results:
        print("Search Results:")
        for book in results:
            print(f"Title: {book['title']}, Author: {book['author']}")
    else:
        print("No books found matching your search.")

def display_books(library):
    if library:
        for book in library:
            status="Read" if book['readStatus'] else "unread"
            print(f"{book['title']} by {book['author']}-{book['year']}-{book['genre']}-{status}")
        else:
            print()

def display_statistics(library):
    total_books = len(library)  # Total number of books in the library
    read_books = len([book for book in library if book['readStatus']])  
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0  # Calculate percentage

    # Display the statistics
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage of books read: {percentage_read:.2f}%")

def main():
    library = load_library()
    
    while True:
        print("Welcomne to your Personal Library Manager!!")
        print("\nMenu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search the library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter a number to proceed: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            library_remove(library)
        elif choice == '3':
            library_search(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Exiting the program.")
            break  
        else:
            print(" Please enter a valid number from the menu.")

if __name__ == '__main__':
    main() 