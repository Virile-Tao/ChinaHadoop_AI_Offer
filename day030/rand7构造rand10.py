import random
def rand7():
    return random.randint(1, 7) # 1到7均匀分布的随机数

def rand49():
    return (rand7() - 1) * 7 + rand7() # 1到49均匀分布的随机数，是[0，7，14，21，28，35，42]与[1，2，3，4，5，6，7]两两相加的结果
    
def rand10():
    while True:
        res = rand49()
        if 4 <= res <= 43: # 4到7除4得1, 8到11除4得2， 12到15除4得3，、、、40到43除4得10
            return res // 4
            
lst = [0 for _ in range(10)]
N = 1000000
while N:
    lst[rand10() - 1] += 1
    N -= 1
print("1到10对应的概率:")
print(list(map(lambda x: x / 1000000, lst)))
