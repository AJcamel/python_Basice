'''
格式化字串 - 使用 %
'''
# 多組文字
msg = "%s, %s" % ("Hi","AJ")
print(msg)

#整數
msg = "I am %d years old." % 36
print(msg)

#文字與整數
msg = "My name %s , %d years old." %("AJ", 36)
print(msg)

#指定寬度(維持10個字元長度，預設向右對齊)
msg = '[%10s]' % 'Hello'
print(msg)

#向左對齊
msg = '[%-10s]' % 'Hello'
print(msg)

#指定浮點數位數
msg = '[%8.3f]' % 12.3456
print(msg)

# 指定文字長度上限 (只有文字，才在格式化字串中加入「.」來限定字串長度)
msg = '[%.3s]' % 'Hello'
print(msg)

# 空白補 0
msg = '[%6.2f]' % 3.1415926
print(msg)
