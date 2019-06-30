#编写一个程序，找出大于200的最小的质数

for num in range(2,200):
    for i in range(2,num):
        if num % i == 0:
            j = num / i  #另一个因子
            break
    else:
        print("%d 是质数" % num)