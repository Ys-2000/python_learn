"""
strip()方法只能删除开头和结尾的指定字符或空格，而不能删除字符串内部的空格或其他字符。
如果需要删除字符串内部的字符，可以使用其他字符串处理函数，例如replace()方法或正则表达式等。
"""

# str1 = "  hello,world!  "
# str2 = "--hello,world!--"
# print(str1.strip())      # strip() 默认去除字符串开头与结尾空格
# print(str2.strip("--"))      # strip() 默认去除字符串开头与结尾空格
#
# # 当strip()函数入参有字符(单个或者多个)的时候，则得到的是删除字符串头尾相应字符(单个或者多个)后的字符串。
# str3 = "abcd123bca"
# print(str3.strip("abc"))    # 输出: d123


# cookie = "buvid3=CEDA375D-FC86-7A00-6A74-70B8B178D4CA03477infoc; b_nut=1689557103; CURRENT_FNVAL=4048; _uuid=5110C816A-3D78-F5F1-154A-C226CEAA28C904301infoc; buvid4=635F7892-A1D5-4EB5-29C9-209D8615554B04234-023071709-%2BjDGOm5ebbPnCZR9djfnyg%3D%3D; rpdid=|(u|k|)|)|u)0J'uY)mll~u|l; FEED_LIVE_VERSION=V8; header_theme_version=CLOSE; enable_web_push=DISABLE; LIVE_BUVID=AUTO8716994025512177; DedeUserID=79419334; DedeUserID__ckMd5=4eac634fba867f43; buvid_fp_plain=undefined; CURRENT_QUALITY=80; PVID=1; fingerprint=da6ce6a5aa3066e8311fc51beb113a40; home_feed_column=5; browser_resolution=1920-919; SESSDATA=06e3b166%2C1720240198%2C95047%2A11CjDGyO9-MtyfjK0BmOXdxKJ4CEikaFMJ1O2B8LlFTAHnhK2K5fSrobp2FEJQyBRtdCESVk1rY3E3azJRczJuVVJtMldxTE1xbVRMZTRqZ3N1T3dnWWM4SEFrWVYwOFFjQlAtY3hWeHBQRWVLcFVRWEVTMUp4bTJmZ3VhcEZaNXdQcEtiRFVrZ3pnIIEC; bili_jct=9123f135774dc84b179293b1c5f50819; buvid_fp=da6ce6a5aa3066e8311fc51beb113a40; sid=4gagaxhl; b_lsid=AB42DDA7_18CF63FCDDF; bp_video_offset_79419334=885192781188825157; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDUxOTc2ODcsImlhdCI6MTcwNDkzODQyNywicGx0IjotMX0.GrFVa2GEb773zfSvaSJCtHHIhJ7T6siBJezEXGPq0kg; bili_ticket_expires=1705197627"
cookie = "GUID=6af04b03-3f41-4168-a1ca-ced5f52d862e; sajssdk_2015_cross_new_user=1; acw_sc__v2=659f61392208ddc22c8735bfb41febdeb8de3c65; Hm_lvt_9793f42b498361373512340937deb2a0=1704943931; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F10%252F30%252F91%252F102849130.jpg-88x88%253Fv%253D1704944063470%26id%3D102849130%26nickname%3D%25E4%25B9%25A6%25E5%258F%258B833R9043b%26e%3D1720496063%26s%3D92129a48a2295771; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22102849130%22%2C%22%24device_id%22%3A%2218cf6637530843-0fe3c266204cae-26001951-2073600-18cf6637531d26%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%226af04b03-3f41-4168-a1ca-ced5f52d862e%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1704944070; ssxmod_itna=eq0xcDg7D=K7qDK40Lc7tDyDHAc4RxxiIQqQtQD/KtxnqD=GFDK40EogP4AErArKmmrpiDuGheeFbFtiE3eNa6j5+oDU4i8DCuBA3TDem=D5xGoDPxDeDADYoUDAqiOD7qDdLwHyzkDbxi3LxDbDin8pxGCDeKD0xwFDQKDu6IxKxhkiDDziloeN=0Yq8AF3bvmROmhqQ08D75pDlpxufEwn8deSOYLUKA3px0kqq0O9ryzCooDUBKsyPANdARYdQrNwihxj7WxzDhrtGZYp7ntNrhr7+DxtQ/N7Q2oHDxDigUNaYD==; ssxmod_itna2=eq0xcDg7D=K7qDK40Lc7tDyDHAc4RxxiIQqQtG9b5KiDBL10D7pP44SFB9lhP8KRl8W=DuiknGHFn=0KhHQnpkejrnDn4Fpdu/QkK1tzZch9rYcWUe82LyIdLrYwOw1/OBwfvaYa9DuhvGuhu/RYjR0LKnRxjKYmRD3jmGOt6DfpRi8LmKh=6ifmHSMoq4ZdvbaTRW6bBSWNHxuvhlnN1UPQ4ouW1da51QRymnOh7Qz=UD/ocYqbGLMWY4/Wis88Wv9USGCAvnQ3jnkk8WkYXMFgnPKUjcx4Wa18iEyUHoCH8IU1aoZzGTdhqKc0TLrQ5mQ6D==MiSwY7O8dexqjO0kDmohiewzYOcOYvEs2At8wmlq7aCm+e7YO+sQoFDIqDkAl5uWGXnNOiQKYb2k5dxwsGYFQwQrWDTt63KGx12DNZSmffDXip9rNDb+SDa7CHmB7CPxi7eGSH5PHf2YT4=iQdW4eC6QnnrSgFFOGi7mkohrGKH4XOgrnBFK0GnlkTfNYB=U+balxEDDw=44B+TbTwWrrmeduq4pI=H2QGDDjKDeL86D4euxYwjrAEo7KOiDD"
lit = cookie.split("; ")
dic = {}
for i in lit:
    k, v = i.split("=",1)   # cookie2中的value存在多个=，这里split()设置1，表示只取一次
    dic[k.strip()] = v.strip()
print(dic)