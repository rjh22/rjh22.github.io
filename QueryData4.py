from optparse import Values
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
from pandas.core.tools.timedeltas import to_timedelta
from IPython.display import display
import os 
#data = pd.read_csv('Project8Data/1992.csv')

cnx = cnx = mysql.connector.connect(
    host ='127.0.0.1',
    user ='root',
    password ='S3pt11N1n85'
    #auth_plugin= 'mysql_native_password'
)

cursor = cnx.cursor()

cursor.execute('''USE `Pro8`;''')


sql1 = '''SELECT `Kind of Business`,`TOTAL` FROM year1992 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1993 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1994 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1995 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1996 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1997 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1998 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1999 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2000 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2001 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2002 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2003 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2004 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2005 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2006 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2007 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2008 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2009 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2010 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2011 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2012 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2013 WHERE `Kind of Business` =  "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2014 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2015 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2016 WHERE `Kind of Business` =  "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2017 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2018 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2019 WHERE `Kind of Business` = "Men's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2020 WHERE `Kind of Business` ="Men's clothing stores"
GROUP BY TOTAL'''

cursor.execute(sql1)
df = {}
for value in cursor:
    df.setdefault(value[0],[]).append(value[1])

sql2 = ''' SELECT `Kind of Business`,`TOTAL` FROM year1992 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1993 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1994 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1995 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1996 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1997 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1998 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year1999 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2000 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2001 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2002 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2003 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2004 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2005 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2006 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2007 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2008 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2009 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2010 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2011 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2012 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2013 WHERE `Kind of Business` =  "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2014 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2015 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2016 WHERE `Kind of Business` =  "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2017 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2018 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2019 WHERE `Kind of Business` = "Women's clothing stores"
union SELECT `Kind of Business`,`TOTAL` FROM year2020 WHERE `Kind of Business` ="Women's clothing stores"
GROUP BY TOTAL '''

cursor.execute(sql2)

df2 = {}
for value in cursor:
    df2.setdefault(value[0],[]).append(value[1])

df.update(df2)

df = pd.DataFrame(df, columns= ["Men's clothing stores","Women's clothing stores"])
#print(df)

time_index = pd.date_range('30/1/1992',periods=28,freq='Y')

#print(time_index)

fig, ax = plt.subplots(figsize=[12,12])

ax.plot(time_index, df["Men's clothing stores"], marker='o',linewidth=2, label='Mens')
ax.plot(time_index, df["Women's clothing stores"], marker='o',linewidth=2, label='Womens')
plt.title("year Earnings")
#ax[0,0].plot(time_index, df["Women's clothing stores"], marker='o',linewidth=2)
#ax[0,0].set_title("Women's yearltime_index trends")
#ax[1,0].plot(time_index, df['Mens Percent Contribution'], marker='o',linewidth=2)
#ax[1,0].set_title('Mens Percent Contribution')
#ax[1,1].plot(time_index, df['Womens Percent Contribution'], marker='o',linewidth=2)
#ax[1,1].set_title('Womens Percent Contribution')


#ax[0,0].set(xlabel='years',ylabel='Money')
#ax[0,0].set(xlabel='years',ylabel='Money')
#ax[1,0].set(xlabel='years',ylabel='Percent')
#ax[1,1].set(xlabel='years',ylabel='Percent')
plt.legend()
plt.show()









