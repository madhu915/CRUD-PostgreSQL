from db_conn import config
import psycopg2

def ex6():
    sql = """SELECT first_name,last_name,salary,0.15*salary AS PF FROM employees"""

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
      
        # Query here
        curs.execute(sql)

        records = curs.fetchall()
        print("Total rows are:  ", len(records))
        for row in records:
            print(' | '.join(map(str, row)))


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

        

