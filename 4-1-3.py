# f-string (又稱作 formatted string literals, version >= 3.6)
name = 'AJ'
age = '25'
resuit = f'name: {name}, age: {age}'
print(resuit)

# 靠左對齊、靠右對齊
resuit = f"name: [{name:<10}], age: [{age:>10}]"
print(resuit)

# 靠左對齊、靠右對齊，字數不足，補「ㄏ」(沒寫補什麼，預設空格)
resuit = f"name: [{name:ㄏ<10}], age: [{age:ㄏ>10}]"
print(resuit)

# 置中對齊
resuit = f"name: [{name:^10}], age: [{age:^10}]"
print(resuit)

# 指定文字長度上限 
resuit = f"name: [{name:^10.2}]"
print(resuit)