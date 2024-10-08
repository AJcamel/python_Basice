# 直接從模組中匯入函式
from myModule import pow, segmenSentence

# 計算幾次方
num = pow(2, 3)
print(num)

# 簡單斷詞
txt = "I will always love you"
list_result = segmenSentence(txt)
print(list_result)

if __name__=="__main__":
    print(__name__)
