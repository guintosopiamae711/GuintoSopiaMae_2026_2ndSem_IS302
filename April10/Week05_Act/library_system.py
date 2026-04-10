class Book_nbs:
    def __init__(self_nbs, title_nbs, author_nbs, year_nbs):
        self_nbs.title_nbs = title_nbs
        self_nbs.author_nbs = author_nbs
        self_nbs.year_nbs = year_nbs
    
    def display_book_nbs(self_nbs):
        print("Title:", self_nbs.title_nbs)
        print("Author:", self_nbs.author_nbs)
        print("Year:", self_nbs.year_nbs)
        print()

print("----- LIBRARY MANAGEMENT SYSTEM -----\n")

# Create three book objects
book1_nbs = Book_nbs("Python Programming", "John Smith", 2022)
book2_nbs = Book_nbs("Data Science Basics", "Sarah Johnson", 2021)
book3_nbs = Book_nbs("Web Development Guide", "Mike Davis", 2023)

# Display book information
print("Book 1:")
book1_nbs.display_book_nbs()

print("Book 2:")
book2_nbs.display_book_nbs()

print("Book 3:")
book3_nbs.display_book_nbs()
