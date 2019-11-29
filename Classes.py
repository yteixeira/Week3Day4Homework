import pyodbc

# database is the main class, it will make the connection to the database
# and it will hold all the main query functions
class connection():
    def __init__(self, driver, server, database, username, password):
        self.driver = driver
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def make_connection(self):

        #makes the connection to the database
        self.database_connection = pyodbc.connect('DRIVER={'+self.driver+'};'
                                                  'SERVER='+self.server+';'
                                                  'DATABASE='+self.database+';'
                                                  'UID='+self.username+';'
                                                  'PWD='+self.password)
        self.cursor = self.database_connection.cursor()
        return self.cursor

class region():
    def __init__(self, region_description):
        self.region_description = region_description

class shippers():
    def __init__(self,company_name, phone):
        self.company_name = company_name
        self.phone = phone

class main_program():
    def __init__(self):
        self.result = ""

    def run(self, sql):
        connect = connection("ODBC DRIVER 17 for SQL SERVER", "localhost,1433", "NorthWind", "sa", "Passw0rd2018")
        cursor = connect.make_connection()
        cursor.execute(sql)
        cursor.commit()


program = main_program()
query = input("Hello .. write sql ")
program.run(query)



