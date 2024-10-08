# 初始化 dict
dict01 = {"蘋果": 100, "橘子": 20, "水梨": 50}
print(dict01)

# 上面的初始化過程，也可以寫成:
dict01 = dict()
dict01['蘋果'] = 100
dict01['橘子'] = 20
dict01['水梨'] = 50
print(dict01)

# 印出蘋果的價格
print(dict01['蘋果'])

# 修改橘子的價格
dict01['橘子'] = 30
print(dict01['橘子'])

# 刪除 水梨
del dict01['水梨']
print(dict01)
dict02 = {
    'name': 'AJ',
    'age': 18,
    'info': {
        'nickname': 'boatman',
        'favorite_role':'Doraemon',
        'phone_number':['0911111111','0922222222','0933333333'
        ]
    }
}

for number in dict02['info']['phone_number']:
    print(number)