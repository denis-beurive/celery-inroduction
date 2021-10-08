from typing import Optional
import os
import sys
from celery import Celery


redis_ip = os.getenv('REDIS_IP')
if redis_ip is None:
    print('ERROR: environment variable "REDIS_IP" is not SET!')
    sys.exit(1)
APP1 = Celery('tasks', broker='redis://{}'.format(redis_ip))
APP2 = Celery('tasks', broker='redis://{}'.format(redis_ip))


@APP1.task
def add(x: int, y: int) -> int:
    return x + y


@APP2.task
def subtract(x: int, y: int) -> int:
    return x - y
