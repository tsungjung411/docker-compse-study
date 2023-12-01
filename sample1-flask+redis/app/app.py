#import os
#os.system('pip install redis')

from flask import Flask
from redis import Redis

print('>>>> name:', __name__)
app = Flask(__name__)
redis = Redis(host='my-redis', port=6379)

@app.route('/')
def index():
  print("[TJ][my-web][debug] >>>> index")
  redis.incr('hits')
  return f'This page has been visited {redis.get("hits")} times'


if __name__  == '__main__':
  print('[TJ][my-web][debug] >>>> run:')
  app.run(host='0.0.0.0', port=80)
