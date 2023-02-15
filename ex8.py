from db_conn import config
import psycopg2

def ex6():
    sql = """INSERT INTO employees VALUES(300,'Ben','Affleck','ABC','198','1987-06-17','PU_CLERK',7000.00,0.10,204,70)"""
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
        print("-"*15, "After executing", "-"*15)
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
    ex6()

        

