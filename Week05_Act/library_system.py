class Book_smg:
    def __init__(self_smg, title_smg, author_smg, year_smg):
        self_smg.title_smg = title_smg
        self_smg.author_smg = author_smg
        self_smg.year_smg = year_smg
    
    def display_book_smg(self_smg):
        print("Title:", self_smg.title_smg)
        print("Author:", self_smg.author_smg)
        print("Year:", self_smg.year_smg)
        print()

print("----- LIBRARY MANAGEMENT SYSTEM -----\n")

# Create three book objects
book1_smg = Book_smg("Python Programming", "John Smith", 2022)
book2_smg = Book_smg("Data Science Basics", "Sarah Johnson", 2021)
book3_smg = Book_smg("Web Development Guide", "Mike Davis", 2023)

# Display book information
print("Book 1:")
book1_smg.display_book_smg()

print("Book 2:")
book2_smg.display_book_smg()

print("Book 3:")
book3_smg.display_book_smg()
