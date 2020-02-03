import redis

class RedisHandler():
    
    def __init__(self, app):
        self.redis = redis.StrictRedis(
                    host=app.config['REDIS_HOST'],
                    port=app.config['REDIS_PORT'],
                    db=app.config['REDIS_DB']
                )
        self.redis.flushdb()

    def save(self, data):
        return self.redis.mset(data)

    def get(self, key):
        return self.redis.get(key)