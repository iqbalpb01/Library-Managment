from mysql.connector import errorcode
from datetime import date,datetime, timedelta
from mysql.connector import(connection)
import os
def clrscreen():
    print("/n *5")
def display():
    try:
        os.system('cls')
        cnx=conection.MYSQLConnection(user='lib',password='computer',host='localhost',database="Library")
        Cursor=cnx.cursor()
        query=("SELECT * FROM MEMBER")
        Cursor.execute(query)
        for (mno,mname,mob,dop,addr) in Cursor:
            print("============================================================")
            print("membercode",mno)
            print("member name",mname)
            print("mobile number of member",mob)
            print("date of membership",dop)
            print("address",addr)
            print("==============================================================")
        Cursor.close()
        cnx.close()
        print("you have done it!!!!!!!!!!!!!")
    except mysql.connector.Error as err:
        if err.errno==errorcode .ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your password or username")
        elif err.errno==errorcode .ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err)
    else:
        cnx.close()
def insertMember():
    try:
        cnx=conection.MYSQLConnection(user='lib',password='computer',host='localhost',database="Library")
        Cursor=cnx.cursor()
        mno=input("enter member code")
        mname=input("enter member name")
        mob=input("enter mobile number")
        print("Enter Date of Membership (Date/Month and Year seperately)")
        DD=int(input("enter date"))
        MM=int(input("enter month"))
        YY=int(input("enter year"))
        addr=input("enter member address")
        Qry=("INSERT INTO MEMBER Values(%s,%s,%s,%s,%s)")
        data=(mno,mname,mob,date(YY,MM,DD),addr)
        Cursor.execute(Qry,data)
        Cursor.close()
        cnx.close()
        print("record inserted...............")
    except mysql.connector.Error as err:
        if err.errno==errorcode .ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your password or username")
        elif err.errno==errorcode .ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err)
        cnx.close()
def deleteMember():
    try:
        cnx=conection.MYSQLConnection(user='lib',password='computer',host='localhost',database="Library")
        Cursor=cnx.cursor()
        mno=input("enter the member code to be deleted from the library")
        Qry=("""DELETE FROM MEMBER WHERE mno=%s""")
        del_rec=(mno,)
        Cursor.execute(Qry,del_rec)
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"record(s) deleted successfully")
    except mysql.connector.Error as err:
        if err.errno==errorcode .ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your password or username")
        elif err.errno==errorcode. ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err)
        cnx.close()
def SearchMember():
    try:
        cnx=conection.MYSQLConnection(user='lib',password='computer',host='localhost',database="Library")
        Cursor=cnx.cursor()
        mname=input("enter book name to be searched from the library")
        query=("SELECT * FROM MEMBER where mname=%s")
        rec_srch=(mname,)
        Cursor.execute(query,rec_srch)
        Rec_count=0
        for (mno,mname,mob,dop,addr) in Cursor:
            print("========================================================================")
            print("member code",mno)
            print("member name",mname)
            print("mobile number of member",mob)
            print("date of membership",dop)
            print("address",addr)
            print("======================================================================")
            if Rec_count%2==0:
                input("press any key to continue")
                clrscreen()
        print(Rec_count,"record(s) found")
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno==errorcode .ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your password or username")
        elif err.errno==errorcode. ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err)
        cnx.close()



        
        