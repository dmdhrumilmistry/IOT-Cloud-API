### API TEST
from sys import argv
from time import sleep

import requests
import random
key = "Test_Key"

url = f"http://127.0.0.1:8000/{key}"
command = "push_data"

def push_data(node_name, sensor_name, sensor_value):
    data = {
        'node' : node_name,
        'sensor' : sensor_name,
        'sen_data' : sensor_value,
    }

    response = requests.post(url=f"{url}/{command}", json=data)
    print(response.content.decode('utf-8'))


if __name__ == "__main__":
    temp = random.randint(0, 40)
    humidity = random.randint(0,100)
    co2 = random.randint(200,400)

    mode = 0 # 0 iterative, 1 continous
    if argv[-1] == '1':
        mode = 1

    print("Runnning in ", end='')
    if mode == 0:
        print("Iterative Mode.")
        for i in range(20):
            push_data("0", "temp", temp)
            push_data("0", "humidity", humidity)
            push_data("0", "CO2", co2)
            temp += 1
            humidity += 1
            co2 += 1
    else:
        print("Continous Mode.")
        print("Ctrl+C to stop")
        while True:
            push_data("0", "temp", temp)
            push_data("0", "humidity", humidity)
            push_data("0", "CO2", co2)
            temp += 1
            humidity += 1
            co2 += 2
            sleep(1)
