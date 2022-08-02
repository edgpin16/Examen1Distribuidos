import random
from xmlrpc.server import SimpleXMLRPCServer
import json

fakeDataProducts = [
    { "ID" : 1, "title": "Brown eggs", "type": "dairy", "description": "Raw organic brown eggs in a basket", "filename": "0.jpg", "height": 600, "width": 400, "price": 28.1, "rating": 4}, 

    { "ID" : 2, "title": "Sweet fresh stawberry", "type": "fruit", "description": "Sweet fresh stawberry on the wooden table", "filename": "1.jpg", "height": 450, "width": 299, "price": 29.45, "rating": 4}, 

    { "ID" : 3, "title": "Asparagus", "type": "vegetable", "description": "Asparagus with ham on the wooden table", "filename": "2.jpg", "height": 450, "width": 299, "price": 18.95, "rating": 3}, 

    { "ID" : 4, "title": "Green smoothie", "type": "dairy", "description": "Glass of green smoothie with quail egg's yolk, served with cocktail tube, green apple and baby spinach leaves over tin surface.", "filename": "3.jpg", "height": 600, "width": 399, "price": 17.68, "rating": 4}, 
    
    { "ID" : 5, "title": "Raw legums", "type": "vegetable", "description": "Raw legums on the wooden table", "filename": "4.jpg", "height": 450, "width": 299, "price": 17.11, "rating": 2}
]

class RPC:
    methods = ['isValidOptions', 'doOperation']
    operators = {
        '1':'1',
        '2':'2',
        '3':'3',
    }
    
    def __init__(self, URL, port):
        self.server = SimpleXMLRPCServer((URL, port), allow_none=True)
        
        for method in self.methods:
            self.server.register_function(getattr(self, method))
    
    def isValidOptions(self, oper):
        return oper in self.operators
    
    def doOperation(self, oper):
        if oper == self.operators['1']:
            return json.dumps(fakeDataProducts, indent=4, sort_keys=True)
        elif oper == self.operators['2']:
            if(not(bool(fakeDataProducts)) ):
                return []
            return json.dumps(random.choice(fakeDataProducts), indent=4, sort_keys=True)
        elif oper == self.operators['3']:
            return fakeDataProducts.clear()
        else:
            return 'Operación no válida'

    def run(self):
        self.server.serve_forever()
        print("SERVER STARTED")
    
if __name__ == '__main__':
    try:
        rpc = RPC('localhost', 20064)
        print('INITIALIZING SERVER...')
        rpc.run()
    except:
        print('something happened :( in MAIN SERVER FUNCTION - Pregunta 2')