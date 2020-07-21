# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:40:16 2020

@author: Suraj
"""
#C:\applications
import pyodbc
import pandas as pd
from dotenv import dotenv

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1Q011U6\MSSQLSERVER02;'
                      'Database=practice;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

df = pd.read_excel(r'C:\Users\Suraj\Desktop\Information.xlsx')

#df =df.rename(columns={'person_id':'PersonID','firstname':'FirstName','lastname':'LastName','salary':'Salary','city':'City'},inplace=True)
df.columns= ['PersonID','FirstName','LastName','Salary','City']

data_type = { 'PersonID':int,'FirstName':object,'LastName':object,'Salary':float,'City':object}

df= df.astype(data_type)
for index,col in df.iterrows():
    cursor.execute("INSERT INTO practice.dbo.information values (?,?,?,?,?)", col['PersonID'], col['FirstName'],col['LastName'],col['Salary'],col['City']) 
 
conn.commit()            
  
sql_query = pd.read_sql_query('SELECT * FROM practice.dbo.information',conn)
conn.close()   

if __name__ == '__main__':
    
