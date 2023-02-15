from db_conn import config
import psycopg2

def ex5():
    sql = """UPDATE employees SET
            email='not available' WHERE department_id=80 AND commission_pct<0.20"""
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
        curs.execute("Select * FROM employees")
        records = curs.fetchall()
        print("Total rows are:  ", len(records))
        for row in records:
            print(row)


        # Query here
        curs.execute(sql)

        # After executing
        print("-"*15, "Before executing", "-"*15)
        curs.execute("Select * FROM employees")
        records = curs.fetchall()
        print("Total rows are:  ", len(records))
        for row in records:
            print(row)

        curs.close()

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
    ex5()

        

