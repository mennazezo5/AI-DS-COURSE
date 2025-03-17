from book import BookFormat,Book,BookItem,BookStatus,Rack,ReservationStatus,BookReservation,BookLending
from library import Library,LibraryCard,BarcodeReader
from user import AccountStatus,Address,Member,Person,Librarian
from catalog import Catalog
from fine import Fine,FineTransaction,CashTransaction,CheckTransaction,CreditCardTransaction
from notification import Notification,PostalNotification,EmailNotification
from datetime import date

library = Library("Central Library", "123 Library St, City, Country")
catalog= Catalog("2023-06-01",3,{"pyton","java","c#"},{"Publisher1","Publisher2","Publisher3"},{"cs"},{"2020-01-01","2021-01-01","2022-01-01"})

address = Address("123 Main St", "City", "State", "12345", "Country")
person = Person("John", address, "john.doe@example.com", "123-456-7890")
person2 = Person("mo ", address, "mo.doe@example.com", "123-666-7890")
library_card = LibraryCard("LC123456", "987654321", date.today(), True)
member = Member(1, "password123", AccountStatus.Active, person)
libraian= Librarian(2, "password223", AccountStatus.Active, person2)


book = Book("123456789", "Python ", "cs", "Publisher1", "English", 300)
book_item = BookItem("B123", False, date.today(), date.today(), 29.99, BookFormat.Hardcover, BookStatus.Available, date.today(), "2020-01-01")

# Librarian.add_book_item(book)

if book_item.checkout():True


def main():
    print("Welcome to the Library Management System!")
    name = input("Please enter your name: ")
    
    while True:
        print("\nPlease choose your role:")
        print("1. Member")
        print("2. Librarian")
        print("3. Exit")
        
        role_choice = input("Enter the number of your role: ")
        
        if role_choice == "1":
            print(f"\nWelcome {name} (Member)!")
            while True:
                print("\n1. Borrow a Book")
                print("2. Return a Book")
                print("3. Search Book")
                print("4. Reserve a Book")
                print("5. Logout")
                
                action_choice = input("Choose an action: ")
                
                if action_choice == "1":
                    print("You chose: Borrow a Book")
                    BookLending("2025-01-07","2025-03-04","2025-07-04")
                elif action_choice == "2":
                    print("You chose: Return a Book")
                    BookReservation(book_item,member)
                elif action_choice == "3":
                    print(" Search Book what?")
                    print("1. author")
                    print("2. title")
                    print("3. subject")
                    print("4. publication date")
                    a=input(" ")
                    if a=="1":
                        a=input("Enter author: ")
                        catalog.search_by_author(a)
                        if True:
                            print("found")
                        else:
                            print("not found")
                    elif a=="2":
                        a=input("Enter title: ")
                        catalog.search_by_title(a)
                        if True:
                            print("found")
                        else:
                            print("not found")   
                    elif a=="3":
                        a=input("Enter subject: ")
                        catalog.search_by_subject(a)
                        if True:
                            print("found")
                        else:
                            print("not found")
                    elif a=="4":
                        a=input("Enter publication date (YYYY-MM-DD): ")  
                        catalog.search_by_publication_date(a)
                        if True:
                            print("found")
                        else:
                            print("not found")                           
                elif action_choice == "4":
                    print("You chose: Reserve a Book")
                    BookReservation(book_item,member)
                elif action_choice == "5":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif role_choice == "2":
            print(f"\nWelcome {name} (Librarian)!")
            while True:
                print("\n1. Add a Book")
                print("2. Remove a Book")
                print("3. Search Book")
                print("4. Manage Members")
                print("5. Logout")
                
                action_choice = input("Choose an action: ")
                
                if action_choice == "1":
                    print("You chose: Add a Book")
                    libraian.add_book_item()
                elif action_choice == "2":
                    print("You chose: Remove a Book")
                elif action_choice == "3":    
                    print(" Search Book what?")
                    print("1. author")
                    print("2. title")
                    print("3. subject")
                    print("4. publication date")
                    a=input(" ")
                    if a=="1":
                        a=input("Enter author: ")
                        catalog.search_by_author(a)
                        if True:
                            print("found")
                        else:
                            print("not found")
                    elif a=="2":
                        a=input("Enter title: ")
                        catalog.search_by_title(a)
                        if True:
                            print("found")
                        else:
                            print("not found")   
                    elif a=="3":
                        a=input("Enter subject: ")
                        catalog.search_by_subject(a)
                        if True:
                            print("found")
                        else:
                            print("not found")
                    elif a=="4":
                        a=input("Enter publication date (YYYY-MM-DD): ")
                        catalog.search_by_publication_date(a)
                        if True:
                            print("found")
                        else:
                            print("not found")                              
                elif action_choice == "4":
                    print("You chose: Manage Members")
                    print("\n1. block_member")
                    print("2. unblock_member")
                    w=input("")
                    if w=="1":
                        libraian.block_member()
                    else:
                        libraian.unblock_member()   
                elif action_choice == "5":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        
    
        elif role_choice == "3":
            print("Thank you for using the Library Management System. Goodbye!")
            break  
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()