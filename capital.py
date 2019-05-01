import numpy as np
import random

p = 0.0
p1 = 0.0
p2 = 0.0
payoff_win = 0
payoff_lose = 0
p1_win = 0
p2_win = 0
p1_lose = 0
p2_lose = 0
M = 0
val_A = 0.0
val_B = 0.0
val_B1 = 0.0
val_B2 = 0.0


def init_Game_A():
    global p, payoff_win, payoff_lose, val_A 
    p = 0.5
    payoff_win = 1
    payoff_lose = -1
    val_A = (float)((p * payoff_win) + ((1.0 - p) * payoff_lose))


def init_Game_B():
    global p1, p2, p1_win, p2_win, p1_lose, p2_lose, M, val_B, val_B1, val_B2
    p1 = 0.1
    p2 = 0.75
    p1_win = 1
    p2_win = 1
    p1_lose = -1
    p2_lose = -1
    M = 3
    val_B = (float)((1.0/ M) * (p1 * p1_win + (1.0 - p1) * p1_lose) + (1.0 - (1.0 / M)) * (p2 * p2_win + (1.0 - p2) * p2_lose))
    val_B1 = (float)((1.0/ M) * (p1 * p1_win + (1.0 - p1) * p1_lose))
    val_B2 = (float)((1.0 - (1.0 / M)) * (p2 * p2_win + (1.0 - p2) * p2_lose))


def set_game():
    init_Game_A()
    init_Game_B()


def play_A(capital, count):
    count += 1
    result_A = random.uniform(0,1)
    if result_A <= p:
        capital += payoff_win
    else:
        capital += payoff_lose
    print("count = %d" %count)
    print("capital = %d" %capital)
    return capital, count


def play_B(capital, count):
    count += 1
    result_B = random.uniform(0,1)
    if capital % M == 0:
        if result_B <= p1:
            capital += p1_win
        else:
            capital += p1_lose
    else:
        #print("Never reach!")
        if result_B <= p2:
            capital += p2_win
        else:
            capital += p2_lose 
    print("count = %d" %count)
    print("capital = %d" %capital)
    return capital, count


def start():
    set_game()
    init_capital = 0
    count = 0
    print("val_A = %f" %val_A)
    print("val_B = %f" %val_B)
    print("val_B1 = %f" %val_B1)
    print("val_B2 = %f" %val_B2)
    print("initial capital = %d" %init_capital)
    print("M = %d" %M)
    while(count < 10000):
        for i in range(0,3):
            init_capital, count = play_A(init_capital, count)
            #if init_capital < 0:
                #break
        for j in range(0,2):
            init_capital, count = play_B(init_capital, count)
        #if init_capital < 0:
            #break

start()
