# 编写一个程序，计算邮局汇款的汇费。如果汇款金额小于100元，汇费为一元，
# 如果金额在100元与5000元之间，按1%收取汇费，
# 如果金额大于5000元，汇费为50元。
# 汇款金额由命令行输入。

n = float(input("请输入汇款金额："))  #类型转换为浮点数
#判断
if n <100:
    print("汇费为：1 元！")
elif n < 5000:
    i = n * 0.01
    print("汇费为：%f 元！" % i)
else:
    print("汇费为：50 元！")