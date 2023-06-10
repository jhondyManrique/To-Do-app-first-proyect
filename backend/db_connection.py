'''This line imports the mysql.connector module, 
which allows us to interact with the MySQL database.'''
import mysql.connector

'''
This code initializes a connection to the MySQL database 
using the mysql.connector.connect() method. Inside the method, 
we pass the necessary connection parameters
'''   

'''host='localhost': Specifies the host where the MySQL database is located.
In this case, it is set to localhost, indicating that the database is hosted 
on the local machine.
''' 
host = "localhost" 

'''
user='root': Specifies the username to authenticate with the MySQL database. 
Here, it is set to 'root'.
'''
user = "root"

'''
password='jhonjamanca': Specifies the password for the specified user. 
In this example, the password is set to 'jhonjamanca'.
'''

password = "jhonjamanca"

'''
database='lista': Specifies the name of the database we want to connect to. 
Here, it is set to 'lista
'''

database = "lista"
db = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database
    )