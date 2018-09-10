from datetime import datetime
import matplotlib.pyplot as plt
from load_database import Load
from MypseudoSQL import Table

"""
use tick_9_2.db
select * from tick_min_log
"""

src = "data/tick_9_2.db"
db = Load(src)

"""
since 2017/1/1
get the average records per minute ()
get the close price every minute
calculate the amplitude % critical curve
this script would depend on day trading 
"""

raw_data = db.get_per_min(start="2017-01-01", drop_night_trade=True)

raw_close = db.get_per_min(start="2017-01-01", drop_night_trade=True, predicate="group by Date;")

columns = ("Date", "Time", "Open", "High", "Low", "Close", "TotalVolume")
data = map(lambda record: dict(zip(columns, record)), raw_data)  # a map generator, dict of list
# close = map(lambda record: dict(zip(columns, record)), raw_close)  # a map generator, dict of list

# data = [dict(zip(columns, record)) for record in raw_data]
close = [dict(zip(columns, record)) for record in raw_close]


def one_day_filter(data, date):
    return filter(lambda record: date == record["Date"], data)


previous = close[139]
oneday = close[140]
print(previous)
print(oneday)
select = one_day_filter(data, oneday["Date"])
amp = []
for i, row in enumerate(select):
    amp_i = abs(row["Close"] - row["Open"]) / previous["Close"] * 100
    amp += [amp_i]
    print(row, "%.4f %s" % (amp_i, "%"))


def moving_avg(amp, m=5, n=5):
    block_avg = [sum(amp[i:i+n])/float(n) for i in range(0, len(amp), n)]
    return [sum(block_avg[i:i+m])/float(m) for i in range(len(amp) - m + 1)]


print("one day trading data length:", i + 1)
ma_5_5 = sorted(moving_avg(amp, 5, 5), reverse=1)
ma_35_5 = sorted(moving_avg(amp, 35, 5), reverse=1)
ma_200_5 = sorted(moving_avg(amp, 200, 5), reverse=1)
print(len(ma_5_5))
print(len(ma_35_5))
print(len(ma_200_5))
plt.plot(ma_5_5, '-')
plt.plot(ma_35_5, '-')
plt.plot(ma_200_5, '-')
plt.show()
# trad_day = Table(["Date", "Time", "Open", "High", "Low", "Close", "TotalVolume"])
#
# for record in trading_day.rows:
#     if record["Date"] not in map(lambda row: row["Date"], trading_day.rows):
#         trad_day.insert(record)
#
# print("data length:", len(table.rows))
# print("close length:", len(close_13_45.rows))
# print("trading days:", len(trad_day.rows))

# for key, val in table.rows[-1].items():
#     print(key, type(val))

# time = [datetime.strptime("T".join(record[:2]), "%Y/%m/%dT%H:%M:%S")
#         for record in data_per_min]
#
# print("since 2017 (day and night):", len(data_per_min))
# print("every close price (day trade):", len(every_close))


