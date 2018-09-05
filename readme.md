# Futures

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
>
>>return
>
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
