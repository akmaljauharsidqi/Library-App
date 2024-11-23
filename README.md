📚 Indonesian Library Management System
This project is a simple Library Management System implemented in Python. The application allows users to register, log in, and manage library activities such as borrowing and returning books. It also includes an admin panel for managing books and user accounts.

💡 Features
For Users
Registration: Create a new account with a username and password.
Login: Authenticate using registered credentials.
View Books: See the list of books and their availability status.
Borrow Books: Borrow available books.
Return Books: Return borrowed books.
For Admins
Add Books: Add new books to the library.
View Books: View a detailed list of all books.
Edit Books: Update book details such as title, author, and availability.
Delete Books: Remove books from the system.
Manage Users: View or delete user accounts.
🛠️ Prerequisites
Python 3.x installed on your system.
JSON files for storing user and book data:
users.json: Stores user data (auto-generated if not found).
books.json: Stores book data (auto-generated if not found).
🚀 Getting Started
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/library-app.git
cd library-app
2. Install Python
Make sure you have Python 3.x installed. Verify using:

bash
Copy code
python --version
3. Run the Program
Execute the main script:

bash
Copy code
python main.py
📂 File Structure
bash
Copy code
.
├── main.py            # Main script for the application
├── function.py        # Contains all helper functions and core logic
├── books.json         # Stores book information (auto-generated)
├── users.json         # Stores user information (auto-generated)
└── README.md          # Documentation


📝 Acknowledgments
Built using Python and JSON for data storage.
Inspired by the need for a simple library management tool.😊
