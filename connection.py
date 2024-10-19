import mysql.connector
import sys
lists = []
try:  # check if there is error 
    con = mysql.connector.connect(host="localhost", username="root", password="", database="joblink")  # create connection
    if con.is_connected():  # check if successfully connected
        db = con.cursor()  # hold connection response and data
        db.execute("SELECT * FROM users")  # Select All Students
        students = db.fetchall()  # get all students
        for student in students:  # loops through students
            lists.append(student[1])  # add student name to list
            lists.append(student[2])  # add student email to list
            lists.append(student[4])  # add student Phone to list
except Exception as error:  # if error caught then print it
    print(error, file=sys.stderr)  # print error CRU
