# 用來建立 dict key(s) 的 list
list01 = ['name', 'school', 'phone_number']

# 建立 dict
dict01 = {key: "" for key in list01}
# 檢索目前的 dict
print(dict01)

# 各別填寫 dict 的 value
dict01["name"] = "AJ"
dict01["school"] = "ntu"
dict01["phone_number"] = "0911111111"
dict01["age"] = 18
del dict01["school"]
print(dict01)