class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # CRUD for Books
    def add_book(self, title, author):
        book = {'id': len(self.books) + 1, 'title': title, 'author': author}
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return
        print("\nList of Books:")
        for book in self.books:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")

    def update_book(self, book_id, new_title, new_author):
        for book in self.books:
            if book['id'] == book_id:
                book['title'] = new_title
                book['author'] = new_author
                print(f"Book ID {book_id} updated successfully!")
                return
        print("Book not found.")

    def delete_book(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                self.books.remove(book)
                print(f"Book ID {book_id} deleted successfully!")
                return
        print("Book not found.")

    # CRUD for Members
    def add_member(self, name, membership_type):
        member = {'id': len(self.members) + 1, 'name': name, 'membership_type': membership_type}
        self.members.append(member)
        print(f"Member '{name}' added successfully!")

    def view_members(self):
        if not self.members:
            print("No members registered.")
            return
        print("\nList of Members:")
        for member in self.members:
            print(f"ID: {member['id']}, Name: {member['name']}, Membership Type: {member['membership_type']}")

    def update_member(self, member_id, new_name, new_membership_type):
        for member in self.members:
            if member['id'] == member_id:
                member['name'] = new_name
                member['membership_type'] = new_membership_type
                print(f"Member ID {member_id} updated successfully!")
                return
        print("Member not found.")

    def delete_member(self, member_id):
        for member in self.members:
            if member['id'] == member_id:
                self.members.remove(member)
                print(f"Member ID {member_id} deleted successfully!")
                return
        print("Member not found.")

# Main function to test Library Management System
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Add Member")
        print("6. View Members")
        print("7. Update Member")
        print("8. Delete Member")
        print("9. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            library.add_book(title, author)

        elif choice == '2':
            library.view_books()

        elif choice == '3':
            book_id = int(input("Enter book ID to update: "))
            new_title = input("Enter new title: ")
            new_author = input("Enter new author: ")
            library.update_book(book_id, new_title, new_author)

        elif choice == '4':
            book_id = int(input("Enter book ID to delete: "))
            library.delete_book(book_id)

        elif choice == '5':
            name = input("Enter member name: ")
            membership_type = input("Enter membership type: ")
            library.add_member(name, membership_type)

        elif choice == '6':
            library.view_members()

        elif choice == '7':
            member_id = int(input("Enter member ID to update: "))
            new_name = input("Enter new name: ")
            new_membership_type = input("Enter new membership type: ")
            library.update_member(member_id, new_name, new_membership_type)

        elif choice == '8':
            member_id = int(input("Enter member ID to delete: "))
            library.delete_member(member_id)

        elif choice == '9':
            print("Exiting the system...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
