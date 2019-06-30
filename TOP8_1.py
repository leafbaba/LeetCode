#使用for循环1到100之间所有能被3整除的整数的和。

j = 0
#循环
for i in range(1,101):
    if i % 3==0:
        j = j + i
print(j)