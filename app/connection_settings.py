import os

from redis import from_url
from rq import Queue

# Create redis connection
redis_connection = from_url(os.getenv("redis_url"))
# Create queue connection
queue = Queue(name="default", connection=redis_connection)
