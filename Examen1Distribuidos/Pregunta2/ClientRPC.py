from xmlrpc.client import ServerProxy
import msvcrt

try: 
    connection = ServerProxy('http://localhost:20064', allow_none=True)
except:
    print('something happened :( in try connection in RPC SERVER - Pregunta 2')

while True:
    print('')
    print('Seleccione una opción')
    print('---------------------------------')
    print("|Presione (1) para ver todos los productos         |")
    print("|Presione (2) para ver un producto aleatorio       |")
    print("|Presione (3) para eliminar todos los productos    |")
    print('---------------------------------')

    option = input('Ingresa el operador: ')

    try:
        if connection.isValidOptions(option):
            print(connection.doOperation(option))
        else:
            print('Operación no válida')
    except:
        print('something happened :( in MAIN SERVER FUNCTION - Pregunta 2')
    
    print('')
    print("Presione 'x' para salir...")
    print("Presione cualquier tecla para continuar...")
    
    key = msvcrt.getwch()
    if key == 'x':
        exit()