import serial

def rfid(): #read RFID Data
    ser = serial.Serial()
    ser.baudrate = 9600    
    ser.port = 'com10' #connect port
    ser.open() #open serial
    RFID_Data=ser.readline() 
    RFID_Data = RFID_Data.decode()  
    RFID_Data = RFID_Data.strip() 
    return(RFID_Data)

if __name__ =="__main__":
    rfid()
