import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
#import RFID_Read 

window=tk.Tk()
window.title('打卡')
window.geometry('380x400')
window.resizable(False, False)
def UI():
    #功能
    menu = tk.Menu(window)
    window.config(menu=menu)
    menu2 = tk.Menu(menu,tearoff=0)
    menu2.add_command(label='新增卡片',command=append_card)
    menu2.add_command(label='輸出')
    menu.add_cascade(label='功能',menu=menu2)



def upload_data():
    print('done')
def append_card():
    newWindow = tk.Toplevel(window)
    newWindow.title('Append Card')
    newWindow.geometry('380x400')
    newWindow.resizable(False, False)
    label = tk.Label(newWindow, text = "請輸入名子: ")
    chack_button = tk.Button(newWindow, text = "確認")

    var = tk.StringVar()

    label.grid(row=1, column=0)
    entry1 = tk.Entry(newWindow)
    entry1.grid(row=1, column=1)
    chack_button.grid(row=3, column=1)  
    #messagebox.asktrycancel('Hi','hahahaha')
    #messagebox.showinfo('Test','hahahaha')
#def chack_name():

if __name__=="__main__":
    UI()


window.mainloop()
