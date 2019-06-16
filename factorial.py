n = int(input("请输入需要阶乘的数："))    #输入阶乘的数字
sum = 1  #定义结果初始值为1
count = 0
while count <= n:   #循环条件循环次数不超过n
    sum = count * sum    #阶乘规则
    count = count + 1    #循环次数
print("\n得到的结果为：%s" % sum)