from math import floor
from statistics import mean
import mysql.connector
import sys


conn = mysql.connector.connect(user = 'root',
                               host = 'localhost',
                               database = 'game')

cursor = conn.cursor()


cursor.execute('SELECT * FROM `tbl_zarib`')
data = cursor.fetchall()
lines=[float(i[0]) for i in data]
data=[float(i[1]) for i in data]

conn.close()


minBalance=0
numLost=0
numWon=0
balance=0
maxDistance=0
maxDisLine=0

conditions=[]
with open("data.txt","r") as f:
    for l in f.readlines():
        conditions.append(list(map(float,l.split())))

deltas={}
for i,d in enumerate(data[:-1]):
    target=0
    for c in conditions:
        if c[0]<=d<=c[1]:
            target=round(floor(d/c[2]*100)/100,2)
            if target<1: target+=1
            break
    
    if target==0: continue

    n=1
    while (i+n<len(data) and data[i+n]<target):
        n+=1

    if target in deltas:
        deltas[target].append(n-1)
    else:
        deltas[target]=[n-1,]

    if n==1:
        numWon += 1
        balance += round(target-1,2)
    else:
        numLost += 1
        balance -= 1
        if n-1>maxDistance: 
            maxDistance=n-1
            maxDisLine=lines[i]
        if balance<minBalance: minBalance=balance

keys=sorted(deltas)
with open('report.txt','w') as f:
    f.write(f'##General##\nLosts : {numLost}\nWons : {numWon}\nBalance : {balance}\nSequential Losts : {maxDistance} (id : {int(maxDisLine)})\nMin Balance : {minBalance}\n\n##Coefs##\n')
    f.write('%-5s  \t\t%-5s\t\t%-5s\t\t%-5s\t\t%-5s\n'%('',"Len",'Avg','Max','Lost'))
    for c in keys:
        ln=len(deltas[c])
        avg=mean(deltas[c])
        mx=max(deltas[c])
        nlost=len([i for i in deltas[c] if i>0])        
        f.write('%-5.2f :\t\t%-5d\t\t%-5.2f\t\t%-5d\t\t%-5d(%-5.2f%%)\n'%(c,ln,avg,mx,nlost,nlost/ln*100))