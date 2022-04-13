### API TEST
from sys import argv
from time import sleep

import requests
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
    temp = 20
    humidity = 40
    
    mode = 0 # 0 iterative, 1 continous
    if argv[-1] == '1':
        mode = 1

    print("Runnning in ", end='')
    if mode == 0:
        print("Iterative Mode.")
        for i in range(20):
            push_data("0", "temp", temp)
            push_data("0", "humidity", humidity)
            temp += 1
            humidity += 1
    else:
        print("Continous Mode.")
        print("Ctrl+C to stop")
        while True:
            push_data("0", "temp", temp)
            push_data("0", "humidity", humidity)
            temp += 1
            humidity += 1
            sleep(1)
