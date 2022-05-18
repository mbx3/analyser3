import mysql.connector
import sys


conn = mysql.connector.connect(user = 'root',
                               host = 'localhost',
                               database = 'game')

cursor = conn.cursor()


cursor.execute('SELECT * FROM `tbl_zarib`')
data = cursor.fetchall()
data=[float(i[1]) for i in data]

conn.close()


if len(sys.argv)==4:
    repeat=int(sys.argv[1])
    zarib=float(sys.argv[2])
    num=int(sys.argv[3])
else:
    repeat=int(input('min tekrar : '))
    zarib=float(input('zarib : '))
    num=int(input('max: '))

deltas={}
for i,d in enumerate(data):
    if data.count(d)>=repeat:
        n=1
        while (i+n<len(data) and data[i+n]<zarib):
            n+=1
        if n>1:
            if d in deltas:
                deltas[d].append(n-1)
            else:
                deltas[d]=[n-1]

with open('Analysis2.txt','w') as file:
    deltas=dict(sorted(deltas.items()))
    for x in deltas:
        if max(deltas[x])<=num:
            print(x,end=',')
            file.write(f'{x},')