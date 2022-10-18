import pandas as pd
import os 
import RFID 

Name=[] #Save Name
Name_list={'Name':Name}
data=[] #Save Data
Name_append=input('Name :') #輸入Name
Name.append(Name_append)   #新增
Name_df=pd.DataFrame(Name_list) 
data_list={'Card ID':data} 
data.append(RFID.rfid()) #新增RFID Data
data_df=pd.DataFrame(data_list)
rfid_df=pd.concat([Name_df,data_df],axis=1) #把兩個列表結合
def create_RFID():
    try : #看有沒有此路徑,如果沒有建立一個資料夾
        os.makedirs('./data')
    except FileExistsError: #如果有此路徑,跑到這
        read_csv=pd.read_csv('./data/Write.csv') #讀取Data
        read_csv_df=pd.DataFrame(read_csv) #建立DataFrame
        read_csv_df=pd.concat([read_csv_df,rfid_df],axis=0) 
        read_csv_df=read_csv_df.drop_duplicates() #把重複的刪掉
        read_csv_df=read_csv_df.reset_index(drop=True) #重置index
        read_csv_df.to_csv('./data/Write.csv',index=False,encoding='utf_8_sig') #輸出CSV
    else : #如果沒有此路徑 跑到這
        rfid_df.to_csv('./data/Write.csv',index=False,encoding='utf_8_sig')
        print('output')
create_RFID()
