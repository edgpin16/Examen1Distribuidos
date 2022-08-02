from xmlrpc.server import SimpleXMLRPCServer;

def garbageCollector(*args):
	res = []
	for arg in args:
		try:
			lengthValue = len(arg)
		except TypeError:
			lengthValue = None
		res.append((lengthValue, arg))
	return res

def domain():
	try:
		print("SERVER STARTED")
		print("LOCALHOST")
		print('PORT: 8000')
		return SimpleXMLRPCServer(('localhost', 8000))
	except:
		print('something happened :( in DOMAIN SERVER FUNCTION - PREGUNTA 1')

def main():
	try:
		server = domain()
		server.register_function(garbageCollector)	
		server.serve_forever()
	except:
		print("something happened :( in MAIN SERVER FUNCTION - PREGUNTA 1")

if __name__ == '__main__':  
    main()
