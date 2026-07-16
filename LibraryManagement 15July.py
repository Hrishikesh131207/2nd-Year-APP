class Book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author

class Patreon:
    def __init__(self,name,id):
        self.name=name
        self.id=id
 
class Library(Book):
    def __init__(self):
        self.books=[]
        self.patreon=[]
        
    def add(self):
        book=input("Enter the Book name: ")
        book_ids=input("Enter the Book ID.: ")
        self.books.append(book)
        
    def display(self):
        if len(self.books)==0:
            print("No books to display!")
        else:
            for b in self.books:
                print("The Books present are...: ")
                print(b)
    
    def browse(self):
        b1=input("Enter the book name to search: ")
        if b1 in self.books:
            print(f"The book {b1} is present...")
        else:
            print(f"The book {b1} is not present...")
            
    def register_patreon(self):
        ids=int(input("Register Patreon ID: "))
        self.patreon.append(ids)
    
    def display_patreon(self):
        if len(self.patreon)==0:
            print("No patreons registered yet...")
        else:
            for i in self.patreon:
                print(i)
            
library=Library()

while True:
    print(""".......Welcome to the Library.......
          1. Add
          2. Browse
          3. Display
          4. Register Patreon
          5. Display Patreon ID's
          6. Exit""")
    opt=int(input("Choose an option..: "))
    if opt==1:
        library.add()
        
    elif opt==2:
        library.browse()
    
    elif opt==3:
        library.display()
    
    elif opt==4:
        library.register_patreon()
    
    elif opt==5:
        library.display_patreon()
    
    elif opt==6:
        print("Exiting....")
        break
    
    else:
        print("Invalid option!\nChoose Again.....")