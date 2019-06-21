print("场景：体育课打篮球")
print("什么叫书呆子？就是玩的时候也在思考问题!")
print("这不书呆子在思考：假设篮球从一高处落下，"
      "每次落地后反弹回原来高度的一半在落下，"
      "那么篮球在第十次落地时，共经过了多少米？"
      "第十次反弹时高度是多少？")
high = int(input("\n请输入篮球落地时的高度："))
count = 0
num = high / (2**10)
while True:
    if count <= 10:
        break
    high = high * ((1 - (1/2) ** 10) / (1 - 1/2))
    count = count + 1
print("\n篮球在第十次落地时，共经过：%d 米" % high)
print("篮球第十次落地后反弹的高度为：%s 米" % num)