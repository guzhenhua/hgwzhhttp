import requests

class BaseApi():
    def send_api(self,res:dict):
        return requests.request(**res)