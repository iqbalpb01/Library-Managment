from mysql.connector import errorcode
from datetime import date,datetime,timedelta
from mysql.connector import (connection)   
import os
import platform
def clrscreen():
    if platform.system()=="Windows":
        print(os.system("cls"))
def display():
    try:
        os.system("cls")  
        cnx=connection.MySQLConnection(user="lib",password="computer",host="localhost",database="Library")    
        Cursor=cnx.cursor()
        query=("SELECT * FROM BOOK")
        Cursor.execute(query)  
        for (bno,bname,Auth,price,publ,qty,dop) in Cursor:
            print("=====================================================================================") 
            print("book code:",bno)  
            print("bookname:",bname) 
            print("author of book:",Auth) 
            print("price of book:",price) 
            print("publisher:",publ)  
            print("total quantity in hand:",qty)
            print("purchased on:",dop)
            print('==================================================================================')
        Cursor.close()
        cnx.close()
        print("you have done it!!!!!")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:    
            print("something is wronmg with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err) 
    else:
        cnx.close()   
import mysql.connector  
def insertData():
    try:
        cnx=connection.MySQLConnection(user="lib",password="computer",host="localhost",database="Library") 
        Cursor=cnx.cursor() 
        bno=input("enter the book code")
        bname=input("enter book name")
        Auth=input("enter book author's name")
        price=int(input("enter the book price"))
        publ=input("enter the publisher of the book")
        qty=int(input("enter the quantity purchased"))
        print("enter data of purchase(date/month and yearseperately)")
        DD=int(input("enter date"))
        MM=int(input("enter month"))
        YY=int(input("enter year"))
        Qry=("INSERT INTO BOOK VALUES(%s,%s,%s,%s,%s,%s,%s)")
        
        data=(bno,bname,Auth,price,publ,qty,date(YY,MM,DD))
        Cursor.execute(Qry,data)
        Cursor.close()
        cnx.close()
        print("record inserted.................")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your username or password")    
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print('database does not exist')
        else:
            print(err)
    cnx.close()
def deleteBook():
    try:
        cnx=connection.MySQLConnection(user="lib",password="computer",host="localhost",database="Library") 
        Cursor=cnx.cursor() 
        bno=input("enter book code of book to be deleted from the library")
        Qry=("""DELETE FROM BOOK WHERE bno=%s""")
        del_rec=(bno,)
        Cursor.execute(Qry,del_rec)
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"Record(s0 deleted successfully................")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your username or password ")
        elif er.errno==errorcode.ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err)
    cnx.close()
def SearchBookRec():
    try:
        cnx =connection.MySQLConnection(user="lib",password="computer",host="localhost",database="Library") 
        Cursor=cnx.cursor() 
        bno=input("enter book no to be searched from the library")
        query=("SELECT * FROM BOOK where bno=%s")
        rec_srch=(bno,)
        Cursor.execute(query,rec_srch)
        Rec_count=0
        for (bno,bname,Auth,price,publ,qty,dop) in Cursor:
            Rec_count+=1
            print("======================================================================================")
            print("Book Code:",bno)
            print("book name",bname)
            print("author of book",Auth)
            print("price of the book",price)
            print("publisher",publ)
            print("total quantity in hand",qty)
            print("purchased on",dop)
            print("======================================================================================= ")
            if Rec_count%2==0:
                input("press any key to continue")
                clrscreen()
                print(Rec_count,'record (s) found')
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err)
    
        cnx.close() 
def UpdateBook():
    try:
        cnx=connection.MySQLConnection(user="lib",password="computer",host="localhost",database="Library") 
        Cursor=cnx.cursor()
        bno=input("enter book code of book to be udated from library")
        query=("SELECT* FROM BOOK where bno=%s")
        rec_srch=(bno,) 
        print("enter new data")
        bname=input("enter th bookname")         
        Auth=input("enter book author's name")
        price=int(input("enter book price"))
        publ=input("enter publisher of book")
        qty=int(input("enter the quantity purchased"))
        print("Enter Date of Purchase(Date/MOnth and Year seperately")
        DD=int(input("enter date"))
        MM=int(input("enter month"))
        YY=int(input("enter year"))
        Qry=("UPDATE BOOK SET bname=%s,Auth=%s,price=%s,publ=%s,qty=%s,dop=%s,WHERE BNO=%s")
        data=(bname,Auth,price,publ,qty,date(YY,MM,DD),bno)
        Cursor.execute(Qry,data)
        Cursor.close()
        cnx.close()     
        print(Cursor.rowcount,"Record(s) updated succssfully............")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your username or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err) 
        cnx.close()
        UpdateBook()
            


