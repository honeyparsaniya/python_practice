#book amnagement system
books=[]

def add_book():
    book = {
        "id": input("enter book id="),
        "title": input("enter book title="),
        "author": input("enter book author name="),
        "year": input("enter book published year=")
    }
    books.append(book)
    print("book added successfully!")

def view_book():
    if not books:
        print("storage is empty")
        return
    for book in books:
        print(book)

def serch_book():
    title=input("enter book title=").lower()
    for  book in books:
        if book["title"].lower()==title:
            print("book found=",book)
            return
        print("book not found")

def delete_book():
    id=(input("enter book id="))
    for book in books:
        if book["id"]==id:
            books.remove(book)
            print("book delete sucessfully")
            return
    print("book not found")

while True:

    print("\n===book management system===")
    print("1.add book")
    print("2.view book")
    print("3.serch book")
    print("4.delete book")
    print("5.exit")
    choice=int(input("enter choice(1-5)="))

    if choice==1:
        add_book()
    elif choice==2:
        view_book()
    elif choice==3:
        serch_book()
    elif choice==4:
        delete_book()
    elif choice==5:
        break
    else:
        print("please enter valid choice!")