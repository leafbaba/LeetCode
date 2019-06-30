# 由命令行输入一个4位整数，求将该数反转以后的数，
# 如原数为1234，反转后的数位4321

n = int(input("请输入一个四位整数："))
if n > 10000:
    print("输入的数字超过四位！")
else:
    print("输入正确,正在反转！")
    a = n // 1000   #通过取整取出千位上的数字
    b = n % 1000 // 100   #先取余在取整得到百位上的数字
    c = n % 1000 % 100 // 10   #原理同上
    d = n % 1000 % 100 % 10    #原理同上
    num = d*1000 + c*100 + b*10 +a
    print("反转后的数位为：%d" % num)