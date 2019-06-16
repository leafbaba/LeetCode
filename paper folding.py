print('*'*50)
print("\n好消息！好消息！动动小手折纸就能上月球了！\n")
thickness = 0.088  #纸的厚度为0.088毫米
distance = 363300000000000  #月球距离地球363300000000000毫米
n = 1
while thickness <= distance:  #循环条件厚度不超过距离
    thickness *= 2            #纸张对折一次厚度乘二
    n = n + 1                 #循环次数
print("亲，您只需要折%s次就能上月球了！\n" % n)
print('*'*50)