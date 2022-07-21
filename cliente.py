from random import choice
from time import sleep, time
from urllib.error import HTTPError
import requests as request

class Sensor:
    __id_device : str
    __temperature: int
    __timestamp: int

    def __init__(self,id_device:str):
        self.__id_device = id_device
        self.__temperature = 0
        self.__timestamp = 0
    
    @property
    def id_device(self):
        return self.__id_device
    
    @id_device.setter
    def id_device(self,idDevice):
        self.id_device = idDevice

    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self,temp):
        self.__temperature=temp
    
    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self,timestmp):
        self.__timestamp = timestmp
    
    def payload(self):
        return {
            "id_device":self.__id_device,
            "temperature":self.__temperature,
            "timestamp":self.__timestamp
            }

class Conexion:
    def __init__(self,URL):
        self.url=URL

    def send(self,payload: dict):
        try:
            response = request.post(self.url,json=payload)
            print(f'INFO {response.status_code}: payload {payload}')
            attempt = 0
            while response.status_code >=400 and attempt < 5:                
                response = request.post(self.url,json=payload)
                print(f'INFO {response.status_code}: atteempt {attempt+1}')
                attempt+=1
                sleep(2)                
            
        
        except HTTPError as http_err:
            print(f'ERROR HTTP {http_err}')
        except Exception as e:
            print(f'ERROR {e}')
        
if __name__=='__main__':
    #Default conexion: localhots in port 8000
    HOST="localhost"# input your IP
    PORT=8000
    
    sensor_one = Sensor("ESP-32-1500")    
    url=f'http://{HOST}:{PORT}/api/v1.0/sensors'    
    conn = Conexion(url)
    rand_tmp = [temp for temp in range(10,100+1)]
    
    while 1:
        try:
            sensor_one.temperature = choice(rand_tmp)
            sensor_one.timestamp =  int(time()*1000)
            #print(sensor_one.payload())
            conn.send(sensor_one.payload())
            sleep(2)
        except KeyboardInterrupt:
            input("\nPress any key then into to exit: ")
            sleep(2)
            break
        except Exception as e:
            print(f'INFO: Exit for exception, {e}')
            sleep(2)
            break