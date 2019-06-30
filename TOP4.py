#有一个不多于5位的正整数，求它是几位数，分别打印出每一位数字。

import random
n = random.randint(0,9999)  #从0-9999之间获取一个随机数
n_len = len(str(n))    #显示字符串个数
print("该数是 %d 位数" % n_len)
print(n)
liststr = list(str(n))  #将随机数转换为列表
print(liststr)