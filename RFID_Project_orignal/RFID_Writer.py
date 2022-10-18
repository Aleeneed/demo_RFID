import pandas as pd
import os 
import RFID 

Name=[] #Save Name
Name_list={'Name':Name}
data=[] #Save Data
Name_append=input('Name :') 
Name.append(Name_append)   
Name_df=pd.DataFrame(Name_list)
data_list={'Card ID':data}
data.append(RFID.rfid())
data_df=pd.DataFrame(data_list)
rfid_df=pd.concat([Name_df,data_df],axis=1)
def create_RFID():
    try :
        os.makedirs('./data')
    except FileExistsError:
        read_csv=pd.read_csv('./data/Write.csv')
        read_csv_df=pd.DataFrame(read_csv)
        read_csv_df=pd.concat([read_csv_df,rfid_df],axis=0)
        read_csv_df=read_csv_df.drop_duplicates()
        read_csv_df=read_csv_df.reset_index(drop=True)
        read_csv_df.to_csv('./data/Write.csv',index=False,encoding='utf_8_sig')
    else :
        rfid_df.to_csv('./data/Write.csv',index=False,encoding='utf_8_sig')
        print('output')
create_RFID()