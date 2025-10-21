contact_book = {}

def add_contact(name, number):
    contact_book[name] = number
    print(f"Contact '{name}' added successfully!")

def search_contact(name):
    if name in contact_book:
        print(f"{name}'s number is {contact_book[name]}")
    else:    
        print(f"{name} not found in contact book.")

def update_contact(name, number):
    if name in contact_book:
        contact_book[name] = number        
        print(f"{name}'s number updated successfully!")
    else: 
        print(f"{name} not found in contact book.")    

def delete_contact(name):
    if name in contact_book:        
        del contact_book[name]
        print(f"{name} deleted from contact book.")
    else: 
        print(f"{name} not found in contact book.")    

def show_contacts():       
    if contact_book:
        print("\n--- All Contacts ---")
        for name, number in contact_book.items():
            print(f"{name}: {number}")
    else:
        print("Contact book is empty.")

# ---------------- Main Loop ----------------
while True:        
    print("\n--- Contact Book Menu ---")
    print("1. Show Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
      
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        show_contacts()  # ✅ Function call fixed
    elif choice == '2':
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        add_contact(name, number)
    elif choice == '3':   
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == '4':
        name = input("Enter name to update: ")
        number = input("Enter new phone number: ")
        update_contact(name, number)
    elif choice == '5':   
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == '6':
        print("Exiting contact book. Goodbye!")    
        break
    else:
        print("Invalid choice! Please select a number from 1 to 6.")
