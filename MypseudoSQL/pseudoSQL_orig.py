import json
from collections import defaultdict

# create a table in SQL
class Table:
    def __init__(self, columns):
        """CREATE TABLE

        create table users (
            user_id int not null,
            name varchar(200),
            num_friends int
        );

        :param columns: [column_values, ]
        """
        self.columns = columns
        self.rows = []

    def __repr__(self):
        return str(self.columns) + "\n" + "\n".join(map(str, self.rows))

    def insert(self, row_values):
        """INSERT INTO

        insert into users (user_id, name, num_friends) values (0, "Hero", 0);

        :param row_values: [row_values, ]
        :return: void
        """
        if len(row_values) != len(self.columns):
            raise TypeError("wrong number of elements")

        self.rows += [dict(zip(self.columns, row_values))]

    def update(self, updates, predicate):
        """UPDATE

        update users
        set num_friends = 1
        where user_id = 0;

        :param updates: {column: new_value, }
        :param predicate: boolean function, f({key: value})
        :return:
        """
        for row in self.rows:
            if predicate(row):
                for column, new_value in updates.iteritems():
                    row[column] = new_value

    def delete(self, predicate=lambda row: True):
        """DELETE

        delete from users  # default delete all
        delete from users where id = 1;  # delete specific row

        :param predicate: boolean function, f({key: value})
        :return:
        """
        self.rows = [row for row in self.rows if not predicate(row)]

    def select(self, keep_columns=None, additional_columns=None):
        """SELECT

        select * from users
        select name, num_friends from users
        select user_id, length(name) as name_len from users

        :param keep_columns: ["column", ]
        :param additional_columns: {new_col: new_val}
        :return: table
        """
        if keep_columns is None:
            keep_columns = self.columns

        if additional_columns is None:
            additional_columns = {}

        result_table = Table(keep_columns + additional_columns.keys())

        for row in self.rows:
            new_row = [row[column] for column in keep_columns]

            for column_name, calculation in additional_columns.iteritems():
                new_row += [calculation(row)]

            result_table.insert(new_row)

        return result_table

    def limit(self, lim):
        """LIMIT

        select * from users limit 2

        :param lim: int
        :return: table
        """
        limit_table = Table(self.columns)
        limit_table.rows = self.rows[:lim]
        return limit_table

    def where(self, predicate=lambda row: True):
        """WHERE

        select * from users where num_friends > 1

        :param predicate: boolean function, f({key: value})
        :return: table
        """
        where_table = Table(self.columns)
        where_table.rows = filter(predicate, self.rows)
        return where_table

    def group_by(self, group_by_columns, aggregates, having=None):
        grouped_rows = defaultdict(list)

        for row in self.rows:
            key = tuple(row[column] for column in group_by_columns)
            grouped_rows[key] += [row]

        result_table = Table(group_by_columns + aggregates.keys())

        for key, rows in grouped_rows.iteritems():
            if having is None or having(rows):
                new_row = list(key)

                for aggregate_name, aggregate_fn in aggregates.iteritems():
                    new_row += [aggregate_fn(rows)]
                    result_table.insert(new_row)

        return result_table

    def order_by(self, order):
        """ORDER BY

        select * from users
        order by name

        :param order: order condition
        :return: table
        """
        new_table = self.select()
        new_table.rows.sort(key=order)
        return new_table

    def join(self, other_table, left_join=False):
        """JOIN

        select * from users
        join interests
        on users.user_id =interests.user_id

        :param other_table: the other table with a foreign key (e.g. id)
        :param left_join: boolean
        :return: table
        """
        # columns in both tables
        join_on_columns = [col for col in self.columns
                           if col in other_table.columns]

        # columns in join table
        additional_columns = [col for col in other_table.columns
                              if col not in join_on_columns]

        join_table = Table(self.columns + additional_columns)

        for row in self.rows:
            # check foreign key
            def is_join(other_row):
                return all(other_row[col] == row[col] for col in join_on_columns)

            other_rows = other_table.where(is_join).rows

            for other_row in other_rows:
                join_table.insert([row[col] for col in self.columns] +
                                  [other_row[col] for col in additional_columns])

            if left_join and not other_rows:
                """
                not []
                >> True
                """
                join_table.insert([row[col] for col in self.columns] +
                                  [None for col in additional_columns])

        return join_table


# read data
with open("user.json") as f:
    data = json.load(f)

with open("interests.json") as f:
    note = json.load(f)

# create table users
users = Table(["user_id", "name", "num_friends"])

# create table interests
interests = Table(["user_id", "interests"])

# insert data into table users
for user in data:
    users.insert(user)

# insert note into table interests
for interest in note:
    interests.insert(interest)


print users
print
print interests
print
j1 = users.join(interests).where(lambda row: row["interests"] == "Python")
print j1
# # update user_id=0, num_friend -> 1
# users.update({"num_friends": 1}, lambda row: row["user_id"] == 0)
#
# # update name="Chi", num_friend -> 10
# users.update({"num_friends": 10}, lambda row: row["name"] == "Chi")
#
# # delete user_id=1
# users.delete(lambda row: row["user_id"] == 1)
#
# # delete all
# users.delete()
#
# # select * from users
# s1 = users.select()
#
# # select name, num_friends from users
# s1 = users.select(keep_columns=["name", "num_friends"])
#
# # select length(name) as name_length from users
# s1 = users.select(keep_columns=["user_id"],
#                   additional_columns={"name_len": lambda row: len(row["name"])})
#
# select num_friends > 2 as fs>2 from users
# s2 = users.select(None, {"fs>2": lambda row: row["num_friends"] > 2})
#
# # select * from users limit 2
# # l1 = users.limit(3)
# l1 = users.select().limit(2)
#
# # select * from users where num_friends > 1
# w1 = users.where(lambda row: row["num_friends"] > 1)
#
# # select name, num_friends where num_friend < 1
# w1 = users.select(["name", "num_friends"]).where(lambda row: row["num_friends"] < 1)
#

# g1 = users.group_by(group_by_columns=["num_friends"])

# # select * from users
# # order by name
# o1 = users.order_by(lambda row: row["name"])

# print users
# print o1

