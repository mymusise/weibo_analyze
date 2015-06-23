#encoding:utf-8
import json
import jieba
def get_content():
	f=open("地震.json",'r')
	temp=open('content','w')
	j=json.load(f)
	for i in range(len(j)):
		temp.write(j[str(i)]['content'].encode('utf-8')+'\n')

def get_key():
	jieba.load_userdict('明星人名1')
	jieba.load_userdict('地震级数')
	jieba.load_userdict('地震学术语')
	f=open('content','r')
	temp=open('key','w')
	content=f.read()
	keys='/'.join(jieba.cut(content,cut_all=True)).encode('utf-8')
	keys=keys.replace('日','')
	keys=keys.replace('的','')
	keys=keys.replace('月','')
	keys=keys.split('/')
	key={}
	for k in keys:
		if k in key:
			key[k]+=1
		else:
			key[k]=1
	key=sorted(key.iteritems(),key=lambda asd:asd[1],reverse=True)
	for k in key[:100]:
		if len(k[0])>3:
			print k[0],k[1]
			temp.write(k[0]+' '+str(k[1])+'\n')

def test1():
	f=open('明星人名','r')
	temp=open('明星人名1','w')
	s=f.read()
	s=s.replace("\n"," 500 nr\n")
	temp.write(s)

def test2():
	f=open('地震级数','w')
	for x in range(11):
		for y in range(9):
			if y!=0:
				f.write(str(x)+'.'+str(y)+'级 100 n\n')
			else:
				f.write(str(x)+'级 100 n\n')				
	pass

def main():
	# test1()
	# test2()
	get_key()

if __name__ == '__main__':
	main()