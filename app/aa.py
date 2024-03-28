import psycopg2

def connect_to_postgres():
    try:
        # Establishing a connection to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="fastapi",
            user="postgres",
            password="8388",
            host="localhost",
            port="5432"
        )
        
        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        
        # Executing a SQL query
        cursor.execute("SELECT version();")
        
        # Fetching the single row output of the query
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
        
        # Closing the cursor and connection
        cursor.close()
        conn.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

if __name__ == "__main__":
    connect_to_postgres()
