import sqlite3


class Load:
    def __init__(self, database):
        self.database = database
        self.conn = sqlite3.connect(database)

    def get_each(self, table='tick_log', lim=10):
        query = "select * from %s limit %d" % (table, lim)
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def get_per_min(self, table='tick_min_log', lim=10):
        query = "select * from %s limit %d" % (table, lim)
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()