# Futures

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
