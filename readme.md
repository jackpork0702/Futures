# Futures

## My pseudo SQL

A python implementation of structure query language

### Usage

***MypseudoSQL*.*Table*(*columns*)**

```
from MypseudoSQL import Table

table = Table(["col_0", "col_1", ...])

table.insert([val_0, val_1, ...])
```
### Parameters

columns: specifying the names of the table's columns 
> list

### Attributes

rows: a dataset as a row which values corresponding to table's columns
> list


### Methods
<table>
  <tr>
    <td>MypseudoSQL</td>
    <td>SQL</td>
  </tr>
  <tr>
    <td>insert(row_values)</td>
    <td>INSERT INTO</td>
  </tr>
  <tr>
    <td>update(updates, predicate)</td>
    <td>UPDATE</td>
  </tr>
  <tr>
    <td>delete()</td>
    <td>DELETE</td>
  </tr>
  <tr>
    <td>select()</td>
    <td>SELECT</td>
  </tr>
  <tr>
    <td>limit(lim)</td>
    <td>LIMIT</td>
  </tr>
  <tr>
    <td>where()</td>
    <td>WHERE</td>
  </tr>
  <tr>
    <td>group_by(group_by_columns, aggregates)</td>
    <td>GROUP BY</td>
  </tr>
  <tr>
    <td>order_by(order)</td>
    <td>ORDER BY</td>
  </tr>
  <tr>
    <td>join(other_table)</td>
    <td>JOIN</td>
  </tr>
</table>


**insert**(row_values)

> dict from column names to values
>
> parameter: 
>> row_values: dict of list
>
> return:
>> void

**update**(updates, predicate)

> updates will be a dict whose keys are the columns to update and whose values are the new values for those fields. 
>>
> predicate is a predicate that returns True for rows that should be updated, False otherwise
>
> parameter:
>> updates: dict
>
> return:
>> void

**delete**(predicate=function)

> to delete rows from a table
>
> parameter:
>> predicate: a predicate function, default=lambda row: True
>
> return:
>> void

**select**(keep_columns=None, additional_columns=None)

> keep_columns specifies the name of the columns you want to keep in the result.
>
>additional_columns is a dictionary whose keys are new column names and whose
values are functions specifying how to compute the values of the new columns.
>
> parameter:
>> keep_columns: list, default=None
>>
>> additional_columns: dict, {column: predicate function}, default=None
>
> return: Table
>>

**limit**(lim)

> to select a limited number of records
>
> parameter:
>> lim: int
>
> return:
>> Table

**where**(predicate=function)

> defines the condition to be met for the rows to be returned
>
> parameter:
>> predicate: a predicate function, default=lambda row: True
>
> return:
>> Table

**group_by**(group_by_columns, aggregates, having=None)

> group together rows with identical values in specified columns and produces aggregate values
>
> parameter:
>> group_by_columns: list
>>
>> aggregates: dict, {col: predicate function}
>>
>> having:  a predicate function, default=None
>
> return:
>> Table

**order_by**(order)

> sorts data returned by a predicate function
>
> parameter:
>> order: a predicate function
>
> return:
>> Table

**join**(other_table, left_join=False)

> join two tables
>
> parameter:
>> other_table: Table
>> 
>> left_join: boolean, default=False
>
> return:
>> Table


## Load
```
from load_database import Load

db = Load("data/tick_9_2.db")

data_each = db.get_each(lim=10)
data_per_min = db.get_per_min()
```
**function**

>*get_each*(table='tick_log', lim=10)
>
>>parameter
>>> table: str, default='tick_log'
>>>
>>> lim: int, default=10
>>
>>return
>>> tuple of list
>
>*get_per_min*(table='tick_min_log', lim=10)
>
>>parameter
>>> table: str, default='tick_min_log'
>>>
>>> lim: int, default=10
>>
>>return
>>
>>> tuple of list

## Database
```
tick_9_2.db
    |
    ├─ tick_log (  # 每筆成交資訊
    |    |
    |    ├─ Date date,
    |    |
    |    ├─ Time time 
    |    |
    |    ├─ Price float,
    |    |
    |    └─ Volume int)
    |
    └─ tick_min_log (  # 每分鐘成交資料
         |
         ├─ Date date,
         |
         ├─ Time time,
         |
         ├─ Open float,
         |
         ├─ High float,
         |
         ├─ Low float,
         |
         ├─ Close float,
         |
         └─ TotalVolume int
```
