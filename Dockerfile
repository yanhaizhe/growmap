FROM nginx:alpine

# 复制 HTML 文件到 nginx 默认目录
COPY 成长地图.html 小人书.html /usr/share/nginx/html/

# 复制 nginx 配置
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
