# import search
import re
# import Pretty Table for creating tables
from prettytable import PrettyTable
# import connection
from connection import db, con, lists
# import Sys for standout output error
import sys
# import Get Password for hiding password input
import getpass
import os
# import loading function
from load import load, home_load
# from logo
from logo import logo
# import send email page
from send_email import send_mail
# import random
import random


def clear_screen():
    # Check the operating system.
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')


class joblink:
    def __init__(self, choice):
        if choice == "1":
            load()
            clear_screen()
            self.sign_up(self)
        elif choice == "2":
            load()
            clear_screen()
            self.sign_in(self)
        elif choice == "3":
            load()
            clear_screen()
            logo()
            print("\033[31mThanks for using our app")
            exit()
        else:
            load()
            clear_screen()
            print("\033[31mInvalid input")
            main()

    @staticmethod
    def sign_up(self):  # allow sign up for users
        print("\033[1m\033[32m --- User Registration ---\n \033[0m")
        print("\033[1m\033[35m Please enter your details: \033[0m")
        name = input("\033[1m\033[36m Your User Name: \033[0m")
        email = input("\033[1m\033[36m Your User Email: \033[0m")
        password = getpass.getpass("\033[1m\033[36m Your User Password: \033[0m")
        phone = input("\033[1m\033[36m Your User Phone Number: \033[0m")
        country = input("\033[1m\033[36m Your User Country: \033[0m")
        school = input("\033[1m\033[36m Your User School, College, University: \033[0m")
        education_level = input("\033[1m\033[36m Your User Education level(Degree): \033[0m")
        if not re.search(r"@.*\..*", email):
            load()
            clear_screen()
            print("\033[1m\033[31m\n************* Enter Valid Email ****************\033[0m")
            self.sign_up(self)
        elif not phone.isnumeric():
            load()
            clear_screen()
            print("\033[1m\033[31m\n************* Phone Number Must Be Numbers ****************\033[0m")
            self.sign_up(self)
        elif name in lists:
            load()
            clear_screen()
            print("\033[1m\033[31m\n************* This Username Is Taken ****************\033[0m")
            self.sign_up(self)
        elif email in lists:
            load()
            clear_screen()
            print("\033[1m\033[31m\n************* This Email Is Taken ****************\033[0m")
            self.sign_up(self)
        elif phone in lists:
            load()
            clear_screen()
            print("\033[1m\033[31m\n************* This Phone Number Is Taken ****************\033[0m")
            self.sign_up(self)
        elif (name == "" or email == "" or password == "" or phone == "" or country == "" or school == "" or
              education_level == ""):
            load()
            clear_screen()
            print("\033[1m\033[31m\n************* You Cant Submit With Empty Fields ****************\033[0m")
            self.sign_up(self)
        else:
            code = random.randint(120000, 600000)
            # otp Code For Email
            msg = (f"Hello {name},\n\nYour verification code is: {code} "
                   f"If you did not request this code, please ignore this message."
                   " Welcome aboard!\n\nBest regards,\n Job Link")
            if send_mail(to=email, sub="Account Creation Successful", msg=msg):
                if code == int(input("\n\033[1m\033[31mEnter Verification Code Sent to your email\033[0m")):
                    # register user to database
                    # values
                    # Insertion
                    data = (name, email, password, phone, country, education_level, school)
                    try:  # check if there is an error while inserting
                        sql = (
                            "INSERT INTO `users`(`uname`, `email`, `password`, `phone`, `country`, `education_level`,"
                            " `school`) VALUES (%s,%s,%s,%s,%s,%s,%s)")
                        db.execute(sql, data)
                        con.commit()
                        if db.rowcount > 0:  # check affected rows to see if inserted
                            load()
                            clear_screen()
                            msg = (f"Hello {name},\n\nYour account has been successfully created."
                                   " Welcome aboard!\n\nBest regards,\n Job Link")
                            if send_mail(to=email, sub="Account Creation Successful", msg=msg):
                                print("\033[1m\033[32m Successfully Registered Login Now \033[0m")
                                self.sign_in(self)  # call the login page if user is inserted well
                        else:  # data not inserted in Database
                            print("**** Failed To Register Your Data Try Again ****", file=sys.stderr)
                            self.sign_up(self)  # recall sign up function if error happened

                    except Exception as e:
                        print(e, file=sys.stderr)
                        self.sign_up(self)
                else:
                    print("Code Doesnt Match")
                    self.sign_up(self)

    @staticmethod
    def sign_in(self):
        print("\n\033[1m\033[32m ---Please Log In---\033[0m\n")
        print("\033[1m\033[35m Please enter your Credential: \033[0m")
        email = input("\033[1m\033[36m Enter Email: \033[0m")
        password = getpass.getpass("\033[1m\033[36m Enter Password: \033[0m")
        if not re.search(r"@.*\..*", email):
            print("\033[1m\033[31m\n******* Enter Valid Email *********\033[0m")
            self.sign_in(self)
        else:
            # data well validated then check if user is registered
            data = (email, password)
            try:  # check if there is an error in the codes
                sql = "SELECT * FROM users WHERE email=%s AND password=%s"
                db.execute(sql, data)
                res = db.fetchall()
                if len(res) > 0:  # check there is any response => home
                    load()  # call The loader Function
                    clear_screen()  # Clear the Screen22
                    print("\n\033[1m\033[32m ----** Successfully Logged In **---- \033[0m\n")
                    self.uname = res[0][1]  # keep the name of logged-in user
                    self.user_id = res[0][0]  # keep the USEr id of logged-in user
                    self.school = res[0][7]  # keep the user school
                    self.email = res[0][2]  # keep the user Email
                    self.home(self)  # call the home function
                else:  # If no Record Matched print msg and recall function
                    load()
                    clear_screen()
                    print("\033[1m\033[31m\n *** Incorrect Username and Password (Not Found Try Again)***\033[0m")
                    self.sign_in(self)
            except Exception as e:
                load()
                print(e, file=sys.stderr)
                self.sign_in(self)

    @staticmethod
    def p_setting(self):
        c_name = input("\033[1m\033[34mEnter Company Name: ")
        c_industry = input("Enter Field: ")
        j_title = input("Enter Job Title: ")
        j_desc = input("Enter Job Description: ")
        j_req = input("Enter Job Requirements: ")
        contract = input("Do You Provide a Contract (Yes/No): \033[0m")
        data = (self.uname, c_name, c_industry, j_title, j_desc, j_req, contract)
        try:  # check if there is an error while inserting
            sql = ("INSERT INTO `org`(`posted_by`, `cp_name`, `cp_industry`, `job_title`"
                   ", `job_description`, `job_doc`, `contract`) VALUES (%s,%s,%s,%s,%s,%s,%s)")
            db.execute(sql, data)
            con.commit()
            if db.rowcount > 0:  # check affected rows to see if inserted
                print("\033[1m\033[32m Successfully Posted Your Company \033[0m")
                dataw = self.uname
                sql2 = (f"SELECT `cp_id`, `cp_name`, `cp_industry`, `job_title`, `job_description`,"
                        f" `job_doc`, `contract`, DATE_FORMAT(date_added, '%d,%M,%Y') FROM `org` "
                        f"WHERE posted_by ='{dataw}'")  # for users jobs
                load()
                clear_screen()
                self.view_jobs(self, sql2)  # call the view jobs page if job is inserted well
            else:  # data not inserted in Database
                print("**** Failed To Register Your Job Try Again ****", file=sys.stderr)
                load()
                clear_screen()
                self.p_setting(self)  # recall sign up function if error happened

        except Exception as e:
            print(e, file=sys.stderr)
            self.p_setting(self)

    @staticmethod
    def home(self):  # contain home page for program
        print(f"\n\033[1m\033[32m ****** Welcome Back, [{self.uname}]! ******\033[0m\n")
        print("\033[1m\033[31m [1] \033[34mView Jobs")
        print("\033[1m\033[31m [2] \033[34mConnect with Alumni")
        print("\033[1m\033[31m [3] \033[34mProfile Settings")
        print("\033[1m\033[31m [4] \033[34mApply For Job")
        print("\033[1m\033[31m [5] \033[34mLog out")
        choices = input("\n\033[1m\033[34mEnter Choice: \033[0m ")  # enter user choice
        # check if user choice is in range
        if choices == "1":
            load()
            clear_screen()
            self.min_view(self)
        elif choices == "2":
            load()
            clear_screen()
            self.view_people(self)
        elif choices == "3":
            print("\n\n\033[1m\033[31mManage Your Profile")
            print("\033[1m\033[31m [1] \033[34mPost Company")
            print("\033[1m\033[31m [2] \033[34mUpdate Company")
            print("\033[1m\033[31m [3] \033[34mDelete Company")
            print("\033[1m\033[31m [4] \033[34mGo Back To Home")
            choi = input("\n\033[1m\033[34mEnter Your choice: \033[0m")
            if choi == "1":
                load()
                clear_screen()
                self.p_setting(self)
            elif choi == "2":
                load()
                clear_screen()
                self.update_job(self)
            elif choi == "3":
                load()
                clear_screen()
                self.delete_job(self)
            elif choi == "4":
                load()
                clear_screen()
                self.home(self)
            else:
                load()
                clear_screen()
                print("\033[1m\033[31m\n---------------- Invalid Choice-------------------\033[0m")
                self.home()
        elif choices == "4":
            self.apply_jobs(self)
            load()
        elif choices == "5":
            load()
            clear_screen()
            print("\n\n\033[1m\033[31m\n######## *** You Have Successfully logged out *** ######## \033[0m\n")
            main()
        else:
            load()
            clear_screen()
            print("Invalid Choice try Again", file=sys.stderr)
            self.home(self)

    @staticmethod
    def apply_jobs(self):  # apply  for jobs
        data = self.uname
        print("\033[1m\033[31mChoose The Job You Want To Apply \033[0m")
        sql = (f"SELECT `cp_id`, `cp_name`, `cp_industry`, `job_title`, `job_description`,"
               f" `job_doc`, `contract`, DATE_FORMAT(date_added, '%d,%M,%Y') FROM `org` "
               f"WHERE posted_by !='{data}'")  # for users jobs
        self.view_jobs_no_recall(self, sql)
        code = input("\033[1m\033[32mEnter Company Code Of Job You Want To Apply: \033[0m")
        try:
            # SQL to check if id exists in records in table
            check = "SELECT users.email, org.cp_name FROM org, users WHERE org.cp_id=%s"
            db.execute(check, (code,))  # send request
            dt = db.fetchall()  # get all data2
            if len(dt) > 0:
                # insert application
                email = dt[0][0]
                cp_name = dt[0][1]
                data2 = (self.email, code)
                ins = (f"INSERT INTO `applications`( `user_email`, `job_id`) "
                       f"VALUES (%s,%s)")
                db.execute(ins, data2)
                con.commit()
                if db.rowcount > 0:  # when application registered send email
                    sub1 = f"Application Confirmation - {cp_name}"
                    msg1 = (f"Dear {self.uname},\n"
                            f"We are writing to inform you that your application to {cp_name} has"
                            f" been successfully submitted.\n"
                            f"We kindly request you to await further instructions from {cp_name} regarding"
                            f" the submission of necessary documents.\n\n"
                            f"Thank you for choosing Job Link as your platform for opportunities.\n\n"
                            f"Best regards,\nJob Link Team\n")

                    sub2 = f"Regarding Application for Your Posted Job"
                    msg2 = (f"Dear {cp_name},\n"
                            f"We wish to inform you that one of our esteemed users, {self.uname} with "
                            f"Email: ({self.email}), "
                            f"has recently submitted an application for one of the job you posted on our platform.\n"
                            f"We encourage you to connect with them for any additional requirements or "
                            f"further information.\n\n"
                            f"Thank you for considering Job Link as your platform of choice.\n\n"
                            f"Best regards,\nJob Link Team\n")

                    # send email to user
                    if send_mail(to=self.email, sub=sub1, msg=msg1):
                        # send email to 2
                        # 2job owner
                        if send_mail(to=email, sub=sub2, msg=msg2):
                            load()
                            clear_screen()
                            print("\033[1m\033[32mSuccessfully sent your Application check your emails and"
                                  " keep track\033[0m")
                            self.home(self)
                        else:
                            print("\033[1m\033[31mFailed To Send Notification2.\033[0m")
                    else:
                        print("\033[1m\033[31mFailed To Send Notification.\033[0m")

                else:
                    print("\033[1m\033[31mFailed To Send Your Application.\033[0m")

            else:
                print("\033[1m\033[31mFailed To Get Your Job Check Company Code: \033[0m")
                self.apply_jobs(self)
        except Exception as e:
            load()
            clear_screen()
            print(e, file=sys.stderr)
            self.apply_jobs(self)

    @staticmethod
    def update_job(self):
        data = self.uname
        print("\033[1m\033[31mChoose The Job You Want To Apply for\033[0m")
        sql = (f"SELECT `cp_id`, `cp_name`, `cp_industry`, `job_title`, `job_description`,"
               f" `job_doc`, `contract`, DATE_FORMAT(date_added, '%d,%M,%Y') FROM `org` "
               f"WHERE posted_by ='{data}'")  # for users jobs
        self.view_jobs_no_recall(self, sql)
        code = input("\n\033[1m\033[34mEnter Company Code To Update: \033[0m ")  # enter user choice
        c_name = input("\033[1m\033[34mEnter Company Name: ")
        c_industry = input("Enter Field: ")
        j_title = input("Enter Job Title: ")
        j_desc = input("Enter Job Description: ")
        j_req = input("Enter Job Requirements: ")
        contract = input("Do You Provide a Contract (Yes/No): \033[0m")
        data2 = (c_name, c_industry, j_title, j_desc, j_req, contract, self.uname, code)
        try:  # check if there is an error while inserting
            sql_update = ("UPDATE `org` SET `cp_name`=%s,`cp_industry`=%s,`job_title`=%s,"
                          "`job_description`=%s,`job_doc`=%s,`contract`=%s WHERE posted_by=%s and cp_id=%s")
            db.execute(sql_update, data2)
            con.commit()
            if db.rowcount > 0:  # check affected rows to see if inserted
                load()
                clear_screen()
                print("\033[1m\033[32m Successfully Updated Your Company \033[0m")
                self.view_jobs(self, sql)  # call the login page if user is inserted well
            else:  # data not inserted in Database
                load()
                clear_screen()
                print("**** Failed To Update Your Job Try Again ****", file=sys.stderr)
                self.view_jobs(self, sql)  # recall sign up function if error happened
        except Exception as e:
            load()
            clear_screen()
            print(e, file=sys.stderr)
            self.update_job(self)

    @staticmethod
    def delete_job(self):
        data = self.uname
        print("\033[1m\033[31mChoose The Job You Want To Delete\033[0m")
        sql = (f"SELECT `cp_id`, `cp_name`, `cp_industry`, `job_title`, `job_description`,"
               f" `job_doc`, `contract`, DATE_FORMAT(date_added, '%d,%M,%Y') FROM `org` "
               f"WHERE posted_by ='{data}'")  # for users jobs
        self.view_jobs_no_recall(self, sql)
        code = input("\n\033[1m\033[34mEnter Company Code To Delete: \033[0m ")  # enter user choice
        data2 = (self.uname, code)
        try:  # check if there is an error while inserting
            sql_update = "DELETE FROM `org` WHERE posted_by=%s and cp_id=%s"
            db.execute(sql_update, data2)
            con.commit()
            if db.rowcount > 0:  # check affected rows to see if inserted
                load()
                clear_screen()
                print("\033[1m\033[32m Successfully Delete Your Company Job \033[0m")
                self.view_jobs(self, sql)  # call the View page if user is inserted well
            else:  # data not Deleted in Database
                load()
                clear_screen()
                print("**** Failed To Delete Your Job Try Again ****", file=sys.stderr)
                self.view_jobs(self, sql)  # recall function if error happened
        except Exception as e:
            load()
            clear_screen()
            print(e, file=sys.stderr)
            self.update_job(self)

    @staticmethod
    def view_people(self):
        print("\n\n\033[1m\033[32m---------------*** List of Your Alumni ***-----------------\033[0m\n\n")
        try:
            sql = (f"SELECT  `uname`, `email`, `phone`, `country`, `education_level`,"
                   f" `school` FROM users  WHERE school = '{self.school}'")
            db.execute(sql)
            students = db.fetchall()
            if len(students) > 0:
                header = ["Alumin Name", "Alumin Email", "Alumin Phone", "Alumni Country", "Alumin School",
                          "Alumin Degree"]
                table = PrettyTable(header)
                for student in students:
                    table.add_row(student)

                print("\033[1m\033[32m")
                print(table, "\033[0m")
                self.home(self)
            else:
                print("You Dont Have Any Alumin ", file=sys.stderr)

        except Exception as e:
            print(e, file=sys.stderr)

    @staticmethod  # provides a menu for the user to choose how they want to view job postings
    def min_view(self):
        print("\n\033[1m\033[31mChoice What You Want To See\033[0m")
        print(f"\033[1m\033[31m [1] \033[34mView Jobs Posted By [\033[31m{self.uname}\033[0m]\033[34m only\033[0m")
        print(f"\033[1m\033[31m [2] \033[34mView Jobs Posted By \033[31mOthers \033[0m")
        print(f"\033[1m\033[31m [3] \033[34mBack To Home  \033[0m")
        choice = input("\n\033[1m\033[34mEnter Choice: \033[0m ")  # enter user choice
        sql = ""
        data = self.uname
        if choice == "1":
            sql = (f"SELECT `cp_id`, `cp_name`, `cp_industry`, `job_title`, `job_description`,"
                   f" `job_doc`, `contract`, DATE_FORMAT(date_added, '%d,%M,%Y') FROM `org` "
                   f"WHERE posted_by ='{data}'")  # for users jobs
        elif choice == "2":
            sql = (f"SELECT `cp_id`, `cp_name`, `cp_industry`, `job_title`, `job_description`, "
                   f"`job_doc`, `contract`, DATE_FORMAT(date_added, '%d,%M,%Y') FROM `org` "
                   f"WHERE posted_by !='{data}'")  # not users jobs
        elif choice == "3":
            load()
            clear_screen()
            self.home(self)
        else:
            load()
            clear_screen()
            print("Invalid Choice Try Again", file=sys.stderr)
            self.min_view(self)
        load()
        clear_screen()
        self.view_jobs(self, sql)

    @staticmethod
    def view_jobs(self, sql):  # function to List All Jobs Posted
        try:
            db.execute(sql)  # query to send
            rows = db.fetchall()  # get all data from db table
            if len(rows) > 0:
                column = ['Company Code', 'Company/Person Name', 'Industry', 'Job Title', 'Job Description',
                          'Job Requirements', 'Contract Details', 'Date Added']  # table headers
                table = PrettyTable(column)  # create table with pretty tables
                for row in rows:  # loop through db data and add every returned row to table
                    table.add_row(row)  # add row to table
                print("\033[1m\033[32m")
                print(table, "\033[0m")  # Display full table after adding column and rows
                self.min_view(self)
            else:
                print("\033[1m\033[31m.................No Jobs Found !!....................\033[0m")  # if no jobs found
                self.min_view(self)
        except Exception as e:  # if any error happened
            print("\n", e, file=sys.stderr)
            self.view_jobs(self)

    @staticmethod
    def view_jobs_no_recall(self, sql):  # function to List All Jobs In Posted
        try:
            db.execute(sql)  # query to send
            rows = db.fetchall()  # get all data from db table
            if len(rows) > 0:
                column = ['Company Code', 'Company/Person Name', 'Industry', 'Job Title', 'Job Description',
                          'Job Requirements', 'Contract Details', 'Date Added']  # table headers
                table = PrettyTable(column)  # create table with pretty tables
                for row in rows:  # loop through db data and add every returned row to table
                    table.add_row(row)  # add row to table
                print("\033[1m\033[32m")
                print(table, "\033[0m")  # Display full table after adding column and rows
            else:
                load()
                clear_screen()
                print("\033[1m\033[31m.................No Jobs Found !!....................\033[0m")  # if no jobs found
                self.min_view(self)
        except Exception as e:  # if any error happened
            load()
            clear_screen()
            print("\n", e, file=sys.stderr)
            self.view_jobs(self)


def main():
    logo()
    home_load()
    clear_screen()
    logo()
    # Remove pass and add menu 
    print(
        "\n\033[1m\033[34m --- Welcome\033[0m \033[1m\033[33mto \033[0m\033[1m\033[36mjoblink\033[0m "
        "\033[1m\033[35mJobs---\033[0m\n")
    print("\033[1m\033[35mChoose from the above\033[m\n")
    print("\033[1m\033[31m [1]\033[0m \033[1m\033[34mSign Up\033[0m")
    print("\033[1m\033[31m [2]\033[0m \033[1m\033[34mSign In\033[0m")
    print("\033[1m\033[31m [3]\033[0m \033[1m\033[34mExit\033[0m")
    choices = input("\n\033[1m\033[34mEnter Choice:\033[0m ")
    joblink(choices)


main()
