print("计算1到n的阶乘之和！")
n = int(input("请输入n的值："))
print("求1到%d阶乘之和，结果见下：" % n)
m = 1
num = 0
count = 1
while True:
    if count >= n+1:
        break
    m = m * count
    num = num + m
    count = count + 1
print(num)