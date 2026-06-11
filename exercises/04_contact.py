"""CONTACT BOOK UTILITY.
A text-menu interface to add, list, and search for contacts using a list of dictionaries.
"""

def show_menu():
    print("\n*** Contact Book ***")
    print("1. Add Contact")
    print("2. List All Contacts")
    print("3. Search Contact")
    print("4. Exit")

def main():
    contacts = []

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")

            if not name:
                print("Error! Name field cannot be empty!")
                continue

            contact = {"name": name, "phone": phone, "email": email}
            contacts.append(contact)
            print(f"Contact for {name} added successfully!")

        elif choice == "2":
            if not contacts:
                print("No contacts found.")
            else:
                print("\n--- Contact List ---")
                for contact in contacts:
                    print(
                        f"Name: {contact['name']}, "
                        f"Phone: {contact['phone']}, "
                        f"Email: {contact['email']}"
                    )

        elif choice == "3":
            search_name = input("Enter name to search: ").strip()
            if not search_name:
                print("Error! Search term cannot be empty.")
                continue

            found = False
            print("\n*** Search Results ***")
            for contact in contacts:
                if search_name in contact["name"]:
                    print(
                        f"Name: {contact['name']}, "
                        f"Phone: {contact['phone']}, "
                        f"Email: {contact['email']}"
                    )
                    found = True

            if not found:
                print("No matching contacts found!")

        elif choice == "4":
            print("Goodbye~")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()