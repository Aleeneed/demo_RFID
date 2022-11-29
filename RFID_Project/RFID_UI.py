import tkinter as tk
from tkinter import messagebox
import serial.tools.list_ports
import RFID_Sql_Append as append
import threading
from threading import Timer
    
class sql_append:#建立class sql
    def __init__(self,name,sex,shift):
        self.name=name
        self.sex=sex
        self.shift=shift
def UI():
    plist = list(serial.tools.list_ports.comports())
    window=tk.Tk()
    window.title('打卡')
    window.geometry('380x400')
    window.resizable(False, False)
    #功能
    menu = tk.Menu(window)  
    window.config(menu=menu)
    menu2 = tk.Menu(menu,tearoff=0)
    menu2.add_command(label='輸出')
    menu.add_cascade(label='功能',menu=menu2)
    if len(plist) <= 0:
        if messagebox.showwarning(title='系統通知',message='請插入RFID裝置'):
            window.destroy() 
    window.mainloop()

def upload_data():
    print('upload ok')
def append_card():
    newwindow=tk.Tk()
    newwindow.title('Append Card')
    newwindow.geometry('380x400')
    newwindow.resizable(False, False)
    name_label = tk.Label(newwindow, text = "請輸入名子 :  ")
    sex_label =tk.Label(newwindow,text='性別 :  ')
    shift_label=tk.Label(newwindow,text='班別 :  ')
    check_button = tk.Button(newwindow, text = "確認")
    cancel_button = tk.Button(newwindow, text = "取消")
    #var = tk.StringVar()
    name_label.grid(row=1, column=0)
    name_entry1 = tk.Entry(newwindow)
    name_entry1.grid(row=1, column=1)
    sex_label.grid(row=2,column=0)
    sex_entry=tk.Entry(newwindow)
    sex_entry.grid(row=2,column=1)
    shift_label.grid(row=3,column=0)
    shift_entry=tk.Entry(newwindow)
    shift_entry.grid(row=3,column=1)
    check_button.grid(row=4, column=0)
    newwindow.mainloop() 
UI_threading=threading.Thread(target=UI)
UI_threading.setDaemon(True)
UI_threading.start()
if __name__=="__main__":
    def func():
        if append.check()==1:
            append_card()
        else:
            print('0')
    while True:
        func()
