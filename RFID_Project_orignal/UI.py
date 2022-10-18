import tkinter as tk
#import RFID_Writer


window=tk.Tk()
window.title('RFID Read and Writer')
window.geometry('380x400')
window.resizable(False, False)

#功能
menu = tk.Menu(window)
window.config(menu=menu)
menu2 = tk.Menu(menu,tearoff=0)
menu2.add_command(label='開啟打卡模式')
menu2.add_command(label='開啟卡片資料庫')
menu2.add_command(label='新增卡片')
menu.add_cascade(label='功能',menu=menu2)

#
label1=tk.Label(text='u')
label1.grid(row=4, column=1)
var = tk.StringVar()
label=tk.Label(text='請輸入名子: ')
label.grid(row=1, column=0)
entry1 = tk.Entry()
entry1.grid(row=1, column=1)
chack_button = tk.Button(width=20, text="確認")
chack_button.grid(row=3, column=1)


#def chack_Rfid():
#    if RFID_Writer.Name==entry1:

#window.iconbitmap('./data.ico')
window.mainloop()