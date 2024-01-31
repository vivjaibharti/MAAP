import mysql.connector 
from django.db import connections

class DbConnector:
   host="localhost"
   user="root"
   database="maap_test"
   port=3306

   def __init__(self):
      #   self.connection = connections['default']
         self.connection=mysql.connector.connect(user=DbConnector.user, host=DbConnector.host,database=DbConnector.database,port=DbConnector.port)


def create_table():
    connector = DbConnector()
    with connector.connection.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS faculty_details (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), department VARCHAR(255))")
        connector.connection.commit()
