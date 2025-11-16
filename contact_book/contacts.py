contact_book = {}
def add_contact(name, number):
    contact_book[name] = number
    print(f"contact ;'{name}' added sucessfully")

def search_contact(name):
    if name in contact_book:
        print(f"{name}'s number is {contact_book[name]}")
    else:    
        print(f"{name}  not found in contact book.")
def update_contact(name, number):
    if name in contact_book:
        contact_book[name] = number        
        print(f"{name}'s number updated sucessfully!")
    else: 
        print(f"{name} not found in contact book")    
def delete_contact(name):
    if name in contact_book:        
        del contact_book[name]
        print(f"{name} deleted from contact book")
    else: 
        print(f"{name} not found in contact book")    
def show_contacts():       
    if contact_book:
        print("\n--- all contacts ---")
        for name, number in contact_book.items():
            print(f"{name}: {number}")
    else:
        print("contact book is empty")

while True:        
    print("\n--- Contact Book Menu ----")
    print("1. show contacts")
    print("2. add contacts")
    print("3. Search contacts")
    print("4. Update contacts")
    print("5. Delete contact")
    print("6. Exit")
      
    choice = input("Enter your choice (1-6)")
    if choice == '1':
        show_contacts
    elif choice == '2':
        name = input("enter name: ")
        number = input("enter phone number: ")
        add_contact(name, number)
    elif choice == '3':   
        name = input("enter name to search: ")
        search_contact(name)
    elif choice == '4':
        name = input("enter name to update: ")
        number = input("enter new phone number: ")
        update_contact(name, number)
    elif choice == '5':   
         name = input("enter name to delete: ")
         delete_contact(name)
    elif choice == '6':
        print("exiting contact book, goodbye")    
        break
    else:
        print("invalid choice, please select a number from 1 to 6")


