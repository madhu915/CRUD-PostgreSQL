from db_conn import config
import psycopg2

def ex3():
    sql = """ALTER TABLE country_new2 DROP region_id"""
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
        curs.execute("Select * FROM country_new2 LIMIT 0")
        colnames = [desc[0] for desc in curs.description]
        for col in colnames:
            print(col)

        # Query here
        curs.execute(sql)

        # After executing
        print("-"*15, "Before executing", "-"*15)
        curs.execute("Select * FROM country_new2 LIMIT 0")
        colnames = [desc[0] for desc in curs.description]
        for col in colnames:
            print(col)

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
    ex3()

        

