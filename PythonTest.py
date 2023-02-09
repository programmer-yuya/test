# # 文字列の出力
print('Hello world')
print('maerge test')
print('sample')

# # 計算
num=800
price=5
print(num*price)

def greeting(name):
    print("Hello,", name)

greeting("World")

# 入出力、条件式
inputData = input('年数の入力（YYYY）:')

if not str.isdigit(inputData):
    print('数字ではないので終了します。')
elif int(inputData) >= 2020:
    nen = int(inputData)-2018
    print('令和'+str(nen)+'年')    
elif int(inputData) >= 1989:
    nen = int(inputData)-1988
    print('平成'+str(nen)+'年')
else:
    nen = int(inputData)-1925
    print('昭和'+str(nen)+'年')