from configparser import ConfigParser
import csv, psycopg2

def config(filename='database.ini', section='postgresql'):
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

def create_table(name ='contacts'):
    """ create tables in the PostgreSQL database"""
    command = f"""
        CREATE TABLE {name} (
            name TEXT PRIMARY KEY,
            num TEXT
        )
        """
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(command)
        print("Created table")
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_data(name, number, table= 'contacts'):
    """ insert a new number into the contacts table """
    command = f"""INSERT INTO {table} (name, num)
            VALUES('{name}', '{number}');"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(command)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def update_data(name, number, change, table = 'contacts'):
    """ change phone data """
    if change == 'name':
        command = f""" UPDATE {table}
                    SET name = '{name}'
                    WHERE num = '{number}'"""
    else:
        command = f""" UPDATE {table}
                    SET num = '{number}'
                    WHERE name = '{name}'"""
    conn = None
    

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(command)
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def show(table= 'contacts'):
    """ get parts provided by a vendor specified by the vendor_id """
    command = f"SELECT * FROM {table}"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
        
        cur.execute(command)
        
        for i in cur.fetchall():
            print(i)
        
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def upload(filename, table='contacts'):
    
    try:
        file = open(filename)
        csv_file = csv.reader(file)
        next(csv_file)
        
        for row in csv_file:
            insert_data(row[0], row[1])
    
    except:
        print('no such file exist!')
    finally:
        file.close()

if __name__ == 'main':
    create_table()
    show()
    insert_data('Beka', '87754564570')
    show()
    update_data('Beka', '1234', 'num')
    show()