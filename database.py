'''
module: database
description: contains DB class to store data locally in form of json
'''

import json
import os


class DB:
    '''
    DB stores data locally in form of json in a filea
    '''
    def __init__(self, path:str=None, indent:int=4) -> None:
        '''
        description:
            Creates a file to store data locally on the server

        params:
            path (str): path of the file
            indent (int): json data indentendation
        
        returns:
            None
        '''
        self.__indent = indent
        self.path = path if path else os.path.join(os.getcwd(), 'mydb.icdb')
        if not self.path.endswith('.icdb'):
            self.path += '.icdb'

        if not os.path.exists(self.path):
            self.data = dict()
            self.write_data()
        else:
            self.data:dict = self.read_data()


    def write_data(self):
        '''
        description:
            writes obj data to the file

        params:
            None

        returns:
            None 
        '''
        with open(self.path, 'w') as f:
            f.write(json.dumps(self.data, indent=self.__indent))


    def read_data(self) -> dict:
        '''
        description:
            reads saved data from the file in dictionary format
            if data is invalid, then it raises JsonDecodeError

        params:
            None

        returns:
            None
        '''
        with open(self.path, 'r') as f:
            data = json.loads(f.read())
        
        return data
        