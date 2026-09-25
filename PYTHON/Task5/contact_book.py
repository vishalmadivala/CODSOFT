"""
Contact Book Application
CodSoft Python Programming Internship - Task 5

A command-line Contact Book that lets users add, view, search, update,
and delete contacts. Each contact stores a name, phone number, email,
and address. Data is stored persistently in a local JSON file
(contacts.json).
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.json")


def load_contacts():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_contacts(contacts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2)


def print_header(title):
    print("\n" + "=" * 42)
    print(title.center(42))
    print("=" * 42)


def view_contacts(contacts):
    print_header("CONTACT LIST")
    if not contacts:
        print("No contacts saved yet.")
        return
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']}  —  {c['phone']}")
    print("=" * 42)


def view_contact_details(c):
    print("-" * 42)
    print(f"Name:    {c['name']}")
    print(f"Phone:   {c['phone']}")
    print(f"Email:   {c['email']}")
    print(f"Address: {c['address']}")
    print("-" * 42)


def add_contact(contacts):
    print("\nEnter new contact details:")
    name = input("Name: ").strip()
    if not name:
        print("Name is required. Contact not added.")
        return
    phone = input("Phone number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
    })
    save_contacts(contacts)
    print(f'Contact "{name}" added.')


def search_contacts(contacts):
    query = input("Search by name or phone number: ").strip().lower()
    results = [
        c for c in contacts
        if query in c["name"].lower() or query in c["phone"].lower()
    ]
    print_header(f"SEARCH RESULTS ({len(results)} found)")
    if not results:
        print("No matching contacts found.")
    for c in results:
        view_contact_details(c)


def _select_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return None
    try:
        choice = int(input("Enter contact number: "))
        if 1 <= choice <= len(contacts):
            return choice - 1
    except ValueError:
        pass
    print("Invalid contact number.")
    return None


def update_contact(contacts):
    idx = _select_contact(contacts)
    if idx is None:
        return
    c = contacts[idx]
    view_contact_details(c)
    print("Leave a field blank to keep its current value.")

    name = input(f"Name [{c['name']}]: ").strip()
    phone = input(f"Phone [{c['phone']}]: ").strip()
    email = input(f"Email [{c['email']}]: ").strip()
    address = input(f"Address [{c['address']}]: ").strip()

    if name:
        c["name"] = name
    if phone:
        c["phone"] = phone
    if email:
        c["email"] = email
    if address:
        c["address"] = address

    save_contacts(contacts)
    print("Contact updated.")


def delete_contact(contacts):
    idx = _select_contact(contacts)
    if idx is None:
        return
    removed = contacts.pop(idx)
    save_contacts(contacts)
    print(f'Deleted contact "{removed["name"]}".')


def main_menu():
    print("""
1. View all contacts
2. Add contact
3. Search contact
4. Update contact
5. Delete contact
6. Exit
""")


def main():
    contacts = load_contacts()
    print_header("CONTACT BOOK")
    print("Manage your contacts easily. Data is saved automatically.")

    while True:
        main_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye! Your contacts have been saved.")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
