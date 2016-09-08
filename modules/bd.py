import pymysql

class myDB:

    conn = None
    def __init__(self):
        #Connect to MySQL database
        if self.conn is None:
            cur = pymysql.connect(host='localhost',database='pythonSQL',user='root',password='mysql')
            self.conn = cur

    def con(self):
        return self.conn

    def connect(self):
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM `catalog`;')
        for r in cur:
            print(r)


    def __del__(self):
        if self.conn is not None:
            self.conn.close()