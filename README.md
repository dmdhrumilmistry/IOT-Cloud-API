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
 
