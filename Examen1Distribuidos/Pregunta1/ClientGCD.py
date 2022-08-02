from xmlrpc.client import ServerProxy
import gc
import pprint

class Model:
    def __init__(self, object):
        print('Not garbage collector:')
        print(object)
        self.object = object
        self.next = None

    def set_next(self, next):
        print('Nodes links {}.next = {}'.format(self, next))
        self.next = next

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__, self.object)

def domain():
    try:
        print("CLIENT CONNECTED")
        print("LOCALHOST")
        print('PORT: 8000')
        return ServerProxy('http://localhost:8000')
    except: 
        print("something happened :( in DOMAIN CLIENT FUNCTION - PREGUNTA 1")

def main():
    try:
        connection = domain()
        objectExample = {"name":"Juan", "age":30, "possessions": ["car","house","bike"]}
        data = Model(connection.garbageCollector(objectExample))
        print('Garbage collector:')
        for r in gc.get_referents(data):
            pprint.pprint(r)
    except:
        print("something happened :( in MAIN CLIENT FUNCTION - Pregunta 1")

if __name__ == '__main__':
    main()