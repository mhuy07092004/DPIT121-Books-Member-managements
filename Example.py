
#  Define Library Items class:
class LibraryItems:
    def __init__(self, title):
        self.title = title

# Book Class (ID,Title,Author)
class Book(LibraryItems):
    def __init__(self, bookID, title, author):
        super().__init__(title)
        self.bookID = bookID
        self.author = author
        self.available = True

#  Member class(MemberID, Member Name)
class Member:
    def __init__(self, memberID, name):
        self.memberID = memberID
        self.name = name
        self.borrowed_books = []

# Main Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.next_book_id = 1

    # 1. Show All Books Function
    def show_books(self):
        print("\nBook Collection:")
        for book in self.books:
            status = 'Available' if book.available else 'Borrowed'
            print(f"ID: {book.bookID}, Title: {book.title}, Author: {book.author}, Status: {status}")
        if not self.books:
            print("No books in the library yet. :( ")

    # 2. Add New Book Function
    def add_book(self, title, author):
        new_book = Book(self.next_book_id, title, author)
        self.books.append(new_book)
        self.next_book_id += 1
        print(f"Book '{title}' added successfully! :)")

    #3.  Search For A Book Function
    def search_book(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books: # Check if Book exist or not
            print("\nSearch Results:")
            for book in found_books: # Check The availability if founded
                status = 'Available' if book.available else 'Borrowed'
                print(f"ID: {book.bookID}, Title: {book.title}, Author: {book.author}, Status: {status}")
        else:
            print("No book found with that title :(")

    # 4. Show All Members Function
    def show_members(self):
        print("\nLibrary Members:")
        for member in self.members:
            borrowed_titles = ', '.join(book.title for book in member.borrowed_books) or 'None'
            print(f"ID: {member.memberID}, Name: {member.name}, Borrowed Books: {borrowed_titles}")
        if not self.members:
            print("No members in the library yet. :(")

    #5. Add Member Function
    def add_member(self, name):
        new_member = Member(len(self.members) + 1, name)
        self.members.append(new_member)
        print(f"New member '{name}' added successfully :)")

    #6. Borrow Book Function
    def borrow_book(self, memberID, bookID):
        member = next((m for m in self.members if m.memberID == memberID), None)
        book = next((b for b in self.books if b.bookID == bookID), None)

        if not member:
            print("Member not found :(")
        elif not book:
            print("Book not found :(")
        elif not book.available:
            print("Book is already borrowed :(")
        else:
            member.borrowed_books.append(book)
            book.available = False
            print(f"Book '{book.title}' borrowed by '{member.name}'.")

    # 7. return Book Function
    def return_book(self, memberID, bookID):
        member = next((m for m in self.members if m.memberID == memberID), None)
        if member:
            book = next((b for b in member.borrowed_books if b.bookID == bookID), None)
        else:
            book = None
        if not member:
            print("Member not found :( ")
        elif not book:
            print("Book not found in borrowed books :( ")
        else:
            member.borrowed_books.remove(book)
            book.available = True
            print(f"Book '{book.title}' returned by '{member.name}'.")



# Main Menu
def menu():
    library = Library()

    # Adding sample Books
    library.add_book("Alice's Adventures in Wonderland", "Lewis Carroll")
    library.add_book("Pride and Prejudice", "Jane Austen")
    library.add_book("Sherlock Holmes", "Sir Arthur Conan Doyle")
    library.add_book("Harry Potter", "J. K. Rowling")
    library.add_book("Big Data Analytics", "DJ Patil")
    # Adding Sample Members
    library.add_member("Minh Huy Loi")
    library.add_member("Hector Elias")
    library.add_member("Keshav Jha")
    library.add_member("Adel Omar")
    library.add_member("John James")

    # Menu Loop for user interaction
    while True:
        print("\n----Welcome To Minh's Library----")
        print("1. Show book collection")
        print("2. Add book")
        print("3. Search book by title")
        print("4. Show list of current members")
        print("5. Add new member")
        print("6. Borrow book")
        print("7. Return book")
        print("8. Exit")

        # Choice Input
        choice = input("Enter your choice -> ")

        # Choices Value Compare
        if choice == "1":
            library.show_books()
        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == "3":
            title = input("Enter book title to search: ")
            library.search_book(title)
        elif choice == "4":
            library.show_members()
        elif choice == "5":
            name = input("Enter member name: ")
            library.add_member(name)
        elif choice == "6":
            memberID = int(input("Enter member ID: "))
            bookID = int(input("Enter book ID: "))
            library.borrow_book(memberID, bookID)
        elif choice == "7":
            memberID = int(input("Enter member ID: "))
            bookID = int(input("Enter book ID: "))
            library.return_book(memberID, bookID)
        elif choice == "8":
            print("Exiting the program. Goodbye! :D")
            break
        else:
            print("Invalid choice. Please try again. :( ")

    menu()