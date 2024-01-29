from os import makedirs
from os.path import exists
import os


"""
makedirs 模块提供了创建文件夹（即目录）的方法。makedirs 函数可以递归地创建目录，即使父目录不存在也可以创建。如果目录已经存在，则不会引发错误。
exists 函数接受一个路径作为参数，并返回一个布尔值，指示该路径是否存在。如果路径存在，则返回 True；如果路径不存在，则返回 False。
"""

RESULTS_DIR = "test/sad"
# makedirs(f'{pa}/path', exist_ok=True)    # 设置了 exist_ok=True 参数 即使目录已经存在也不会引发异常。

# # 检测目录不存在就创建
# # 方法一
# exists(RESULTS_DIR) or makedirs(RESULTS_DIR)  # or: 只要第一个值是False,就会执行第二个值
# 方法二
if not exists(RESULTS_DIR):
    makedirs(RESULTS_DIR)




