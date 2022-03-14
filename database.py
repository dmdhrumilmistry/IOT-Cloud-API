import json
import os


class DB:
    def __init__(self, path:str=None, indent:int=4) -> None:
        self.__indent = indent
        self.path = path if path else os.path.join(os.getcwd(), 'mydb.icdb')
        if not self.path.endswith('.icdb'):
            self.path += '.icdb'

        if not os.path.exists(self.path):
            self.data = dict()
            self.write_data()
        

    def write_data(self):
        with open(self.path, 'w') as f:
            f.write(json.dumps(self.data, indent=self.__indent))


    def read_data(self) -> dict:
        with open(self.path, 'r') as f:
            data = json.loads(f.read())
        
        return data
