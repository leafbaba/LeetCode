n = int(input("请输入需要阶乘的数："))
count = 1
sum = 1
while count <= n:
    sum = count * sum
    count = count + 1
print("\n得到的结果为：%s" % sum)