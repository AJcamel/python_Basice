'''一般 list 用法'''
list01 = []
for x in range(10):
    list01.append(x)
print(list01)

# 一行直接建立 list
liste02 = [x for x in range(10)]
print(liste02)

# 還可以設定條件
list03 = [x for x in range(10) if x % 2 == 0]
print(list03)