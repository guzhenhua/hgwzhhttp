from api.base_api import BaseApi
import requests

class WeWork(BaseApi):
    def get_token(self):
        data={
            "method":"get",
            "params":{"postId":1},
            "url":"http://jsonplaceholder.typicode.com/comments"
        }
        r=self.send_api(data)
        print(r.json())