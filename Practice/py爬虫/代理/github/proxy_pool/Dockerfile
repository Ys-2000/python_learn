FROM python:3.6-alpine

MAINTAINER jhao104 <j_hao104@163.com>

WORKDIR /app

COPY ./requirements.txt .

# apk repository    # 更改 Alpine Linux 的软件源为国内镜像
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories

# timezone  #安装时区设置，并将时区设置为亚洲上海
RUN apk add -U tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && apk del tzdata

# runtime environment   # 安装一些基础的开发依赖
RUN apk add musl-dev gcc libxml2-dev libxslt-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev

# 将当前目录下的文件复制到镜像中
COPY . .

# 将容器的端口 5010 暴露出来
EXPOSE 5010

# 设置容器启动时的默认命令
ENTRYPOINT [ "sh", "start.sh" ]
