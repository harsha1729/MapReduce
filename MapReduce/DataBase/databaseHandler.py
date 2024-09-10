import psycopg2

class dbHandler:
    def __init__(self):
        self.conn = self.connecttoDB()

        if(self.conn):
            print("Connection to database is successfull")
        else:
            print("Connection to database failed..Try again")

        self.create_tables()

    def connecttoDB(self):
        '''Connect to the database'''
        try:
           return psycopg2.connect("host='localhost' dbname='mapreduce' user='harsha' password='55123'")

        except:
            return False
        
    def clearDB(self):
        '''To clear the database and tables'''
        curr = self.conn.cursor()
        curr.execute("truncate table userInfo;")
        self.conn.commit()


    
    def create_tables(self):
        curr = self.conn.cursor()
        query = '''CREATE TABLE IF NOT EXISTS userInfo(id SERIAL PRIMARY KEY, 
                    username VARCHAR(80) NOT NULL UNIQUE,
                    password VARCHAR(80) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );'''
        curr.execute(query)
        self.conn.commit()

    def add_user(self, username, password):
        '''Add a new user to the database'''
        if not username or not password:
            print("Error: Username and password must not be empty.")
            return
    
        curr = self.conn.cursor()
        query = '''
                INSERT INTO userInfo(username, password) VALUES('
                ''' + username + "' , '" + password + "' );" 
        curr.execute(query)
        self.conn.commit()

# if __name__=='__main__':
#     db = dbHandler()