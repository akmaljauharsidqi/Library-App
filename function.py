import json

# Initiate file variable
BOOKS_FILE = "books.json"
USERS_FILE = "users.json"

# Load data from JSON file
def load_data(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        if file_name == USERS_FILE:
            return {}
        elif file_name == BOOKS_FILE:
            return []

# Save file to JSON
def save_data(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def login(user):
    print("\n=== LOGIN ===")
    username = input('Username : ')
    password = input('Password : ')
    if username in user and user[username]['password'] == password:
        print(f'Login success, Welcome {username}')
        return user[username]
    else:
        raise ValueError('Login failed, username or password is not correct.')

def register(user):
    print("\n=== REGISTRATION ===")
    username = input("username : ")
    password = input("password : ")
    password_confirmation = input('confirm password : ')
    if password == password_confirmation and username not in user:
        user[username] = {"username" : username, "password" : password, 'borrowed_books' : []}
        save_data(USERS_FILE, user)
        print("Registration success!")
    else:
        raise Exception('Password did not match, or username already in use!')

# Admin action
def admin_action():
    while True:
        print("\n=== LIBRARY MANAGEMENT ===")
        print("1. Add Books")
        print("2. Show Books")
        print("3. Edit Books")
        print("4. Delete Books")
        print("5. Show Users")
        print("6. Delete Users")
        print("7. Log Out")
        choice = input("Choose action (1-7): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            edit_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            show_users()
        elif choice == "6":
            delete_users()
        elif choice == "7":
            break
        else:
            print("Input is not valid!")

# Add book
def add_book():
    books = load_data(BOOKS_FILE)
    
    # Generate ID based on max id in JSON file
    book_id = max([book["id"] for book in books], default=0) + 1
    
    print("\n=== Add Books ===")
    title = input("Book title: ")
    author = input("Author: ")
    year = int(input("Publication year: "))
    
    books.append({"id": book_id, "title": title, "author": author, "year": year, "status": True})
    save_data(BOOKS_FILE, books)
    
    print("Book added successfully!")


# Show books
def show_books():
    books = load_data(BOOKS_FILE)
    if not books:
        print("There are no books to display.")
    else:
        print("\nList of Books:")
        for book in books:
            status = "Available" if book["status"] else "Borrowed"
            print(f"{book['id']}. {book['title']} - {book['author']} ({book['year']}) [{status}]")

# Edit books
def edit_book():
    books = load_data(BOOKS_FILE)
    show_books()
    book_id = int(input("Enter books ID: "))
    for book in books:
        if book["id"] == book_id:
            print("\n=== Edit Books ===")
            book["title"] = input("Book title: ")
            book["author"] = input("Author: ")
            book["year"] = int(input("Publication year: "))
            book["status"] = ask_for_status()
            save_data(BOOKS_FILE, books)
            print("Book was updated successfully!")
            return
    print("Can not find book!")

def ask_for_status():
    while True:
        status_input = input("Is the book available? (yes/no): ").strip().lower()
        if status_input in ['yes', 'y']:
            return True
        elif status_input in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

# Delete Books
def delete_book():
    books = load_data(BOOKS_FILE)
    show_books()
    print("\n=== Delete Books ===")
    book_id = int(input("Enter books ID: "))
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_data(BOOKS_FILE, books)
            print("The book has been successfully deleted!")
            return
    print("Can not find book!")

# Show users
def show_users():
    users = load_data(USERS_FILE)
    books = load_data(BOOKS_FILE)
    if not users:
        print("There are no users to show.")
    else:
        print("\nUsers List:")
        for username, user_data in users.items():
            print(f"Username: {username}")
            borrowed_books = user_data.get("borrowed_books", [])
            if borrowed_books:
                print("  Borrowed books:")
                for book_id in borrowed_books:
                    book = next((b for b in books if b["id"] == book_id), None)
                    if book:
                        print(f"    - {book['id']}. {book['title']} by {book['author']} ({book['year']})")
            else:
                print("  No borrowed books.")


# Delete users
def delete_users():
    users = load_data(USERS_FILE)
    if not users:
        print("There are no users to delete.")
        return
    
    show_users()
    username = input("Input username that want to be deleted: ")
    
    if username in users:
        del users[username]  # Delete the user by key
        save_data(USERS_FILE, users)
        print(f"Users named '{username}' successfully deleted!")
    else:
        print("Can not find user!")
        
        
# Users action
def users_action(user):
    while True:
        print("\n=== INDONESIAN LIBRARY ===")
        print("1. Show Books")
        print("2. Borrow Books")
        print("3. Return Books")
        print("4. Log Out")
        choice = input("Choose action (1-5): ")

        if choice == "1":
            show_books()
        elif choice == "2":
            borrow_books(user)
        elif choice == "3":
            return_books(user)
        elif choice == "4":
            break
        else:
            print("Input is not valid!")

# Borrow Books
def borrow_books(user):
    books = load_data(BOOKS_FILE)
    users = load_data(USERS_FILE)
    users[user["username"]] = user
    print("\n=== Borrow Books ===")
    show_books()

    book_id = int(input("Enter the book ID you want to borrow: "))

    for book in books:
        if book["id"] == book_id:
            if book["status"]:
                book["status"] = False
                user["borrowed_books"].append(book_id)
                save_data(BOOKS_FILE, books)  # Save the updated book list
                save_data(USERS_FILE, users)  # Save the updated user data
                print(f"You have successfully borrowed '{book['title']}'.")
                return
            else:
                print("Sorry, this book is already borrowed.")
                return
    print("Book not found!")
    
def return_books(user):
    books = load_data(BOOKS_FILE)
    print("\n=== Return Books ===")
    
    # Show borrowed books for the user
    if not user["borrowed_books"]:
        print("You have no borrowed books.")
        return
    
    print("Your borrowed books:")
    for book_id in user["borrowed_books"]:
        for book in books:
            if book["id"] == book_id:
                print(f"{book['id']}. {book['title']} - {book['author']} ({book['year']})")
    
    # Ask the user for the book ID they want to return
    book_id = int(input("Enter the book ID you want to return: "))

    users = load_data(USERS_FILE)
    users[user["username"]] = user
    # Check if the book is in the user's borrowed list
    if book_id in user["borrowed_books"]:
        for book in books:
            if book["id"] == book_id:
                book["status"] = True
                user["borrowed_books"].remove(book_id)
                save_data(BOOKS_FILE, books)
                save_data(USERS_FILE, users)  # Save updated users data
                print(f"You have successfully returned '{book['title']}'.")
                return
    else:
        print("You haven't borrowed this book.")
