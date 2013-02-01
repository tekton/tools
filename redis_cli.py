import os
import redis


class R:
    """
        To make things a little easier, and use the connection pool, one class
        to use redis for all of the functions and other classes in the player
        app
    """
    redis_connection = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
    r = redis.from_url(redis_connection)
