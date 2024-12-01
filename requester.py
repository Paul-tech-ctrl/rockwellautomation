import requests

class request():
    def __init__(self):
        pass
        
    def headers(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }
        
        return headers
    
    def make_request(self, url):
        try:
            req = requests.get(url, headers=self.headers())
        
            if req.status_code == 200:
                return req.content
            else:
                return None
        except Exception as e:
            return None