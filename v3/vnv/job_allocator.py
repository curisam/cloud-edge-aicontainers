import os
import yaml
import re
from device_info import set_model4infer

from collections import OrderedDict
from redis_connector import redis_connector
rcon = redis_connector()


class job_allocator():
    def __init__(self):
        pass
    
    def set_job(self):
        #get_device_ministat()
        #get_cluster_list()

        hostname = socket.gethostname()
    
        if mode == 'getinfo':
            pass
        else:
            rcon.set_data(f'vnv:edge:{mode}:job:{hostname}:start_frame', 0)
            rcon.set_data(f'vnv:edge:{mode}:job:{hostname}:end_frame', 100)
        