### API TEST
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


temp = 20
humidity = 40
for i in range(20):
    push_data("0", "temp", temp)
    push_data("0", "humidity", humidity)
    temp += 1
    humidity += 1