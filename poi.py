import json,time
from urllib import request
url1='https://restapi.amap.com/v5/place/polygon?key={0}&polygon={1}&types={2}&page_size={3}&page_num={4}'
key='00c7be21f1350c27784aaf9d7d388df5'
polygon='121.31,31.29|121.63,31.18'
types=120000
size=25
num=1
out=[]
while num<=100:
    url=url1.format(key,polygon,types,size,num)

    html=request.urlopen(url).read()
    t=json.loads(html)
    p=t['pois']
    f=['parent', 'address', 'distance', 'pcode', 'adcode', 'pname', 'cityname', 'type', 'typecode', 'adname', 'citycode', 'name',  'id']
    for poi in p:
        line=[]
        for i in f:
            line.append(poi[i])
        line.append(poi['location'].split(',')[0])
        line.append(poi['location'].split(',')[1])
        out.append(line)
    print(num)
    num+=1
timemark=str(time.strftime('%Y%m%d%H%M%S'))
output=open('poi_{0}.txt'.format(timemark),'wb')
title='\t'.join(f)+'\tx\ty\n'
output.write(title.encode('utf8'))
for l in out:
    output.write(('\t'.join(l)+'\n').encode('utf8'))
output.close()