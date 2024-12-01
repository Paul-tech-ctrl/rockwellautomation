import json
from parser import product
from xlxsparser import parse
from extra_functions import extra

if __name__ == '__main__':
    # url = 'https://www.rockwellautomation.com/en-ca/products/hardware/allen-bradley/vfd/low-voltage-ac-drive/compact-drive/25a-powerflex-523.html'
    # with open('urls.json', 'r', encoding='utf-8') as json_file:
    #     urls = json.load(json_file)
    
    # items = []
    # for i in urls:
    #     _product = {}
    #     _product['item id'] = i['id']
    #     _product.update(product(i['url']).get_item())
    #     items.append(_product)
    
    
    
    # #Convert item to JSON string
    # item_json = json.dumps(items)
    
    # # Write JSON string to a file
    # with open('item.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(items, json_file, ensure_ascii=False)
    
    with open('item.json', 'r', encoding='utf-8') as json_file:
        item = json.load(json_file)
        
    xclprsr = parse(item)
    xclprsr.process() 
    
    # list_url = 'https://www.rockwellautomation.com/en-ca/products/hardware/allen-bradley/vfd/low-voltage-ac-drive/compact-drive.html'
    # xtra = extra()
    # xtra.get_product_urls(list_url)
    
    # print(item_json)