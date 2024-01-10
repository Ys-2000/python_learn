# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pymongo
from caipiao.settings import MYSQL

"""
存储的方案:
    1.要做数据分析     存储到csv  
    2.牵扯到业务逻辑   存储到MySQL
    3.大批量数据储备   存储到MondoDB 
    4.文件的存储       如:文件、图片、视频
"""

# 注意：管道是默认是不生效的，需要去settings里面去开启管道
class CaipiaoPipeline:
    """
    1.我们希望的是，在爬虫开始的时候，打开这个文件
    在执行过程中，不断的往里存储数据
    在执行完毕时，关掉这个文件
    """

    def open_spider(self, spider):
        self.f = open('./双色球.csv', mode='a', encoding='utf-8')

    def close_spider(self, spider):
        if self.f:
            self.f.close()

    def process_item(self, item, spider):
        # with open('./双色球.csv', mode='a', encoding='utf-8') as f:  # process_item是一条数据执行一次 如果模式是'w'会被覆盖
        #     f.write(f"{item['qihao']},{'_'.join(item['red_ball'])},{item['blue_ball']}\n")

        self.f.write(f"{item['qihao']},{'_'.join(item['red_ball'])},{item['blue_ball']}\n")
        return item


class CaipiaoMySQLPipeline:

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=MYSQL["host"],
            port=MYSQL["port"],
            user=MYSQL["user"],
            password=MYSQL["password"],
            database=MYSQL["database"]
        )


    def close_spider(self, spider):
        if self.conn:
            self.conn.close()


    def process_item(self, item, spider):   # process_item()是处理函数的专用方法(定死的)      item:数据     spider:爬虫
        try:
            cursor = self.conn.cursor()
            sql = "insert into caipiao(qihao,red_ball,blue_ball) value (%s,%s,%s)"
            cursor.execute(sql, (item['qihao'], '_'.join(item['red_ball']), item['blue_ball']))
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()

        return item      # return会传到下一个管道



class CaipiaoMongoDBPipeline:

    def open_spider(self, spider):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = self.client['testdb']  # 选择数据库
        # db.authenticate("admin","000000")     # MongoDB没有密码 不需要这个
        self.collection = db['caipiao']         # 选择数据库集合


    def close_spider(self, spider):
        self.client.close()


    def process_item(self, item, spider):
        data = {"qihao": item['qihao'], 'red_ball': item['red_ball'], 'blue_ball': item['blue_ball']}
        self.collection.insert_one(data)
        return item