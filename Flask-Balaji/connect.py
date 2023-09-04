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
        print("The Name is : ",  dictionary["NAME"])
        print("The E-mail is : ", dictionary["EMAIL"])
        print("The Contact is : ",  dictionary["CONTACT"])
        print("The Adress is : ",  dictionary["ADDRESS"])
        print("The Role is : ",  dictionary["ROLE"])
        print("The Branch is : ",  dictionary["BRANCH"])
        print("The Password is : ",  dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(email,password):
    sql= "select * from USER where email='{}' and password='{}'".format(email,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["NAME"])
        print("The E-mail is : ", dictionary["EMAIL"])
        print("The Contact is : ", dictionary["CONTACT"])
        print("The Address is : ", dictionary["ADDRESS"])
        print("The Role is : ", dictionary["ROLE"])
        print("The Branch is : ", dictionary["BRANCH"])
        print("The Password is : ", dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,name,email,gender,contact,date,doctor):
    sql= "INSERT into APP VALUES('{}','{}','{}','{}','{}','{}')".format(name,email,gender,contact,date,doctor)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

try:
    import ibm_db
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=32286;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=zmk67414;PWD=ChyAigq7rWQliBMi",'','')
    print(conn)
    print("connection successful...")
    insertdb(conn,"Balaji","Hari@gmail.com",'Male',789456000,'13-12-2004','RMP DoCTOR')
    #getdetails("Hari@gmail.com",'1234567')
    #showall()

except:
    print("Error connecting to the database")



