import pyodbc

server = "HASITHA-LAP\\NS16"
database = "Cricket_Tournament_db"
username = "sa" 
password = "9sense@$$"
connection_string = "Driver={SQL Server};Server="+server+";Database="+database+";User="+username+";Password="+password+";"

def establish_db_connection():
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except pyodbc.Error as e:
        # Handle the connection error
        print(f"Database connection error: {str(e)}")
        return None
    
def close_db_connection(conn):
    if conn:
        conn.close()

def read_from_db(query, *parameters):

    conn = establish_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            rows = cursor.fetchall()
            
            return rows
        except pyodbc.Error as e:
            print(f"Database error: {str(e)}")
            close_db_connection(conn)
        finally:
            close_db_connection(conn)
    else:
        print("Failed to establish a database connection.")
        return None