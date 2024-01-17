# selenium 使用get_cookies()获取到的cookie是字符串形式，可以使用该方法转换为字典格式

cookies_dict = {'Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273': '1705460056;Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273=1705460056;r=3290;t=0372fa8016b9c760a454109555a9ddaf'}

cookie_string = ";".join([f"{key}={value}" for key, value in cookies_dict.items()]) # 把获取到的字典 转换成字符串格式
print(cookie_string)