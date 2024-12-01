import json
from requester import request
from bs4 import BeautifulSoup

class product():
    def __init__(self, url):
        self.url = url
        self.req = request()
        
    def get_item(self):
        try:
            content = self.req.make_request(self.url)
            soup = BeautifulSoup(content, 'html.parser')
            
            item = {}
            item['url'] = self.url
            item['title'] = self.get_title(soup)
            item['images'] = self.get_images(soup)
            item['description'] = self.get_description(soup)
            item['overview'] = self.get_overview(soup)
            item['productselection'] = self.get_product_selection(soup)
            item['documents'] = self.get_documents(soup)
            
            return item
        except Exception as e:
            return None
        
    def get_title(self, soup):
        try:
            tag = soup.select_one('h1')
            if tag:
                return tag.text.strip()
            return None
        except Exception as e:
            return None
        
    def get_images(self, soup):
        try:
            images = []
            tag = soup.select('.multimedia-grid__active-media div div picture source')
            if tag:
                for item in tag:
                    images.append('https://www.rockwellautomation.com' + item.get('srcset'))
            return images
        except Exception as e:
            return []
    
    def get_description(self, soup):
        try:
            tag = soup.select_one('.column-control__container.grid.collapse-cols-mobile.no-nested-padding')
            if tag:
                return tag.get_text().strip()
            return None
        except Exception as e:
            return None    
        
    def get_overview(self, soup):
        try:
            overview = []
            tag = soup.select('[data-rte-class="rte-temp"]')
            if tag:
                for item in tag:
                    overview.append(item.get_text().strip())
            return overview
        except Exception as e:
            return []
        
    def get_product_selection(self, soup):
        try:
            item = {}
            products = []
            page = 1
            while True:
                base_url = self.url.split('.html')[0]
                url = f"{base_url}/jcr:content/root/main-par/generic_container_3/GenericContainerParsys/column_control/Col1/product_variant_grid.productVariants.{page}.100.json"
                content = self.req.make_request(url)
                _json = json.loads(content)
                products += _json['products']
                pages = _json['numberOfPages']
                if page >= pages or page == 10:
                    break
                page += 1
            for itm in products:
                item[itm['catalogNumber']] = itm['names'][0]['value']
            return item
        except Exception as e:
            return None
        
    def get_documents(self, soup):
        try:
            documents = []
            tag = soup.select('.table__container table tbody tr')
            if tag:
                for item in tag:
                    links_val = []
                    temp = {}
                    resource = item.select_one('[data-label="Resource"]').get_text().strip()
                    pub_num = item.select_one('[data-label="Publication Number"]').get_text().strip()
                    links_tag = item.select_one('[data-label="Language"]')
                    if links_tag:
                        links = links_tag.select('option')
                        links_val = {}
                        for link in links:
                            lang = link.get_text().strip()
                            val = link.get('value')
                            if val == 'none':
                                continue
                            links_val[lang] = val
                    temp["resource"] = resource
                    temp["publicationnumber"] = pub_num
                    temp["links"] = links_val
                    documents.append(temp)
            return documents
        except Exception as e:
            return []