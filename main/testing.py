#!/usr/bin/python3

# Dictionary to store user data (simulated database)
users = {}

# List to store uploaded artwork names
artworks = []

# Function to handle user sign up
def sign_up():
    full_name = input("Enter your full name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in users:
        print("User already exists. Please sign in.")
    else:
        users[email] = {"full_name": full_name, "password": password}
        print("User successfully registered.")

# Function to handle user sign in
def sign_in():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in users and users[email]["password"] == password:
        print("Login successful.")
        return email
    else:
        print("Invalid credentials.")
        return None

# Function to display main menu
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. See List of Artwork")
        print("2. Upload Artwork")
        print("3. Search Artwork")
        print("4. View Profile")
        print("5. Delete Account")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            see_artwork_list()
        elif choice == "2":
            upload_artwork()
        elif choice == "3":
            search_artwork()
        elif choice == "4":
            view_profile()
        elif choice == "5":
            delete_account()
            break
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please select again.")

# Function to see list of artwork
def see_artwork_list():
    print("\nList of Artwork:")
    for artwork in artworks:
        print(artwork)

# Function to upload artwork
def upload_artwork():
    filename = input("Enter the filename to upload: ")
    artworks.append(filename)
    print("Artwork uploaded successfully.")

# Function to search artwork
def search_artwork():
    search_term = input("Enter the name of artwork to search: ")
    matching_artworks = [artwork for artwork in artworks if search_term in artwork]
    if matching_artworks:
        print("Matching artworks:")
        for artwork in matching_artworks:
            print(artwork)
    else:
        print("{} does not exist.".format(search_term))

# Function to view profile
def view_profile():
    print("\nProfile:")
    print("Full Name:", users[current_user]["full_name"])
    print("Email:", current_user)

# Function to delete account
def delete_account():
    choice = input("Are you sure you want to delete your account? (yes/no): ")
    if choice.lower() == "yes":
        del users[current_user]
        print("Account deleted successfully.")

# Main program
current_user = None

while True:
    print("\nWelcome to Your Art App")
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Quit")

    initial_choice = input("Enter your choice: ")

    if initial_choice == "1":
        sign_up()
    elif initial_choice == "2":
        current_user = sign_in()
        if current_user:
            main_menu()
    elif initial_choice == "3":
        break
    else:
        print("Invalid choice. Please select again.")
