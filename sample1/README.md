## 顯示拜訪次數

### 功能
- my-redis: 快取 key/value
- my-web: 顯示拜訪次數，向  my-redis 要拜訪次數
- my-kong: 代理 my-web

### 檔案架構
```
├── app
│   ├── app.py
│   └── uwsgi.ini
├── docker-compose.yml
├── kong
│   ├── kong.conf
│   └── kong.yml
├── my-kong-Dockerfile
├── my-web-Dockerfile
└── run.sh
```
