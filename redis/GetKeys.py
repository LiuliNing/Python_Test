import redis

host = '127.0.0.1'
port = 6379

pool = redis.ConnectionPool(host=host, port=port)

r = redis.Redis(connection_pool=pool)
keys = r.keys()
print(type(keys))
for key in keys:
    print(key)
