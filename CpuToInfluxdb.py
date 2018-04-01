import psutil
import os
from influxdb import InfluxDBClient
import time


"""
获取CPU的状态,存储到influxdb
"""

p1 = psutil.Process(os.getpid())

while True:
    a = psutil.virtual_memory().percent   # cpu占有率

    b = psutil.cpu_percent(interval=1.0)   # cpu占有率

    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "fields": {
                "cpu": b,
                "mem": a
            }
        }
    ]

    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'xxyyxx')
    client.create_database('xxyyxx', if_not_exists=False)
    client.write_points(json_body)

    time.sleep(2)

