# 在浏览器中直接负责的cookie是字符串格式的，可以使用该方法转换为字典



# cookie = "GUID=6af04b03-3f41-4168-a1ca-ced5f52d862e;sajssdk_2015_cross_new_user=1;acw_sc__v2=659f61392208ddc22c8735bfb41febdeb8de3c65;Hm_lvt_9793f42b498361373512340937deb2a0=1704943931;accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.28491325E20496063%26s%3D92129a48a2295771;ssxmod_itna=eq0iIqQtQD/KtxnqD=GFDK4;c_channel=0"

cookie_string = "Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273=1705460056;Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273=1705460056;r=3290;t=0372fa8016b9c760a454109555a9ddaf"

# # 传统的循环
# lit = cookie_string.split("; ")
# dic = {}
# for i in lit:
#     k, v = i.split("=",1)   # cookie2中的value存在多个=，这里split()设置1，表示只取一次
#     dic[k.strip()] = v.strip()      # strip()去空格
# print(dic)

# 列表推导式
# cookies_dict = dict(cookie.split('=', 1) for cookie in cookie_string.split('; '))
cookies_dict = {key.strip(): value.strip() for key, value in (cookie.split('=', 1) for cookie in cookie_string.split('; '))}
print(cookies_dict)