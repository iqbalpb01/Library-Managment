import MENULIB
import BOOK
import ISSUE
while True:
    BOOK.clrscreen()
    print("\t\t\t Library Management")
    print("===================================================================")
    print("1.book management")
    print("2.members management")
    print("3.issue/return book")
    print("4.exit")
    print("==================================================================")
    choice=int(input("enter choice between 1to 4-------------"))
    if choice==1:
        MENULIB.MenuBook()
    elif choice==2:
        MENULIB.MenuMember()
    elif choice==3:
        MENULIB.MenuIssueReturn()
    elif choice==4:
        break
    else:
        print('wrong choice ......enter another choice')
        x=input("enter any key to continue")