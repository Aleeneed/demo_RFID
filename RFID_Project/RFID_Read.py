import serial
import time

ser = serial.Serial()
ser.port = 'COM10' 
ser.open()     
def rfid():
    RFID_Data=ser.readline() 
    RFID_Data = RFID_Data.decode()  
    RFID_Data = RFID_Data.strip()
    return(RFID_Data)

if __name__ =="__main__":
    rfid()
