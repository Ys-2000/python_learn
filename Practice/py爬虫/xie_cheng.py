import requests, logging, time, asyncio

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s: %(message)s')
#
# TOTAL_NUMBER = 10
# URL = 'https://httpbin.org/delay/5'
#
# start_time = time.time()
# for _ in range(1, TOTAL_NUMBER + 1):
#     logging.info('scraping %s', URL)
#     response = requests.get(URL)
# end_time = time.time()
# logging.info('total time %s seconds', end_time - start_time)


async def execute(x):
    print('Number:', x)
    return x

coroutine = execute(1)
print('Coroutine:', coroutine)      # 协同程序
print('After calling execute')      # 调用execute之后

loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
print("task:", task)
loop.run_until_complete(coroutine)
print("task:", task)
print('After calling loop')         # 调用loop后