import socket
import json
import sys
import time
import signal
from Coins import Coins

DEFAULT_REFRESH_TIME = 30   # Tiempo de actualizacion de datos por defecto en segundos
CONFIG_FILE_PATH = "config.txt" # Archivo de configuracion

# Se define el handler de la señal SIGINT
def sigint_handler(sig, frame): 
    print(f'Se presiono CTRL+C. Saliendo del programa...')
    exit(0)  

class Main:
    def __init__(self):
        pass

    def main(self):
        signal.signal(signal.SIGINT, sigint_handler)

        port = 10000
        try:
            port = int(sys.argv[1])
        except:
            print("Puerto incorrecto")
            exit(1)

        # Se crea el socket UDP
        serverAddressPort   = ("localhost", port)
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        print(f"Cliente inicializado. Enviando datos...")
        
        while True:
            try:
                with open(CONFIG_FILE_PATH, "r") as config_file:
                    quotes_path = config_file.readline().strip("path=\n")
                    refresh_time = DEFAULT_REFRESH_TIME
                    refresh_time_str = config_file.readline().strip("refresh_time=\n")                    
                    if refresh_time_str.isdecimal():
                        refresh_time = int(refresh_time_str)
                    else:
                        print(f"Tiempo de actualizacion incorrecto. Se usara el valor por defecto: {DEFAULT_REFRESH_TIME} segundos.")

            except Exception as e:
                print("Error al leer el archivo de configuracion: " + str(e))
                exit(1)                

            coins = Coins(quotes_path)         

            l_loins = coins.parse_data()
            jsonValues = json.dumps(l_loins)
            tx_data = bytearray(jsonValues, 'utf-8')
                        
            UDPClientSocket.sendto(tx_data, serverAddressPort)  # Se envian los datos al servidor usando el socket UDP creado
            time.sleep(refresh_time)    # Se espera el tiempo de actualizacion de datos

program = Main()
program.main()