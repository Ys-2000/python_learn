## Python打包Docker

### 一、编写 Dockerfile
```dockerfile
# 使用 Python 官方镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . /app

# 安装依赖
RUN pip install -r requirements.txt

# 设置环境变量
ENV PYTHONUNBUFFERED 1

# 启动应用
CMD ["python", "app.py"]
```
###  二、构建镜像
`docker build -t project_name:tag .`
`docker build -t proxypool_cqc:v1 .`

这个命令告诉 Docker在当前目录中寻找 Dockerfile，并使用该文件中的指令来构建一个新的镜像。 
-t project_name:tag 则是为新镜像命名并添加一个标签。project_name 是镜像的名称，tag 是版本或者标识符。
 . 表示 Dockerfile 所在的当前目录。


###  三、创建容器
在目标服务器上安装 Docker，并通过以下命令运行镜像
`docker run -d -p host_port:container_port --name test project_name:tag`
`docker run -p 8080:8080 --name dlc_cqc proxypool_cqc:v1`

docker run: 运行一个容器
-d 后台运行容器
-p host_port:container_port 将容器的端口映射到宿主机的端口 8080:8080
--name <容器名称> 是给容器命名，不添加系统会自动生成名称
project_name:tag 容器名称:版本号

### 四、更新文件
docker cp /本地路径/要复制的文件 容器name:/容器内目标路径

docker cp 将目录或文件复制到运行中的Docker容器中的目录

**例如**：

`docker cp app.py 容器ID:/app/app.py`

将本地的 app.py 文件复制到运行中的 Docker 容器的 /app 目录下
