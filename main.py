import function

# Run the program
if __name__ == "__main__":
    while True:
        print("\n=== WELCOME TO INDONESIAN LIBRARY ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose action (1-3): ")
        user = function.load_data(function.USERS_FILE)
        
        if choice == "1":
            function.register(user)
            continue
        elif choice == "2":
            role = function.login(user)
        elif choice == "3":
            break
        else:
            print("Input is not valid!")
            continue

        if role["username"] == "admin":
            function.admin_action()
        else:
            function.users_action(role)