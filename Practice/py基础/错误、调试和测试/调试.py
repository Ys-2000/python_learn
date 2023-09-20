# # assert 断言
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is 0zero!'        # assert断言 n != 0,如果断言失败，assert语句本身就会抛出AssertionError
#     return 10 / n
#
# def main():
#     foo('0')

# main()



# #logging
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)