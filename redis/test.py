import redis

host = '127.0.0.1'
port = 6379

pool = redis.ConnectionPool(host=host, port=port)

r = redis.Redis(connection_pool=pool)

r.set('foo:test:121464213', 'bar')
print(r.get('foo'))