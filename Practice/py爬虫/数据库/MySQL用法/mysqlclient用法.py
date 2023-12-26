import pandas as pd
from sqlalchemy import create_engine, types

df = pd.read_csv('data.csv')

# 当engine连接的时候我们就插入数据
engine = create_engine('mysql://root:000000@localhost/avidol?charset=utf8')
with engine.connect() as conn, conn.begin():
    df.to_sql('date', conn, if_exists='replace',index=False)

# dtype = {
#     'column1': types.VARCHAR(length=255),
#     'column2': types.Float(precision=2),
#     # 指定 DataFrame 中每一列的数据类型
#     # 例如，'column1' 和 'column2' 分别对应你 CSV 文件中的列名
# }
# # 创建数据库表结构
# df.to_sql('data', engine, if_exists='replace', index=False, dtype=dtype)
# # index=False 用于避免将 DataFrame 的索引作为数据库表的一列