# import psycopg2 as ps, re, csv
import re, csv, psycopg2 as ps
from configparser import ConfigParser

# All the required commands
commands = {
    'select':       """SELECT name FROM {} 
                    WHERE name = '{}' AND surname = '{}'""",
    
    'create':      """CREATE TABLE {} (
                    name TEXT,
                    surname TEXT,
                    phone TEXT)""",
            
    'insert':       """INSERT INTO {} (name, surname, phone)
                    VALUES ('{}', '{}', '{}') """,
    
    'update':       """UPDATE {} 
                    SET phone = '{}' WHERE name = '{}' AND surname = '{}'""",
    
    'delete':       """DELETE FROM {} 
                    WHERE name = '{}' OR surname = '{}' OR phone = '{}'""",
                
    'select_pag':   """SELECT * FROM {}
                    ORDER BY {} LIMIT {} OFFSET {}""",
    
    'search':       """SELECT * FROM {} 
                    WHERE name ILIKE '{}' OR surname ILIKE '{}' OR phone ILIKE '{}'"""
    
}

# Function to configure database
def config(filename='data.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

# To check if the number is valid in Kazakhstan
def isValid_KZ(number):
    match = re.search("[a-zA-Z]", number)
    
    if (
        ((number[0] == '+' and len(number) == 12)
        or 
        (number[0] == '8' and len(number) == 11))
        and
        not match):
        return True
    
    return False

# 
def print_beautifully(list):
    print(f"|NAME|{' ' * 11}|SURNAME|{' ' * 8}|NUMBER|")
    print('_' * 50)
    for row in list:
        print(f"|{row[0]}|{' ' * (15-len(row[0]))}|{row[1]}|{' ' * (15-len(row[1]))}|{row[2]}|")
        print('-' * 50)
# Class with executable functions
class CMD:
    def init(self, cursor):
        self.cur = cursor
    
    def doEXIST(self, name, surname):
        # Function to check if the user is already exists
        self.cur.execute(commands['select'].format(self.table, name, surname))
        return len(self.cur.fetchall())
    
    def create(self):    
        # To create a new table
        self.cur.execute(commands['create'].format(self.name))
        print(f"TABLE with name {self.name} successfully created")
    
    def insert(self):        
        # To insert list of data and update if already exists
        invalid = []
        updated = 0
        
        for data in self.list:   
            # Check if data exist and is the number is valid
            if not self.doEXIST(data[0], data[1]):
                if isValid_KZ(data[2]):
                    self.cur.execute(commands['insert'].format(self.table, data[0], data[1], data[2]))
                else:
                    invalid.append(data)
                
            else:
                if isValid_KZ(data[2]):
                    updated += 1
                    self.cur.execute(commands['update'].format(self.table, data[2], data[0], data[1]))
                else:
                    invalid.append(data)
        
        # Print the executed command and all invalid data (if any)            
        if (len(invalid) != len(self.list) and updated != len(self.list) - len(invalid)):
            print(f"DATA of length {len(self.list) - len(invalid)} inserted")
        if updated:                     
            print(f"DATA of length {updated} updated")
        if len(invalid):
            print(f"DATA with incorrect number (total {len(invalid)}) \n") 
            print_beautifully(invalid)
    
    def delete(self):    
        # To delete data by name or surname or phone
        given = None
        if   self.name    != None: given = self.name
        elif self.surname != None: given = self.surname
        elif self.phone   != None: given = self.phone
        
        if given:
            self.cur.execute(commands['delete'].format(self.table, given, given, given))
            print("DATA was deleted")
        else:
            print("No data to delete from")
    
    def select(self):   
       # To query data with pagination 
        self.cur.execute(commands['select_pag'].format(self.table, self.order, self.limit, self.offset))
        data = self.cur.fetchall()
        print(f"The queried data from table {self.table}:\n")
        print_beautifully(data)
    
    def search(self):    
        # To search data with given pattern
        if self.pattern:
            self.cur.execute(commands['search'].format(self.table, self.pattern, self.pattern, self.pattern))
            data = self.cur.fetchall()
            print(f"The data satistifying the pattern = {self.pattern} \n", data) if len(data) else print(f"No matching data for pattern = {self.pattern}")
        else:
            print("No pattern to search by")
 
    def update(self):
        # To insert list of data and update if already exists
        if self.doEXIST(self.name, self.surname):
            if isValid_KZ(self.phone):
                self.cur.execute(commands['update'].format(self.table, self.phone, self.name, self.surname))
                print(f"Changed the phone number of {self.name} {self.surname} to {self.phone}")
            else:
                print('INVALID phone number!')
        else:
            print(f"Row {self.name} - {self.surname} does not exist for update")
        
    def upload(self):      
        # To upload data from csv file
        if self.path:
            with open(self.path) as csv_file:
                reader = csv.reader(csv_file)
                next(reader)
                for row in reader:
                    self.name = row[0]
                    self.surname = row[1]
                    self.phone = row[2]
                    self.list = [(self.name, self.surname, self.phone)]
                    self.insert()
            print(f"DATA have been uploaded from csv-file '{self.path}'")
        else:
            print("No PATH given")

def execute(command, **kargs):
    """The function to execute the given commands in PostgreSQL database

    Args:
        command (str) : String-name of the command
        **kargs (dict): A dictionary with needed arguments
                        EXAMPLE: execute('insert', name= User, surname= Admin, phone= 83450632143)
                        If some data is not given, default is picked or error is printed
    """
    
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = ps.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        
        # Create the class
        C = CMD(cur)
        
        # Given keyword arguments
        C.table   = kargs.get('table', 'test')
        C.name    = kargs.get('name', None)
        C.surname = kargs.get('surname', None)
        C.phone   = kargs.get('phone', None)
        C.order   = kargs.get('order', 'name')
        C.limit   = kargs.get('limit', 999)
        C.offset  = kargs.get('offset', 0)
        C.list    = kargs.get('list', [(C.name, C.surname, C.phone)])
        C.pattern = kargs.get('pattern', None)
        C.path    = kargs.get('path', None)
        
        call = {
            'create'    : C.create,
            'insert'    : C.insert,
            'delete'    : C.delete,
            'select_pag': C.select,
            'search'    : C.search,
            'update'    : C.update,
            'upload'    : C.upload
        }
        
        call[command]()
        
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
        
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
if __name__ == 'main':
    print("TEST OUTPUT:\n")
    # execute('upload', path= "dates.csv", table= 'KBTU')
    execute('select_pag', table = 'KBTU')
    # execute('search', table='KBTU', pattern= "%at")
    # execute('create', name= 'KBTU')
    # execute('insert', table= 'KBTU', name= 'Bekzat', surname= 'Tursun', phone= '87754564570')
    # execute('insert',  table='KBTU' ,list = [("Jenifer", "Lulably", "89996663322"), ("Inerajen", "Dirakgua", "+71236548899")])
    # execute('select_pag', limit= 3, offset= 1, order= 'phone')
    # execute('search', pattern= "%jen%")