'''不回傳 值'''

# 定義函式
def show_name():
    print("AJ")

# 執行函式
show_name()

'''回傳 值'''

# 定義函式
def get_name():
   name = "AJ"
   return name

#  # 執行函式
result = get_name()
print(result)

'''傳遞變數'''
# 定義函式
def get_greeting(name):
    return "Hello," + name

# 執行函式
result = get_greeting("AJ")
print(result)