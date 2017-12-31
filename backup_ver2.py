<<<<<<< HEAD
#-*-coding:utf-8-*-

import os
import time

#需备份的目录
source = ["E:\\work\\python\\backup_demo\\testFile\\testTxt.txt"]

#主备份目录
target_dir = 'E:\\work\\python\\backup_demo\\backup'

#备份目录不存在时，创建目录
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

#创建以当前日期命名的文件夹
today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

#os.sep,路径分隔符，通用
#time.strftime()，获取当前时间，并格式化
target = today + os.sep + now + '.zip'

if not os.path.exists(today):
	os.mkdir(today)
	print('successfully created directory:',today)

zip_command = 'zip -r {0} {1}'.format(target,''.join(source))

print('zip command is:')
print(zip_command)
print('running:')
if os.system(zip_command) == 0:
	print('successful backup to',target)
else:
	print('backup failed')
=======
#-*-coding:utf-8-*-

import os
import time

#需备份的目录
source = ["E:\\work\\python\\backup_demo\\testFile\\testTxt.txt"]

#主备份目录
target_dir = 'E:\\work\\python\\backup_demo\\backup'

#备份目录不存在时，创建目录
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

#创建以当前日期命名的文件夹
today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

#os.sep,路径分隔符，通用
#time.strftime()，获取当前时间，并格式化
target = today + os.sep + now + '.zip'

if not os.path.exists(today):
	os.mkdir(today)
	print('successfully created directory:',today)

zip_command = 'zip -r {0} {1}'.format(target,''.join(source))

print('zip command is:')
print(zip_command)
print('running:')
if os.system(zip_command) == 0:
	print('successful backup to',target)
else:
	print('backup failed')
>>>>>>> 备份程序
	