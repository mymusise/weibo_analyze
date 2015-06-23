#encoding:utf-8
from collections import defaultdict
import json
import uniout
from get import *
import datetime
import time
import os
def tree():
    return defaultdict(tree)
def main():
	temp=tree()
	temp[1]
	temp[1]['username']='滴滴打车'
	temp[1]['userid']='12342433'

	print str(json.dumps(temp)).decode('utf-8').encode('utf-8')
	pass

def test():
	f=open('temp.json','r')
	s=f.read()
	js= json.loads(s)
	print js['2']['username'].encode('utf-8')
	pass
def test1():
	my_driver=webdriver.Firefox()
	login_2(my_driver,'mymusise@sina.com','1262guochengxi.')
	get_weibo_comment(my_driver,'http://weibo.com/2846859150/BFe3qr2oG')

def test2():
	d1=datetime.datetime(2015,3,20)
	d2=datetime.datetime(2015,5,12)
	print d2-d1
	# oneday=d2-d1
	# for i in range(40):
	# 	d1=d1+oneday
	# 	print d1.strftime("%Y-%m-%d")
	# os.mkdir('./helo')
	# print os.path.isdir('./datedata/2015-05-02/')

def get_user_day_by_day(my_driver):
	lis=os.listdir('./datedata/2015-03-20:2015-05-12/userid')
	# for l in lis:
	# 	os.mkdir("./datedata/2015-03-20:2015-05-12/result/userdata/"+l)

if __name__ == '__main__':
	get_user_day_by_day(123)