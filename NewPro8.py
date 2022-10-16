import os
import pandas as pd
import numpy as np
from pandas.core.tools.timedeltas import to_timedelta
from IPython.display import display
import mysql.connector

#create varibles to store file path 
folder = 'Project8Data/'
data = os.listdir(folder)
data.remove('.DS_Store')
data.sort()

#create connection to local instance of Mysql 
cnx = mysql.connector.connect(
    host ='127.0.0.1',
    user ='root',
    password ='My_Password',
    auth_plugin= 'mysql_native_password'
    )

#create cursor
cursor = cnx.cursor()

# Create new database by dropping any existing database with the same name
cursor.execute('''DROP DATABASE IF EXISTS `NewPro8`;''')
cursor.execute('''CREATE DATABASE IF NOT EXISTS `NewPro8`;''')
cursor.execute('''USE NewPro8;''')

#commit to Mysql and close connection
cnx.commit()
cnx.close()

# Create empty list to store transformed data in
df = []
for file in data:
      
    #Read csv files in folder and transform data into pandas dataframe      
    d = pd.read_csv(folder + file)
    d1 = pd.DataFrame(d)    
    #print(d1) - check to ensure file is being read correctly formatted by pandas operations
    
    d1 = d1.replace(to_replace="(S)",value =np.nan)
    d1 = d1.replace(to_replace="(NA)",value =np.nan)
    d1 = d1.dropna(axis=0,how='all',inplace=False).dropna(axis=1,how='all',inplace=False).drop(columns=['Unnamed: 15','Unnamed: 16'],errors='ignore')
    d1 = d1.replace(to_replace=np.nan,value='0')
    d1 = d1.replace(",","",regex=True)
    #display(d1) - view dataframe to ensure transform operation were successful

    year = file[:-4]
    #print(year) - check to make sure year is correct
    
    d1.columns = ['Code','Busi Type','01-'+ year,'02-'+year,'03-'+year,'04-'+year,'05-'+year,
    '06-'+year,'07-'+year,'08-'+year,'09-'+year,'10-'+year,'11-'+year,'12-'+year,'TOTAL']
    #print(d1.columns) - check to ensure columns maintain names
    
    #Variable to use as table names
    when = "year" + year

    #open MySQL connector for individual file input
    cnx = mysql.connector.connect(
    host ='127.0.0.1',
    user ='root',
    password ='S3pt11N1n85',
    auth_plugin= 'mysql_native_password'
    )

    cursor = cnx.cursor()
    #choose database
    cursor.execute('''USE NewPro8;''')
    #Create table for each year as 'file' loops in 'data'
    cursor.execute('''CREATE TABLE `'''+when+'''`(`Code` VARCHAR(250) NOT NULL, `Busi Type` VARCHAR(250) NOT NULL, `01-'''+year+'''` INT NOT NULL, `02-'''+year+'''` INT NOT NULL,
        `03-'''+year+'''` INT NOT NULL, `04-'''+year+'''` INT NOT NULL, `05-'''+year+'''` INT NOT NULL, 
        `06-'''+year+'''` INT NOT NULL, `07-'''+year+'''` INT NOT NULL, `08-'''+year+'''` INT NOT NULL,
        `09-'''+year+'''` INT NOT NULL, `10-'''+year+'''` INT NOT NULL, `11-'''+year+'''` INT NOT NULL,
        `12-'''+year+'''` INT NOT NULL, `TOTAL` INT NOT NULL);''')
    
    #Begin for loop to enter values from each .csv file into table; also changing string values to integer
    for i, row in d1.iterrows():

        #SQL statement to insert values into table
        sql2 = "INSERT INTO `"+when+"` VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        code = row["Code"]
        kind = row["Busi Type"]
        jan = int(row["01-"+year]) 
        feb = int(row["02-"+year])
        mar = int(row["03-"+year])
        apr = int(row["04-"+year])
        may = int(row["05-"+year])
        jun = int(row["06-"+year])
        jul = int(row["07-"+year])
        aug = int(row["08-"+year])
        sep = int(row["09-"+year])
        oct = int(row["10-"+year])
        nov = int(row["11-"+year])
        dec = int(row["12-"+year])
        tot = int(row["TOTAL"])
    
        val = (code,kind,jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec,tot)
        cursor.execute(sql2,val)
        print("Record Inserted")

        #commit data and close connection
    cnx.commit()
    cnx.close()        

    # Add each table to database 
    df.append(d1)
# View database
display(df)



