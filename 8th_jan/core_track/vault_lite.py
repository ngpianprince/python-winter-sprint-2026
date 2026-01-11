import json
import os

FILE_NAME = "vault_data.json"


# Load data from file
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# View saved credentials
def view_credentials():
    data = load_data()
    if not data:
        print("\nNo credentials found.\n")
        return

    print("\nSaved Credentials:")
    for i, cred in enumerate(data, start=1):
        print(f"{i}. Website: {cred['website']} | Username: {cred['username']}")
    print()


# Add new credential
def add_credential():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    data = load_data()
    data.append({
        "website": website,
        "username": username,
        "password": password
    })

    save_data(data)
    print("\nCredential saved successfully.\n")


# Update credential (password only)
def update_credential():
    data = load_data()
    if not data:
        print("\nNo credentials to update.\n")
        return

    print("\nSelect credential to update password:")
    for i, cred in enumerate(data, start=1):
        print(f"{i}. {cred['website']} ({cred['username']})")

    choice = int(input("Enter number: ")) - 1

    if 0 <= choice < len(data):
        new_password = input("Enter new password: ")
        data[choice]["password"] = new_password
        save_data(data)
        print("\nPassword updated successfully.\n")
    else:
        print("\nInvalid choice.\n")


# Main menu (loop-based)
def main_menu():
    while True:
        print("===== Vault Lite =====")
        print("1. View saved credentials")
        print("2. Add new credential")
        print("3. Update a credential")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_credentials()
        elif choice == "2":
            add_credential()
        elif choice == "3":
            update_credential()
        elif choice == "4":
            print("\nExiting Vault Lite.")
            break
        else:
            print("\nInvalid option. Try again.\n")


# Program start
main_menu()
