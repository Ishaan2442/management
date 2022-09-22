import mysql.connector as connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
from turtle import clearscreen


def AddExam():
   try:
     conn= connector.connect(  host="localhost",
     user="root",
     password="01AkShAt04#",
     database="online_exams"
     )
     cursor=conn.cursor()
     Exam_ID = input("Enter Exam_ID : ")
     Subject_ID = input("Enter Subject_ID : ")
     Exam_Date=input("Enter Exam Date : ")
     Exam_Link = input("Enter Exam Link : ")
     Qry = ("INSERT INTO Exam VALUES (%s, %s, %s, %s)")
     data = (Exam_ID, Subject_ID,Exam_Date, Exam_Link)
     cursor.execute(Qry,data)
     conn.commit()
     cursor.close()
     print("Record Inserted.")
   except connector.ERROR as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
     else:
         print(err)
     conn.rollback()
   conn.close()



def DeleteExam():
 try:
  conn= connector.connect(  host="localhost",
  user="root",
  password="01AkShAt04#",
  database="online_exams"
  )
  cursor=conn.cursor()
  Exam_ID = input("Enter Exam_ID of Exam to be deleted : ")
  Qry = ("""DELETE FROM Exam WHERE Exam_ID = %s""")
  del_rec = (Exam_ID,)
  cursor.execute(Qry, del_rec)
  conn.commit()
  cursor.close()
  print(cursor.rowcount, "Record(s) Deleted Successfully.")
 except connector.ERROR as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
  else:
         print(err)
  conn.rollback()
 conn.close()



def ViewExam():
 try:
  conn= connector.connect(  host="localhost",
  user="root",
  password="01AkShAt04#",
  database="online_exams"
  )
  cursor=conn.cursor()
  Exam_ID = input("Enter Exam_ID of Exam to be searched : ")
  query = ("SELECT * FROM Exam WHERE Exam_ID = %s ")
  rec_srch = (Exam_ID,)
  cursor.execute(query, rec_srch)
  Rec_count = 0
  for(Exam_ID, User_ID,Subject_ID, Exam_Link) in cursor:
   Rec_count += 1
   print("=============================================================")
   print("Exam_ID : ", Exam_ID)
   print("User_ID : ", User_ID)
   print("Subject_ID : ", Subject_ID)
   print("Exam_Link: ", Exam_Link)
   print("=============================================================")
   if Rec_count%2 == 0:
     input("Press any key continue")
     clearscreen()
  print(Rec_count, "Record(s) found")
  conn.commit()
  cursor.close()
 except connector.ERROR as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
  else:
         print(err)
  conn.rollback()
 conn.close()