import os
from time import sleep
from mail import *

check_time=200
check_dir="./"

def main():
	while 1:
		file_list=os.listdir(check_dir)
		len1=len(file_list)
		sleep(check_time)
		file_list=os.listdir(check_dir)
		len2=len(file_list)
		if len2==len1:
			mail_to('server_ping@163.com','pingserver','smtp.163.com','604072107@qq.com','spider stop in [answer] ','all_has_downloaded!')
			break
		sleep(check_time)
	pass


if __name__ == '__main__':
	main()