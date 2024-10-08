# #算術運算子
print(9 + 4)
print(3 / 2)
print(2 ** 3)

# #賦值運算子
a = 9
b = 4
a += b
print(a)
c = 3
d = 2
d **= c
print(d)

# #比較運算子(用 if 判斷)
e = 4
if e == 4:
    print('e 等於 4')
if e > 2: print('e 大於 2')
if e != 2: print('e 不等於 2')

# #邏輯運算子
f = 8
name = 'Apple'
if f == 8 and name == 'Apple':
    print('ok')
if f == 6 or name == 'Apple':
    print('name 等於 Apple')

#成員運算子
myList = [9, 5, 2, 7]
if 2 in myList:
    print('2 在 list 裡')
if 4 not in myList:
    print('4 不在 list 裡')    

