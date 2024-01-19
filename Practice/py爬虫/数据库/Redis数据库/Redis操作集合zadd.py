import redis

# 1) 直连模式
r = redis.Redis(host='127.0.0.1', port=6379, db=2, password='', decode_responses=True)
# decode_responses=True 表示获取到的Redis数据是否需要解码 默认是False  设置后就不需要.decode('utf-8')

r.zadd("香烟",{"将军":10,"中华":50,"南京":15,"红塔山":7})

r.zincrby("香烟",-5,"南京")     # 分数加减