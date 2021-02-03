import mysql.connector
if __name__ == "__main__":
    db_manager

class db_manager:
    def __init__(self,host,user,password):
        self.__db = mysql.connector.connect(
            host= host,
            user= user,
            password=password
        )
        self.__cursor = self.__db.cursor()
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS pylogin")
        self.__cursor.execute("USE pylogin")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(64), email VARCHAR(128), password VARCHAR(2048))")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Register\n2. Login\n3. Edit\n4. Delete\n5. Show all users\n6. Search by name\n0 Exit\n ===>> "))
            if choice == 1:
                answer = self.__register()
                print(answer)
            elif choice == 2:
                answer = self.__login()
                print(answer)
            elif choice == 3:
                answer = self.__edit()
                print(answer)
            elif choice == 4:
                answer = self.__delete()
                print(answer)
            elif choice == 5:
                answer = self.__showAllUsers()
                print(answer)
            elif choice == 6:
                answer = self.__searchUsers()
                print(answer)
            elif choice == 0:
                exit = True
                print("Bye!")
            else:
                print("Wrong choice.")

    def __register(self):
        username = input("Username ")
        email = input("Email ")
        password = input("Password ")
        confirm_password = input("Confirm password ")

        if password != confirm_password:
            return "Password do not match."

        self.__cursor.execute(
            "SELECT email FROM users WHERE email = '" + email + "'")
        result = self.__cursor.fetchone()

        if result != None:
            return "User exists"

        else:
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            val = (username, email, password)
            self.__cursor.execute(sql, val)
            self.__db.commit()
            return "User successfully created"

    def __edit(self):
        enter_email = input("Enter email user whom want to edit : ")
        edit_username = input("Enter name for edit : ")
        edit_email = input("Enter email for edit : ")
        edit_password = input("Enter password for edit : ")

        edit_sql = "UPDATE `users` SET `username`=%s,`email`=%s,`password`=%s WHERE `email` = %s"
        edit_val = (edit_username, edit_email, edit_password, enter_email)
        self.__cursor.execute(edit_sql, edit_val)
        self.__db.commit()
        return "User successfully edited"

    def __delete(self):
        de_email = input("Enter email user whom want to delete : ")
        del_sql = "DELETE FROM `users` WHERE `email` = %s"
        del_val = (de_email)
        self.__cursor.execute(del_sql, del_val)
        self.__db.commit()
        return "User successfully delete"

    def __showAllUsers(self):
        # show_sql = "SELECT `username`, `email` FROM `users` WHERE 1"
        self.__cursor.execute("SELECT `username`, `email` FROM `users` WHERE 1")
        # self.__db.commit()
        myresult = self.__cursor.fetchall()
        # return  self.__cursor.execute("SELECT `username`, `email` FROM `users` WHERE 1")
        for x in myresult:
            print(x)

    def __login(self):
        print("Sing in system")
        email_for_login = input("Enter email : ")
        pass_for_login = input("Enter password : ")

        self.__cursor.execute('SELECT * from `users` WHERE username="%s" AND password="%s"' % (email_for_login,pass_for_login))
        if self.__cursor.fetchone() is not None:
            print("Welcome")
        else:
            print("Login failed")
        # result =  self.__cursor.execute(login_sql)
        # for x in result:
        #     print(x)

    def __searchUsers(self):
        email_for_search = input("Enter email for find user : ")

        self.__cursor.execute('SELECT `username`, `email` FROM `users` WHERE `email` = "%s"' % (email_for_search))
        if self.__cursor.fetchone() is not None:
            print("Welcome")
        else:
            print("Search failed")


# user = raw_input "User:"
# pswd = getpass.getpass "Password"

# db = sqlite3.connect('/SABB/DATASETS/SENHAS')
# c = db.cursor()
# c.execute('SELECT * from sabb WHERE usuario="%s" AND senha="%s"' % (user, pswd))
# if c.fetchone() is not None:
#     print "Welcome"
# else:
#     print "Login failed"