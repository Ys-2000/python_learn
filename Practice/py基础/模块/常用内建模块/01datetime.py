from datetime import datetime, timedelta, timezone
import re
# now = datetime.now() # 获取当前datetime
# print(now)
#
# # 获取指定日期和时间
# dt = datetime(2018, 7, 19, 12, 20)
#
# # datetime转换为timestamp
# tdt = dt.timestamp() # 把datetime转换为timestamp
# print(tdt)
#
# # timestamp转换为datetime
# print(datetime.fromtimestamp(tdt))      # 本地时间
# print(datetime.utcfromtimestamp(tdt))   # UTC时间

# # str转换为datetime
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)
#
# # datetime转换为str
# now = datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))

# # datetime加减
# now = datetime.now()
# print(now)
# print(now + timedelta(hours=10))
# print(now - timedelta(days=1))
# print(now + timedelta(days=2, hours=12))

# # 本地时间转换为UTC时间
# tz_utc_8 = timezone(timedelta(hours=8))     # 创建时区UTC+8:00
# now = datetime.now()
# print(now)
# dt = now.replace(tzinfo=tz_utc_8)           # 强制设置为UTC+8:00
# print(dt)

# # 时区转换
# # 拿到UTC时间，并强制设置时区为UTC+0:00:
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# # astimezone()将转换时区为北京时间:
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print(bj_dt)
# # astimezone()将转换时区为东京时间:
# tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt)
# # astimezone()将bj_dt转换时区为东京时间:
# tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt2)

# 练习
# 设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，
# 请编写一个函数将其转换为timestamp：

def to_timestamp(dt_str, tz_str):
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    l = tz_str.split('C')[1].split(':')[0]
    k = int(l)
    tz_utc_k = timezone(timedelta(hours=k))
    dt = cday.replace(tzinfo=tz_utc_k)
    return dt.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
