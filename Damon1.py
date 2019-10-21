# coding=utf-8
import random
import time

'''
    练习：这是一个简单的猜拳游戏
'''
flag = True
while flag:
    print('################ 欢迎来到猜拳游戏 ##################')
    player = int(input('请输入你要出的拳(1(剪刀)，2(石头)，3(布))：'))
    computer = random.randint(1, 3)

    time.sleep(1)

    if player < computer or (computer == 1 and player == 3):
        print('玩家出的{}，电脑出的是{}，电脑玩家获胜。'.format(player, computer))
        once_agin = input('还要再来一次吗(y/n)？')
        if once_agin == 'y':
            continue
        elif once_agin == 'n':
            flag = False
        else:
            print('输入错误')
            flag = False
    elif player == computer:
        print('玩家出的{}，电脑出的是{}，双方打成了平手。'.format(player, computer))
        once_agin = input('还要再来一次吗(y/n)？')
        if once_agin == 'y':
            continue
        elif once_agin == 'n':
            flag = False
        else:
            print('输入错误')
            flag = False
    else:
        print('玩家出的{}，电脑出的是{}，玩家胜。'.format(player, computer))
        once_agin = input('还要再来一次吗(y/n)？')
        if once_agin == 'y':
            continue
        elif once_agin == 'n':
            flag = False
        else:
            print('输入错误')
            flag = False
else:
    print('################ 您已退出游戏，欢迎下次光临 ##################')
