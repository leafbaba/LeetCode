# 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个。
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。
# 到第10天早上想再吃时，见只剩下一个桃子了。
# 求第一天共摘了多少。程序分析：采取逆向思维的方法，从后往前推断。

peach = 1
count = 0
#循环
while count <= 12:  #猴子从摘桃到后面吃的只剩下一个桃子总共用了12天
    peach = (peach + 1) * 2
    count = 1 + count
print("第一天总共摘了 %d 个桃子！" % peach)