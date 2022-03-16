# IOT-Cloud-API

Custom Cloud RESTful API written in Python using Flask Framework to save data from the sensors on the server in json format and fetch it later for analysis.

## Installation
- Clone/Download Project
  ```bash
  git clone https://github.com/dmdhrumilmistry/IOT-Cloud-API.git
  ```
  
- Install requirements
  ```bash
  pip install -r requirements.txt
  ```
  > Note : use `pip3` instead of `pip` on Ubuntu Distro 
  
- Change Auth key in config.py module
  ```python
  # AUTH_KEY = "Test_Key"
  AUTH_KEY = "S0m3T#1n9_5tr0ng&53cR3T"
  ```
  > Note: `AUTH_KEY` will be required to authenticate data publisher and fetcher on the server

- Run the test server using
  ```bash
  flask run
  ```
 
## Endpoints
|endpoint|description|
|:------:|:----------|
|/|returns Home Page html code|
|/AUTH_KEY/push_data|authenticates user, saves pushed data on the server and returns the status in json format|
|/AUTH_KEY/get_data|authenticates user and returns the data on the server in json format|

## Example Test Programs
- Requirements:
  - requests

- Push Data to server using python for testing
  ```python
  import requests
  key = "Test_Key"

  url = f"http://127.0.0.1:5000/{key}/push_data"
  command = "push_data"
  data = {
      'node' : "1",
      'sensor' : "mq135",
      'sen_data' : '120',
  }
  response = requests.post(url=url, json=data)
  print(response.content.decode('utf-8'))
  ```
- Get data from the server using python for testing
  ```python
  import requests
  key = "Test_Key"
  
  url = f"http://127.0.0.1:5000/{key}/get_data"
  response = requests.post(url={url}, json=data)
  print(response.content.decode('utf-8'))
  ```