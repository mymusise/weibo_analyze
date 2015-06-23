#encoding:utf-8
import os
import json
import jieba
def get_all_userid():
	root="./datedata/2015-03-20:2015-05-12/"
	weibos_file_list=os.listdir(root)
	all_userid=[]
	number=0
	for weibos_file in weibos_file_list:
		if os.path.isfile(root+weibos_file):
			f_obj=open(root+weibos_file)
			json_date=json.load(f_obj)
			json_len=len(json_date)
			if json_len==0:
				continue
			else:
				for i in range(json_len):
					userid=json_date[str(i)]['userid']
					number=number+1
					if userid not in all_userid:
						all_userid.append(userid)
	#get userid what has download
	all_download_userid=[]
	download_ps=os.listdir(root+'result/userdata/')
	for download_p in download_ps:
		download_pps=os.listdir(root+'result/userdata/'+download_p)
		for downloaded_userid in download_pps:
			if downloaded_userid not in all_download_userid:
				all_download_userid.append(downloaded_userid)
	'''
	#merge the all_download_userid with all_userid
	#all_userid - all_download_userid in all_userid
	#all_userid + all_download_userid not in all_userid
	'''
	for download_userid in all_download_userid:
		if download_userid in all_userid:
			print download_userid
			all_userid.remove(download_userid)

	print len(all_userid),number,len(all_download_userid)
	userid_file=open(root+'result/all_userid','w')
	for userid in all_userid:
		userid_file.write(userid+'\n')
	# help(all_userid)

def get_most_hot_weibos():
	root="./datedata/2015-03-20:2015-05-12/"
	weibos_file_list=os.listdir(root)
	most_weibos=[('','','',0),('','','',0),('','','',0),('','','',0),('','','',0),('','','',0),('','','',0),('','','',0),('','','',0),('','','',0)]
	number=0
	for weibos_file in weibos_file_list:
		if os.path.isfile(root+weibos_file):
			f_obj=open(root+weibos_file)
			json_date=json.load(f_obj)
			json_len=len(json_date)
			if json_len==0:
				continue
			else:
				for i in range(json_len):
					link=json_date[str(i)]['link']
					weibos_stat=json_date[str(i)]['stat']
					weibos_stat=weibos_stat.split('\n')
					if len(weibos_stat[1])>=3:
						forward_number=int(weibos_stat[1][2:])
					else:
						forward_number=0
					if len(weibos_stat[2])>=3:
						comment_number=int(weibos_stat[1][2:])
					if len(weibos_stat)>3:
						zan_number=int(weibos_stat[3])
					hot_value=(forward_number*6+comment_number*3+zan_number*1)/10
					# print "forward_number:",forward_number,"comment_number:",comment_number,"zan_number:",zan_number,"hot_value:",hot_value
					if hot_value>most_weibos[-1][-1]:
						most_weibos[-1]=(json_date[str(i)]['link'],hot_value)
						most_weibos=sorted(most_weibos,key=lambda x:x[-1],reverse=True)
	print most_weibos
	result_file=open('../data/result/top_hot_weibo','w')
	result_file.write(str(most_weibos))

def result2():
	root="./datedata/2015-03-20:2015-05-12/"
	weibos_file_list=os.listdir(root)
	most_weibos=[('',0),('',0),('',0),('',0),('',0),('',0),('',0),('',0),('',0),('',0)]
	number=0
	for weibos_file in weibos_file_list:
		if os.path.isfile(root+weibos_file):
			f_obj=open(root+weibos_file)
			json_date=json.load(f_obj)
			json_len=len(json_date)
			if json_len==0:
				continue
			else:
				for i in range(json_len):
					link=json_date[str(i)]['link']
					weibos_stat=json_date[str(i)]['stat']
					weibos_stat=weibos_stat.split('\n')
					if len(weibos_stat[1])>=3:
						forward_number=int(weibos_stat[1][2:])
					else:
						forward_number=0
					if len(weibos_stat[2])>=3:
						comment_number=int(weibos_stat[1][2:])
					if len(weibos_stat)>3:
						zan_number=int(weibos_stat[3])
					hot_value=(forward_number*6+comment_number*3+zan_number*1)/10
					# print "forward_number:",forward_number,"comment_number:",comment_number,"zan_number:",zan_number,"hot_value:",hot_value

					link=json_date[str(i)]['link']
					userid=link.split('/')[-2]
					not_in=1
					for i in range(len(most_weibos)):
						if userid==most_weibos[i][0]:
							most_weibos[i]=(userid,most_weibos[i][1]+hot_value)
							most_weibos=sorted(most_weibos,key=lambda x:x[-1],reverse=True)
							not_in=0
							break
					if not_in:
						if hot_value>most_weibos[-1][-1]:
							most_weibos[-1]=(userid,hot_value)
							most_weibos=sorted(most_weibos,key=lambda x:x[-1],reverse=True)
	print str(most_weibos)
	result_file=open('../data/result/top_hot_user','w')
	result_file.write(str(most_weibos))
	pass

