from rq import Worker

from connection_settings import queue, redis_connection

if __name__ == "__main__":
    worker = Worker([queue], connection=redis_connection)
    worker.work()
