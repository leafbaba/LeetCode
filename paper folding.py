print('*'*50)
print("\n好消息！好消息！动动小手折纸就能上月球了！\n")
thickness = 0.088
distance = 363300000000000
n = 1
while thickness <= distance:
    thickness *= 2
    n = n + 1
print("亲，您只需要折%s次就能上月球了！\n" % n)
print('*'*50)