def get_user_city(userid):
	f=open('../data/userdata/'+userid,'r')
	city=''
	s=f.readline()
	while s!='':
		if s[:9]=='地区：':
			s=s.replace('\n','')
			city=s[9:].decode('utf-8')
		elif s=='所在地：\n':
			s=f.readline()
			s=s.replace('\n','')
			city=s.decode('utf-8')
		s=f.readline()
	return city
	

def get_day_city_number_info():
	root="./datedata/2015-03-20:2015-05-12/"
	weibos_file_list=os.listdir(root)
	day_number=[]
	for weibos_file in weibos_file_list:
		if os.path.isfile(root+weibos_file):
			f_obj=open(root+weibos_file)
			json_date=json.load(f_obj)
			json_len=len(json_date)
			day_of_city={}
			for i in range(len(json_date)):
				userid= json_date[str(i)]['userid']
				try:
					city=get_user_city(userid)
				except:
					city=""
				if city!='':
					if city not in day_of_city:
						day_of_city[city]=1
					else:
						day_of_city[city]+=1
					print city.encode('utf-8')
			day_of_city=sorted(day_of_city.iteritems(),key=lambda x:x[1])
			day_number.append({weibos_file:day_of_city})
			# day_number.append((weibos_file,json_len))
	day_number=sorted(day_number,key=lambda x:x)
	print json.dumps(day_number)

	# print day_number
	result_file=open('../data/result/day_city_number','w')
	result_file.write(str(day_number))
	pass



def get_day_keyWord():
	jieba.load_userdict('../data/明星人名1')
	jieba.load_userdict('../data/地震级数')
	jieba.load_userdict('../data/地震学术语')
	root="./datedata/2015-03-20:2015-05-12/"
	weibos_file_list=os.listdir(root)
	day_keyWord=[]
	number=0
	for weibos_file in weibos_file_list:
		if os.path.isfile(root+weibos_file):
			f_obj=open(root+weibos_file)
			json_date=json.load(f_obj)
			json_len=len(json_date)
			if json_len==0:
				day_keyWord.append((weibos_file,0,''))
			else:
				content=""""""
				for i in range(json_len):
					content+=json_date[str(i)]['content']

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
				key_words=""
				for k in key[:15]:
					if len(k[0])>3:
						key_words+=k[0]+'|'
						print k[0],k[1]
						# temp.write(k[0]+' '+str(k[1])+'\n')
				day_keyWord.append((weibos_file,json_len,key_words))
	day_keyWord=sorted(day_keyWord,key=lambda asd:asd[0],reverse=False)
	result_file=open('../data/result/day_keyWord','w')
	for day in day_keyWord:
		result_file.write(day[0][5:]+'\t'+str(day[1])+'\t'+day[2]+'\n')
	pass

def get_all_keyword():
	jieba.load_userdict('../data/明星人名1')
	jieba.load_userdict('../data/地震级数')
	jieba.load_userdict('../data/地震学术语')
	root="./datedata/2015-03-20:2015-05-12/"
	weibos_file_list=os.listdir(root)
	keyWord=[]
	number=0
	all_content=""""""
	for weibos_file in weibos_file_list:
		if os.path.isfile(root+weibos_file):
			f_obj=open(root+weibos_file)
			json_date=json.load(f_obj)
			json_len=len(json_date)
			if json_len!=0:
				for i in range(json_len):
					all_content+=json_date[str(i)]['content']
	keys='/'.join(jieba.cut(all_content,cut_all=True)).encode('utf-8')
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
	result_file=open('../data/result/all_keyWord','w')
	for i in key[:100]:
		if len(i[0])>3:
			print i[0],i[1]
			result_file.write('"'+i[0]+'","'+i[0]+'",'+str(i[1])+'\n')
	pass

def main():
	# get_all_userid()
	# get_most_hot_weibos()
	# result2()
	# get_day_city_number_info()
	get_day_keyWord()
	# get_all_keyword()

if __name__ == '__main__':
	main()