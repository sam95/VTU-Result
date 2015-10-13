
from vtu_reval import vtu
import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="user", # your username
                      passwd="yourpassword", # your password
                      db="databasename") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT email,name,count,court FROM dclusers where count=0")
count=0

# print all the first cell of all the rows
#print len(cur.fetchall())
for row in cur.fetchall() :
	name=row[1]
	email=row[0]
	court=row[3]
	if(row[3]=='VTU revaluation results'):
		count=vtu(row[1],row[0])
		if count==1:
			cur.execute("UPDATE `dclusers` SET `count` = 1 WHERE name =name and email=email and court='VTU revaluation results'")
#the above statement is used to change the count so that the user doesn't get multiple emails even if it's run continuously
