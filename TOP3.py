#试写一个三位数，从小到大排列，然后再从大到小排列。

n = input("请输入一个三位数：")
liststr = list(n)  #将字符串转换为列表
liststr.sort(reverse=True)  #将列表中元素倒序
print(liststr)
