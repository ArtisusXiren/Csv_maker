#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os
def process_csv(products_data, upload_file, path_decided):
    column_list=[]
    Title=[]
    aligned_repeated_sizes=[]
    dict_product={}
    Handle=[]
    V_Price=[]
    title=[]
    for columns in products_data.columns:
        column_list.append(columns)
    Title=upload_file['Product Name'].tolist()
    Price=upload_file['Price'].tolist()
    columns_for_new= column_list
    dataframe=pd.DataFrame(columns=columns_for_new)
    Size_chart=[columns for columns in upload_file.columns[:-1] if columns!='Product Name' and columns!='Price']
    for i,rows in upload_file.iterrows():
        for columns in Size_chart:
            repetetions=rows[columns]
            if pd.notna(repetetions):
                repetetions=int(repetetions)
                aligned_repeated_sizes.extend([columns]*repetetions)

    for values,(index,rows) in zip(Title,upload_file.iterrows()):
        for columns in Size_chart: 
            repetetions=rows[columns]
            if pd.notna(repetetions):
                repetetions=int(repetetions)
                Handle.extend([values]*repetetions)

    for values,(index,rows) in zip(Price,upload_file.iterrows()):
        for columns in Size_chart: 
            repetetions=rows[columns]
            if pd.notna(repetetions):
                repetetions=int(repetetions)
                V_Price.extend([values]*repetetions)

    for values in Handle:
        if values in title:
            title.append(" ")
        else:
            title.append(values)        

    dataframe['Handle']=Handle
    dataframe['Variant Price']=V_Price
    dataframe['Option1 Value'] = aligned_repeated_sizes 
    dataframe['Title']=title
    id_number=0
    temp_id=0
    new_file=os.path.join(path_decided,f"output_file")
    if not os.path.exists(f"{new_file}.csv"):
        dataframe.to_csv(f"{new_file}.csv",index=False)
    else:
        temp_id +=1
        while os.path.exists(f"{new_file}_{temp_id}.csv"):
            temp_id +=1
        id_number =temp_id
        file_to_store=f"{new_file}_{id_number}.csv"
        dataframe.to_csv(file_to_store, index=False)
    



# In[ ]:




