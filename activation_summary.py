#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 15:15:25 2022

@author: parksangbeomm
"""

import os
import shutil
import json
import csv
import pandas as pd 
import nothing



place_list = {'01_타타대우상용차' : '2e0e492a-082e-4142-aafc-46fa6624234b', 
              '02_푸드뱅크 사무실' : 'e34ce08f-23a9-4fb9-8e93-635bb12fc4e3', 
              '03_D동 1층 GM대우(cd구역EPS)' : '263be482-9b18-4e0c-bb15-36fe04e880e2', 
              '04_가동 리바트' : 'f6164ad0-7068-4630-b14a-409eb5806521',
              '05_LG생활건강 3층(Cd구역EPS)' : 'ee1155d3-e323-436d-a6e2-6792f1770995', 
              '06_별관2층 국양로지텍' : '54b6b91a-4319-46f2-b60c-a1646958b32d', 
              '07_A동 쌍용C&B' : '387fb88e-68e0-4710-8cf6-8e9d6c476561', 
              '08_A동 금호타이어' : 'b66718bf-ead8-49ea-9c71-12514ea0c6b9',
              '09_hanjin02 (라동)' : 'ba9a823f-8749-4c53-954b-461dd1343007', 
              '10_D동 5층 GM대우(cd구역 EPS)' : 'f9fd062c-90d0-45e0-89b4-48277e653b24', 
              '11_D동 3층 SD바이오센서(a사무실)' : 'fd0ceaf0-844b-47e4-99eb-706275a0f21e', 
              '12_메인동 방재실' : 'bc3d1a03-1534-44db-92e1-5c78735e77c4',
              '13_hanjin03 (나동)' : 'f9ea9dcc-5fb2-4ea1-b511-3532d4ec96f5', 
              '14_C동 2층 함소아(c사무실)' : '28efe0cb-b0ec-4e2a-82c0-008d67788146', 
              '15_C동 5층 SD바이오센스(a사무실)' : 'fd0ceaf0-844b-47e4-99eb-706275a0f21e'}
level = {
    "00_00" : "경",
    "00_30" : "경",
    "01_00" : "경",
    "01_30" : "경",
    "02_00" : "경",
    "02_30" : "경",
    "03_00" : "경",
    "03_30" : "경",
    "04_00" : "경",
    "04_30" : "경",
    "05_00" : "경",
    "05_30" : "경",
    "06_00" : "경",
    "06_30" : "경",
    "07_00" : "경",
    "07_30" : "경",
    "08_00" : "경",
    "08_30" : "경",
    "09_00" : "중",
    "09_30" : "중",
    "10_00" : "최대",
    "10_30" : "최대",
    "11_00" : "최대",
    "11_30" : "최대",
    "12_00" : "중",
    "12_30" : "중",
    "13_00" : "중",
    "13_30" : "중",
    "14_00" : "중",
    "14_30" : "중",
    "15_00" : "중",
    "15_30" : "중",
    "16_00" : "중",
    "16_30" : "중",
    "17_00" : "최대",
    "17_30" : "최대",
    "18_00" : "최대",
    "18_30" : "최대",
    "19_00" : "최대",
    "19_30" : "최대",
    "20_00" : "중",
    "20_30" : "중",
    "21_00" : "중",
    "21_30" : "중",
    "22_00" : "최대",
    "22_30" : "최대",
    "23_00" : "경",
    "23_30" : "경"}
count = {
    '경' : 0,
    '중' : 0,
    '최대' : 0
    }

#read directory name from this path 
path_dir = './CSV/'

while(1):
    for key, value in place_list.items():
        print(key)
    
    place = input("Which place do you want ? ex) 03_D동 1층 GM대우(cd구역EPS) >> ")
    date = input("Which date do you want to export? ex) 28-12-2021 >> ")
    
    print("Place :" , place)
    print("Date :" , date)
    with open('./summary/'+ place + '_' + date + '_summary' + '.csv', 'a', newline = '') as output_file :
        f = csv.writer(output_file)
        f.writerow(place)
        f.writerow(["address", "조명 Type", "경부하", "중간부하", "최대부하"])
    
    datas = list()
    tables = list()
    
    table_excel = pd.read_excel('./nodeTable_2022_0103.xlsx', sheet_name = 'grid_prod_nodeTable_2022_0103',
                                usecols=['address', 'name', 'maxWatt', 'groupId', 'hubId'])
    table_excel = table_excel.sort_values(by='hubId')
    #print(table_excel)
    input_file = pd.read_csv(path_dir+ date +'/'+ place +'_'+ date +'.csv').sort_values(by=['address', 'time'], ascending=[True, True])
    print(input_file)
    for i in range(1,len(input_file)):
        if(i<10):
            print(input_file.iloc[i])
            

    ctn = input("Continue? Type 'y' to continue or type anything >> ")
    if ctn != 'y':
        print("Done!")
        break
        
        
        
        
        
        
        
        