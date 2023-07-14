class library:
    no_of_books = 0
    book_rack = []

    def __init__(self):
        self.book_name = input("Enter the book's name = ")
        

    def books_add(self):
        library.book_rack.append(self.book_name)
        print(f"Books added in library are = {library.book_rack}")
        library.no_of_books = library.no_of_books + 1

    def sum_book(self):

        if library.no_of_books == len(library.book_rack):
            print("no of books entered is correct")
        else:
            raise ValueError 
        

student = library()
student.books_add()


while True:

    user_add = input("Do you want enter more books (Y/N) = ")

    if user_add == "Y" or user_add == "y":
      student.__init__()
      student.books_add()

      user_sum = input("Do you want to check the number of books (Y/N) = ")

      if user_sum == "Y" or user_sum == "y":         
         student.sum_book()
    
    else:
        print("Thank you!")
        break
     
     









        