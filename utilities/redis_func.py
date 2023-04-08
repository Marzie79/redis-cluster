from django.conf import settings
from redis.cluster import RedisCluster

redis = RedisCluster(startup_nodes=settings.REDIS_NODES,
                        moved_response=False,
                        decode_responses=True,
                        read_from_replicas=True)

def redis_func(key, value):

    redis = RedisCluster(startup_nodes=settings.REDIS_NODES,
                            moved_response=False,
                            decode_responses=True,
                            read_from_replicas=True)

    redis.set(key, value)

    # if we want to get multiple keys from different slot we should use another redis key
    # redis.mget_nonatomic(["aa", "zz"]
