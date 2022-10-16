from optparse import Values
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
from pandas.core.tools.timedeltas import to_timedelta
from IPython.display import display
import os 
#data = pd.read_csv('Project8Data/1992.csv')

cnx = mysql.connector.connect(
    host ='127.0.0.1',
    user ='root',
    password ='S3pt11N1n85'
    #auth_plugin= 'mysql_native_password'
)

cursor = cnx.cursor()

cursor.execute('''USE `Pro8`;''')


sql1 = '''SELECT `Kind of Business`,`TOTAL` FROM year2020 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2019 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2018 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2017 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2016 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2015 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2014 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2013 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2012 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2011 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2010 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2009 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2008 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2007 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2006 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2005 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2004 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2003 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2002 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2001 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2000 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1999 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1998 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1997 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1996 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1995 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1994 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1993 WHERE `Kind of Business` IN ('Book stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1992 WHERE `Kind of Business` IN ('Book stores')
GROUP BY TOTAL'''

cursor.execute(sql1)

df = {}
for value in cursor:
    df.setdefault(value[0],[]).append(value[1])

sql2 = '''SELECT `Kind of Business`,`TOTAL` FROM year2020 WHERE `Kind of Business` ='Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2019 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2018 WHERE `Kind of Business` =  'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2017 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2016 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2015 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2014 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2013 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2012 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2011 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2010 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2009 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2008 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2007 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2006 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2005 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2004 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2003 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2002 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2001 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year2000 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year1999 WHERE `Kind of Business` =  'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year1998 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year1997 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year1996 WHERE `Kind of Business` =  'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year1995 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year1994 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year1993 WHERE `Kind of Business` = 'Hobby, toy, and game stores'
union SELECT `Kind of Business`,`TOTAL` FROM year1992 WHERE `Kind of Business` ='Hobby, toy, and game stores'
GROUP BY TOTAL'''

cursor.execute(sql2)

y= []
df1 = {}
for value in cursor:
    df1.setdefault(value[0],[]).append(value[1])


sql3 = '''SELECT `Kind of Business`,`TOTAL` FROM year2020 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2019 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2018 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2017 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2016 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2015 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2014 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2013 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2012 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2011 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2010 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2009 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2008 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2007 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2006 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2005 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2004 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2003 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2002 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2001 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year2000 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1999 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1998 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1997 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1996 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1995 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1994 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1993 WHERE `Kind of Business` IN ('Sporting goods stores')
union SELECT `Kind of Business`,`TOTAL` FROM year1992 WHERE `Kind of Business` IN ('Sporting goods stores')
GROUP BY TOTAL'''

cursor.execute(sql3)

y= []
df2 = {}
for value in cursor:
    df2.setdefault(value[0],[]).append(value[1])
#print(df2)
cursor.execute('''SHOW TABLES;''')
for table in cursor:
    b = table
    b = int(b[0].replace('year',''))
    y.append(b)

y = np.delete(y,21)
df.update(df1)
df.update(df2)

fig, ax = plt.subplots(figsize=[9,7])

ax.plot(y, df['Book stores'], marker='o',linewidth=2,label = 'Book stores')
ax.plot(y, df['Hobby, toy, and game stores'], marker='o',linewidth=2,label = 'Hobby, toy, and game stores')
ax.plot(y, df['Sporting goods stores'], marker='o',linewidth=2,label = 'Sporting goods stores')

plt.legend()
plt.show()
