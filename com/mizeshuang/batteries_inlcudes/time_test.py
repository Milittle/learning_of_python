# python内置对时间的支持
from datetime import datetime
print(datetime.now()) # 2017-06-30 16:11:34.408226 获取系统时间


# 自定义时间
print(datetime(2017, 6, 30, 16, 13)) # 2017-06-30 16:13:00

# 将datetime转换为timestamp
print(datetime.now().timestamp())

# 将timestamp转化为datetime
print(datetime.fromtimestamp(1498824384.357802))

# 将timestamp转化为utc标准时间
print(datetime.utcfromtimestamp(1498824806.419829)) #utc0时间

# 从str转化为datetime
print(datetime.strptime('2017-6-30 8:18:59', '%Y-%m-%d %H:%M:%S'))

# 将datetime转换为str
print(datetime.now().strftime('%a,%b,%d %H:%M'))

# datetime的加减，需要timedelta类来做辅助 使用timedelta可以很容易得到附近几天的时间
from datetime import timedelta
print(datetime.now()+timedelta(hours = 10)) # days,minutes,seconds
print(datetime.now()+timedelta(minutes = 10))
print(datetime.now()+timedelta(seconds = 500))

# 本地时间转换为utc-0时间
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours = 8)) # 设置时区
now = datetime.now() # 获取当前时间
dt = now.replace(tzinfo = tz_utc_8) # 强制将当前时间转换为设定时区的时间
print(dt) # 打印市区时间

# utc-0时间转换为任意时区时间，也就是带有时区的函数可以使用astimezone可以直接转换为相应的时区
print(datetime.utcnow()) # 拿到的时间是utc-0的时间 但是不是带有utc的标准时间

print(datetime.utcnow().replace(tzinfo = timezone.utc).astimezone((timezone(timedelta(hours = 8))))) # 直接将utc0转化为utc8
# 需要注意的是在时区转换函数中，需要将原始时间转换为utc时间
# 这样才能进行时区的转换
# 而且在时区转换的时候，replace函数和astimezone这两个函数都可以进行转换，只不是前者是当前时间就行
# 后者必须为时区时间，前者接收的参数是一个dict是tzinfo = timezone对象 后者是接收一个timezone对象