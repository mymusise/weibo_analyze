#encoding:utf-8
import json
f=open('地震.json')
out=open('userid','wr')
data=json.load(f)
data_len= len(data)
for i in range(data_len):
	out.write(data[str(i)]['userid']+'\n')

r=open('userid','r')
l=r.readline()
while l!='':
	print l
	l=r.readline()
