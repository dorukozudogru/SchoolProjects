DATA_FILE = 'books.txt'

def read_books():
    books = []
    with open(DATA_FILE, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                books.append({'title': parts[0], 'author': parts[1], 'year': parts[2]})
    return books

def add_book(title, author, year):
    with open(DATA_FILE, 'a') as file:
        file.write(f"{title},{author},{year}\n")
    print("Book added successfully.")

def display_books(books):
    if not books:
        print("No books found.")
    else:
        print(f"{'Title':<30}{'Author':<30}{'Year':<5}")
        print("-" * 65)
        for book in books:
            print(f"{book['title']:<30}{book['author']:<30}{book['year']:<5}")

def search_books(query):
    books = read_books()
    result = [book for book in books if query.lower() in book['title'].lower()]
    return result

def main():
    while True:
        print("\nLibrary Book Tracker")
        print("1. View all books")
        print("2. Add a book")
        print("3. Search books by title")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_books(read_books())
        elif choice == '2':
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter year published (YYYY): ").strip()
            if title and author and year.isdigit() and len(year) == 4:
                add_book(title, author, year)
            else:
                print("Invalid input. Please try again.")
        elif choice == '3':
            query = input("Enter title to search: ").strip()
            results = search_books(query)
            display_books(results)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
