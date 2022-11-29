import mysql.connector
import pandas as pd
import time
import RFID_Read
import os
connection=mysql.connector.connect(host='127.0.0.1',
                                        port='3306',
                                        user='root',
                                        password='password') #user password
cursor= connection.cursor()
def return_exist():
    if os.path.exists('C:/ProgramData/MySQL/MySQL Server 8.0/Data/rfid_databases'):
        cursor.execute('USE `Rfid_databases`')       
        return 0
    else:    
        cursor.execute('CREATE DATABASE `Rfid_databases`;')
        cursor.execute('USE `Rfid_databases`')
        cursor.execute('CREATE TABLE `employee` (`emp_id` INT PRIMARY KEY, `name` VARCHAR(20),`card_id` VARCHAR(30),`sex` VARCHAR(1) , `shift` VARCHAR(10));')
        cursor.execute('CREATE TABLE `punch_record` (`emp_id` INT PRIMARY KEY , `name` VARCHAR(20),`shift` VARCHAR(10), `punch_time` TIMESTAMP,FOREIGN KEY(`emp_id`) REFERENCES `employee`(`emp_id`) ON DELETE CASCADE);')        
        cursor.close()  
        connection.close()
        return 1 
if __name__ == '__main__':
    return_exist()

