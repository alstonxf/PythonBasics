# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:31:19 2020

@author: lee
"""


1. 三个同样的字母连在一起，一定是拼写错误，去掉一个的就好啦：比如 helllo -> hello
2. 两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好啦：比如 helloo -> hello
3. 上面的规则优先“从左到右”匹配，即如果是AABBCC，虽然AABB和BBCC都是错误拼写，应该优先考虑修复AABB，结果为AABCC

#%%

input1 = '''2
helloo
wooooooow'''
#%%
input1 = '''3
helloo
helllo
wooooow'''
#%%

input1 = input()
test = input1.split('\n')

def check(x):
    
    #三个同样的字母连在一起，一定是拼写错误，去掉一个的就好啦：比如 helllo -> hello
    y = x[:3]
    for i in range(3,len(x)):
        if x[i]==x[i-1] and x[i]==x[i-2]:
            pass
        else:
            y = y+x[i]
            
        #print(y)
    #两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好啦：比如 helloo -> hello
    z = y[:3]
    for i in range(3,len(y)):
        if y[i]==y[i-1] and y[i-2]==y[i-3]:
            pass
        else:
            z = z+y[i]
    print (z)
    return z
        
#check('helloo')
#check('wooooooow')

for each in test[1:]:
    check(each)
    
    
#%%
def check(x): 
    #三个同样的字母连在一起，一定是拼写错误，去掉一个的就好啦：比如 helllo -> hello
    y = x[:3]
    for i in range(3,len(x)):
        if x[i]==x[i-1] and x[i]==x[i-2]:
            pass
        else:
            y = y+x[i]
            
        #print(y)
    #两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好啦：比如 helloo -> hello
    z = y[:3]
    for i in range(3,len(y)):
        if y[i]==y[i-1] and y[i-2]==y[i-3]:
            pass
        else:
            z = z+y[i]
    print (z)
    return z

total_test_num = int(input())
for i in range(total_test_num):
    x = input()
    check(x)
    
#%%
for i in range(len(x)-2):
    x.replace(x[i,i+3])

#%% 麻将

input1 = '1 1 1 1 2 2 3 3 5 6 7 8 9'

all_cards = []

for i in range(1,10):
    all_cards.extend([i]*4)

got_cards = input1.split(' ')
got_cards_dict = {}
for each in got_cards:
    try:
       got_cards_dict[each]
       got_cards_dict[each] = got_cards_dict[each]+1
    except:
        got_cards_dict[each]=0
        got_cards_dict[each] = got_cards_dict[each]+1

available_cards = []
for each in list(got_cards_dict.keys()):
    if got_cards_dict[each] < 4:
        available_cards.append(each)

for each in available_cards:
    
#写一个函数判断给定14张牌是否可以胡牌。
    
#第一种情况：4个对子，一个雀头
#第二种情况：

#%%
#6 硬币问题：
n = input()
money_r = 1024-int(n)

coin_64 = int(str(money_r/64).split('.')[0])
#print(coin_64)

money_after64 = money_r-64*coin_64
coin_16 = int(str(money_after64/16).split('.')[0])
#print(coin_16)

money_after16 = money_after64-16*coin_16
coin_4 = int(str(money_after16/4).split('.')[0])
#print(coin_4)

coin_1 = money_after16-4*coin_4
#print(coin_1)

print(coin_64+coin_16+coin_4+coin_1)
















