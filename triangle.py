n = int(input('请输入等腰三角形高度：'))
for i in range(n+1):   #控制行
    # 控制列，左侧空白的部分，控制正三角形行的开始位置
    for j in range(n-i):
        print(end=' ')
     #控制列，正三角形的部分
    for k in range(2*i-1):
        print('*',end='')
    #打印完一行后换行
    print()