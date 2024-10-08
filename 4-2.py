# 初始化一個 list
ids = [1, 2, 3, 4, 5, 6]
print(ids[5])

#新增元素在 list 尾端
ids.append(79)
print(ids)

# 修改索引位置的元素
ids[4] = 99
print(ids)

# 刪除索引位置的元素
ids.pop(4)
print(ids)

# 新增元素 9 在指定索引 1，其餘元素往後移
ids.insert(1,9)
print(ids)

# 移除指定的值
ids.remove(9)
print(ids)

# 補充: 字串分割成 list
'''
用法
string.split()
說明
默認以空格、換行字元分割字串 string，回傳 list
'''
Apple = "1, 2, 3,4"
Boss = Apple.split(",")
print(Boss)

# 補充: 將 list 元素合併成字串
'''
用法
string.join(seq)
說明
以 string 為分隔符號，將 seq 中的元素串起來成為一個新的字串
'''
Apple = ['古道', '西風', '瘦馬']
Boss = "-".join(Apple)
print(Boss)

Boss = "".join(Apple)
print(Boss)

Apple = "Hello,World!"
print(Apple[0:5])