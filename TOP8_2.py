#使用while循环求1到100之间所有能被3整除的整数的和。

num = 0
s = 0
#循环
while num < 99:
    num = num + 3
    s = num + s
print("1到100之间能被3整除的整数之和为：%s" % s)