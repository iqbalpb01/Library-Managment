import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os
def clrscreen():
    print("\n" *5)
def ShowIssuedBooks():
    try:
        os.system("cls")
        cnx=connection.MYSQLConnection(user="lib",password='computer',host="localhost",database="Library")
        Cursor=cnx.cursor()
        query=("SELECT B.bno,bname,M.mno,mname,doi,dor FROM BOOK B,ISSUE I,MEMBER M where B.bno=I.bno and I.mno=M.mno")
        Cursor.execute(query)
        for (bno,bname,mno,mname,doi,dor) in Cursor:
            print("==============================================================")
            print("book code",Bno)
            print("book name",Bname)
            print("member code",Mno)
            print("member name",Mname)
            print("date of issue",doi)
            print("date of return",dor)
            print("================================================================")
        Cursor.close()
        cnx.close()
        print("you have done it!!!!!!")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your password or username")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err)
    else:
        cnx.close()
def issueBook():
    try:
        cnx=connection.MYSQLConnection(user="lib",password='computer',host="localhost",database="Library")
        Cursor=cnx.cursor()
        bno=input("enter the book code to issue")
        mno=input("enter the member code")
        print("Enter Date of Issue (Date/Month and Year seperately)")
        DD=int(input("enter date"))
        MM=int(input("enter the month"))
        YY=int(input("enter the year"))
        Qry=("INSERT INTO ISSUE (bno,mno,doi)VALUES(%s,%s,%s)")
        data=(bno,mno,date(YY,MM,DD))   
        Cursor.execute(Qry,data)
        cnx.close()
        print("record inserted...................")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your username or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err)
    cnx.close()
def returnBook():
    try:
        cnx=connection.MYSQLConnection(user="lib",password='computer',host="localhost",database="Library")
        Cursor=cnx.cursor()
        bno=input("enter book code of book to be returned to the library")
        Mno=input("enter the member code of member wo is returning book")
        retDate=date.today()
        Qry=("""Update ISSUE set dor=%s WHERE bno=%s and mno=%s""")
        Cursor.execute(Qry,rec)
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"record(s) deleted successfully............")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your username or password")

        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err)
        cnx.close()
    

