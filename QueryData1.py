import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
from pandas.core.tools.timedeltas import to_timedelta
from IPython.display import display

#data = pd.read_csv('Project8Data/1992.csv')

cnx = mysql.connector.connect(
    host ='127.0.0.1',
    user ='root',
    password ='My_password'
    #auth_plugin= 'mysql_native_password'
)

cursor = cnx.cursor()

cursor.execute('''USE `Pro8`;''')

sql = '''SELECT `Kind of Business`,`TOTAL` FROM Year2020 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2019 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2018 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2017 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2016 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2015 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2014 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2013 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2012 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2011 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2010 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2009 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2008 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2007 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2006 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2005 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2004 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2003 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2002 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2001 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year2000 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year1999 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year1998 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year1997 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year1996 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year1995 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year1994 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year1993 WHERE `Kind of Business` = 'Retail and food services sales, total'
union SELECT `Kind of Business`,`TOTAL` FROM Year1992 WHERE `Kind of Business` = 'Retail and food services sales, total'
Group BY TOTAL'''
cursor.execute(sql)
y= []

for value, total in cursor:
    a = int(total)
    y.append(a)
    #for i in range(len(x)):
        #if x[i] == 'Retail and food services sales, total,':
         #   x[i] = ''
np.array(y).tolist()

print(len(y)) 


cursor.execute('''SHOW TABLES;''')
x = []
for table in cursor:
    b = table
    b = int(b[0].replace('Year',''))
    x.append(b)

x = np.delete(x,21)
#np.array(x).tolist()
print(x)


plt.plot(x,y)
plt.xlabel('year')
plt.ylabel('total')
plt.title('Total per year')

plt.show()


