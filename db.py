print("Database setup goes here")

import pymysql as pyms


my_con = pyms.connect(host= 'localhost', user ='root', database = 'todolist' , passwd='Cassanova911@')
print(my_con)
print('connection succefully')

myCursor = my_con.cursor()
print("done")