from requester import request
from bs4 import BeautifulSoup
import json
import uuid

class extra():
    def __init__(self):
        self.req = request()
    
    def get_product_urls(self, url):
        try:
            content = self.req.make_request(url)
            soup = BeautifulSoup(content, 'html.parser')
            urls = []
            
            tags = soup.select('[data-link-text="product details"]')
            if tags:
                for tag in tags:
                    urls.append({
                        'id': str(uuid.uuid4()),
                        'url': 'https://www.rockwellautomation.com' + tag.get('href')
                    })
                    
            with open('urls.json', 'w') as f:
                json.dump(urls, f, indent=4)
                
            return urls
        except Exception as e:
            return []