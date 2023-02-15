from db_conn import config
import psycopg2

def ex2():
    sql = """CREATE TABLE IF NOT EXISTS jobs2(
            job_id SERIAL PRIMARY KEY,
            job_title VARCHAR (255) NOT NULL DEFAULT '',
            min_salary NUMERIC(6) DEFAULT 8000,
            max_salary NUMERIC(6) DEFAULT NULL)"""
    conn = None  
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        print("Connected database successfully")
        # create a new cursor
        curs = conn.cursor()
      
        print("-"*15, "Before executing", "-"*15)
        curs.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'""")
        for table in curs.fetchall():
            print(table)

        # Query here
        curs.execute(sql)

        # After executing
        print("="*15, "After executing", "="*15)
        curs.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'""")
        for table in curs.fetchall():
            print(table)


        # commit the changes to the database
        conn.commit()
        # close communication with the database
        curs.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__=='__main__':
    ex2()

        

