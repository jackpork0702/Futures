import sqlite3

class Load:
    def __init__(self, database):
        self.database = database
        self.conn = sqlite3.connect(database)

    def _get(self, table, **karg):
        query = "select * from %s" % table

        if any(filter(lambda k: k in ("start", "drop_night_trade", "predicate"), karg)):
            query += " where"
            subquery = []

            if 'start' in karg.keys():
                start = karg['start']
                subquery += ["(Date>='%s')" % start]

            if "drop_night_trade" in karg.keys():
                if karg["drop_night_trade"]:
                    subquery += ["(Time>='08:45:00') & (Time<='13:45:00')"]

            query += " " + " & ".join(subquery)

        if "predicate" in karg.keys():
            predicate = karg["predicate"]
            query += " " + predicate

        if "lim" in karg.keys():
            lim = karg['lim']
            query += " limit %d" % lim

        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def get_each(self, table='tick_log', **karg):
        return self._get(table, **karg)

    def get_per_min(self, table='tick_min_log', **karg):
        return self._get(table, **karg)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
