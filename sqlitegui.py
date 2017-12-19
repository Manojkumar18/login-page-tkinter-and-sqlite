import sqlite3

conn =sqlite3.connect('login.db')
c=conn.cursor()
def read_db(logName,logPassword):
    if logName=='' and logPassword=='':
        print('plese enter the details')
    else:
        line=("SELECT * FROM logindb WHERE Name= " + "'" + logName + "' ")
        c.execute(line)
        data =c.fetchall()
        for num in data:
            if num[0]==logName :
                if num[1]==logPassword:
                    print("Your login ")
                else:
                    print("check your Password is worng")
        if data == []:
            print("check your Name worng")
            print("No data enter on data base")
