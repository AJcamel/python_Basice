# while 迴圈
count = 1
while count <= 5:
    print(count, end="")
    count += 1


'''
用法
range(n, m-1)

說明
會走訪 n 到 m-1 的數字
'''
# for i in range(5 , 0):
#     print(i, end = ",")


for i in range(4, 20, 3):
    print(i,end=',')