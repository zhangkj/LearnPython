#-*-encoding:utf-8-*-

#==========================实用函数
#计算闰年函数
def LeapYear(year):
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        return  True
    else:
        return  False

#print LeapYear(2015)


# =============================获取上一级目录
#print os.path.abspath(os.path.join(os.path.dirname('ch02_E2.py'),os.path.pardir))

#==============================================标准库：re 正则表达式
import re
strText ="output_1986_output_1999.txt"
regex = re.compile(r"output_(\d{4})")   #re.compile 可以把正则表达式编译成一个正则表达式对象。
m1 = re.search(regex,strText)   #re.search函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回，如果字符串没有匹配，则返回None。
m2 = re.match(regex,strText)    #re.match从头开始检查字符串是否符合正则表达式。必须从字符串的第一个字符开始就相符。
m3 =re.findall(regex,strText)  #re.findall可以获取字符串中所有匹配的字符串。
m4= re.split(regex,strText)    ## 根据正则表达式分割字符串， 将分割后的所有子字符串放在一个表(list)中返回
m5 =re.sub(regex,"a",strText)

print m1.group(0),m1.group(1),m2.group(0),m2.group(1),m3,m4,m5


#===============标准库：time，datetime 时间与日期
import  time
import  datetime

#time.sleep(2)  #sleep for 2 seconds

t = datetime.datetime(2016,3,24,13,15,22)
t2 = datetime.datetime(2016,3,24,13,15,21)
t1 = time.localtime()
#print t.year,t.minute,t.weekday(),t1
delta1 = datetime.timedelta(seconds=600)  #一个时间间隔对象timedelta
delta2 = datetime.timedelta(weeks=3)
format ="output-%Y-%m-%d-%H%M%S.txt"   #此处小写y会报错
strtime = "output-1997-12-23-030000.txt"
t3 = datetime.datetime.strptime(strtime,format)#用格式化读取的方式读取时间信息。
#print t+delta1,t+delta2,t-t2
#print t3,t2.strftime(format)          #datetime对象的strftime()方法，来将datetime对象转换为特定格式的字符串。



#===================标准库：存储对象（pickle包，cpickle包）
#包括1.将内存中的对象转换成文本流；2.重建对象；
import pickle
class Bird(object):
    have_father = True
    way_of_reproduction = 'egg'
'''
summer = Bird()
picklestring = pickle.dumps(summer) #使用pickle.dumps()方法可以将对象summer转换成了字符串 picklestring(也就是文本流)
writef = open('txtwrite.txt','w')
writef.write(picklestring)
fn = 'a.pkl'

with open(fn,'w') as f:
    picklestring = pickle.dump(summer,f) #使用pickle.dump()的方法，将上面两部合二为一,对象summer存储在文件a.pkl
with open(fn,'r') as f2:
    summer2 = pickle.load(f2)            #使用pickle.loads(str)的方法，将字符串转换成为对象
    #print summer2.have_father
'''

#=================标准库：子进程（subprocess包）


