import BOOK
import MEMBER
import ISSUE
def MenuBook():
    while True:
        BOOK.clrscreen()
        print("\t\t\tBook Record Management\n")
        print("===================================================================")
        print("1.Add Book Record")
        print("2.Display Book Records")
        print("3.Search Book Record")
        print("4.Delete Book Record")
        print("5.Update Book Record")
        print("6.Return to Main Menu ")
        print("===================================================================")
        choice=int(input("Enter Choice between 1 to 5------------->:"))
        if choice==1:
            BOOK.insertData()
        elif choice==2:
            BOOK.display()
        elif choice==3:
            BOOK.SearchBookRec()
        elif choice==4:
            BOOK.deleteBook()
        elif choice==5:
            print("no such function")
        elif choice==6:
            return
        else:
            print("wrong choice.......enter your choice again")
            x=input("enter any key to continue")
def MenuMember():
    while True:
        BOOK.clrscreen() 
        print('\t\t\tMember Record Management\n')
        print("============================================================") 
        print("1.add member record")
        print("2.display member records")
        print("3.search member record") 
        print("4.delete member record") 
        print("5.update book record") 
        print("6.return to mainmenu") 
        print("=============================================================")
        choice=int(input("enter choice between 1 to 5-------->")) 
        if choice==1:
            MEMBER.insertMember()
        elif choice==2:
            MEMBER.display()
        elif choice==3:
            MEMBER.SearchMember()
        elif choice==4:
            MEMBER.deleteMember()
        elif choice==5:
            print("no such function")
        elif choice==6:
            return
        else:
            print("wrong choice.........enter your choice again")
            x=input("enter any key to continue")
#---------------------------------------------------------------------
def MenuIssueReturn():
    while True:
        BOOK.clrscreen()
        print("\t\t\t Member record management\n")
        print("============================================================") 
        print("1.issuebook")
        print("2.display issued book records")
        print("3.return issued book")
        print("4.return to main menu")
        print("============================================================") 
        choice=int(input("Enter Choice between 1 to 4------------->:"))
        if choice==1:
            ISSUE.issueBook()
        elif choice==2:
            ISSUE.ShowIssuedBooks() 
        elif choice==3:
            ISSUE.returnBook()  
        elif choice==4:
            return
        else:
            print("wrong choice.........enter your choice again")
            x=input("enter any key to continue")
            
            

        

