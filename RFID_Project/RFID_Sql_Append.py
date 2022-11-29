import mysql.connector
import os
import RFID_Read as RF
import RFID_Sql_New as New
from threading import Timer
connection=mysql.connector.connect(host='127.0.0.1',
                                        port='3306',
                                        user='root',
                                        password='root',
                                        database='Rfid_databases',
                                        buffered=True)
cursor= connection.cursor()

def check():
    if New.return_exist()==0:
        if RF.rfid() == cursor.execute('SELECT 1 FROM `employee` WHERE `card_id`') :
                
            print('ex')
            #cursor.reset()
            return 0
        else:      
            print('265')
            return 1



if __name__=='__main__':
    while True:
        check()
