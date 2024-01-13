# import requests
# import urllib
# import json
#
#
# import urllib.request as request
# def get_comments():
#     url = 'http://sjgh.techaction.cn:8010/contest/dianshang/mall-comments/1.json?0.27832417413353383'
#     response = request.urlopen(url)
#     datas = response.read().decode('utf-8')
#     datas = json.loads(datas)
#     comment = {}
#
#     with open("comments_data", "w", encoding="utf-8") as f:
#         try:
#             for comm in datas["comments"]:
#                 comment["cmid"] = str(comm.get('id', ""))   # 该评论的id
#                 comment["nickname"] = str(comm.get('nickname' ""))  # 用户昵称
#                 comment["creationTime"] = str(comm.get('creationTime', "")) # 创建时间
#                 comment["content"] = str(comm.get('content', "")).replace(",","").replace('', "").replace('\n', "").strip()
#                 comment["score"] = str(comm.get('score', ""))
#                 comment["userClientShow"] = str(comm.get('userClientShow', ""))
#                 info = str.format("{0},{1},{2},{3},{4},{5}\n", comment["smid"], comment["nickname"], comment["creationTime"], comment["score"],)
#                 f.write(info)
#         except Exception as e:
#             print(e)
#
#
# if __name__ == "__main__":
#     get_comments()
#     print("执行完成")



import json
import urllib.request as request


# 获取10条评论信息
def get_comments():
    url = "http://sjgh.techaction.cn:8010/contest/dianshang/mall-comments/1.json?0.27832417413353383"
    response = request.urlopen(url)
    datas = response.read().decode('utf-8')
    datas = json.loads(datas)
    comment = {}  # 评论信息
    # 保存到csv文件
    with open("comments_data.csv", "w", encoding="utf-8") as f:
        try:
            for comm in datas["comments"]:
                comment["cmid"] = str(comm.get('id', " "))  # 该评论的id
                comment["nickname"] = str(comm.get('nickname', ""))  # 用户昵称
                comment["creationTime"] = str(comm.get('creationTime', ""))  # 创建时间
                comment["content"] = str(comm.get('content', "")).replace(",", "，").replace(' ', "").replace('\n',"").strip()
                comment["score"] = str(comm.get('score', ""))  # 分数
                comment["userClientShow"] = str(comm.get('userClientShow', ""))  # 评论客户端
                info = str.format("{0},{1},{2},{3},{4},{5}\n", comment["cmid"],comment["nickname"],comment["creationTime"],comment["score"],comment["userClientShow"],comment["content"])
                f.write(info)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    get_comments()
    print("执行完成")