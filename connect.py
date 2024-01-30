# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:58:50 2023

@author: Shivani_SB
"""
def showall():
    sql= "SELECT * from USER"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The DEPARTMENT is : ",  dictionary["NAME"])
        print("The  DOCTOR  is : ", dictionary["EMAIL"])
        print("The DATE is : ",  dictionary["CONTACT"])
        print("The TIME is : ",  dictionary["ADDRESS"])
        print("The FULLNAME is : ",  dictionary["ROLE"])
        print("The PHONE NUMBER is : ",  dictionary["BRANCH"])
        print("The EMAIL is : ",  dictionary["PASSWORD"])
        print("The WHATSAP NUMBER is: ", dictionary["WHATSAP NUMBER"])
        print("The PROBLEM is: ", dictionary["problem"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(email,password):
    sql= "select * from USER where email='{}' and password='{}'".format(email,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The  is : ",  dictionary["NAME"])
        print("The E-mail is : ", dictionary["EMAIL"])
        print("The Contact is : ", dictionary["CONTACT"])
        print("The Address is : ", dictionary["ADDRESS"])
        print("The Role is : ", dictionary["ROLE"])
        print("The Branch is : ", dictionary["BRANCH"])
        print("The Password is : ", dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,name,email,contact,address,role,branch,password):
    sql= "INSERT into USER VALUES('{}','{}','{}','{}','{}','{}','{}')".format(name,email,contact,address,role,branch,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

try:
    import ibm_db
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=rqy41363;PWD=9ozyrz3LXNz0Fwhv",'','')
    print(conn)
    print("connection successful...")
    #insertdb(conn,"Hari","Hari@gmail.com",'1234567890','Adarsh nagar','Faculty','Civil','1234567')
    getdetails("Hari@gmail.com",'1234567')
    #showall()

except:
    print("Error connecting to the database")



