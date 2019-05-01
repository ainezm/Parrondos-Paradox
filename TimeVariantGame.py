import numpy as np
import random
import util

class TimeVariantGame:
    def __init__(self):

        self.p = 0.0
        self.p1 = 0.0
        self.p2 = 0.0
        self.payoff_win = 0
        self.payoff_lose = 0
        self.p1_win = 0
        self.p2_win = 0
        self.p1_lose = 0
        self.p2_lose = 0
        self.M = 0
        self.val_A = 0.0
        self.val_B = 0.0
        self.val_B1 = 0.0
        self.val_B2 = 0.0
        self.capital = random.randint(1,10)
        self.count = 0


    def init_Game_A(self):
        self.p = random.uniform(0,1)
        self.payoff_win = random.randint(-10,0)
        self.payoff_lose = random.randint(-10,0)
        self.val_A = ((self.p * self.payoff_win) + ((1.0 - self.p) * self.payoff_lose))


    def init_Game_B(self):
        self.p1 = random.uniform(0,1)
        self.p2 = random.uniform(0,1)
        self.p1_win = random.randint(0,10)
        self.p2_win = random.randint(-20,-10)
        self.p1_lose = random.randint(0,10)
        self.p2_lose = random.randint(-20,-10)
        self.M = random.randint(2,5)
        self.val_B1 = ((self.p1 * self.p1_win + (1.0 - self.p1) * self.p1_lose))
        self.val_B2 = ((self.p2 * self.p2_win + (1.0 - self.p2) * self.p2_lose))
        self.val_B = ((1.0/self.M)*self.val_B1 + (self.M-1.0)/self.M * self.val_B2)

    def game_is_losing(self):
        return (self.M-1) * self.val_A + self.val_B1 <= 0

    def set_game(self):
        # for Game A:
        while(1):
            self.init_Game_A()
            if self.val_A < 0:
                break

        # for Game B:
        while(1):
            self.init_Game_B()
            if self.val_B < 0:  
                break
        
        if self.game_is_losing():
            self.set_game()

    def play_A(self):
        self.count += 1
        result_A = random.uniform(0,1)
        if result_A <= self.p:
            self.capital += self.payoff_win
        else:
            self.capital += self.payoff_lose
        print("count = %d" %self.count)
        print("capital = %d" %self.capital)


    def play_B(self):
        self.count += 1
        result_B = random.uniform(0,1)
        if self.count % self.M == 0:
            if result_B <= self.p1:
                self.capital += self.p1_win
            else:
                self.capital += self.p1_lose
        else:
            print("Never reach!")
            if result_B <= self.p2:
                self.capital += self.p2_win
            else:
                self.capital += self.p2_lose 
        print("count = %d" %self.count)
        print("capital = %d" %self.capital)


    def start(self):
        self.set_game()
        self.count = 0
        print("val_A = %f" %self.val_A)
        print("val_B = %f" %self.val_B)
        print("val_B1 = %f" %self.val_B1)
        print("val_B2 = %f" %self.val_B2)
        print("initial capital = %d" %self.capital)
        print("M = %d" %self.M)
        while(self.count < 1000):
            for i in range(self.M-1):
                self.play_A()
                #if init_capital < 0:
                    #break
            self.play_B()
            #if init_capital < 0:
                #break
    def write(self, opt_name, b_name, a_name):
        f = open(opt_name,'w')
        self.set_game()
        self.count = 0
        print("val_A = %f" %self.val_A)
        print("val_B = %f" %self.val_B)
        print("val_B1 = %f" %self.val_B1)
        print("val_B2 = %f" %self.val_B2)
        print("initial capital = %d" %self.capital)
        initial_capital = self.capital
        print("M = %d" %self.M)
        while(self.count < 1000):
            for i in range(self.M-1):
                self.play_A()
                f.write("%d," %self.count)
                f.write("%d\r\n" %self.capital)

            self.play_B()
            f.write("%d," %self.count)
            f.write("%d\r\n" %self.capital)

        self.capital = initial_capital
        self.count = 0
        f.close()
        b = open(b_name,'w')
        print("B")
        while(self.count < 1000):
            self.play_B()
            b.write("%d," %self.count)
            b.write("%d\r\n" %self.capital)

        self.capital = initial_capital
        self.count = 0
        b.close()
        a = open(a_name,'w')
        while(self.count < 1000):
            self.play_A()
            a.write("%d," %self.count)
            a.write("%d\r\n" %self.capital)
        f.close()
        print("A")

if __name__ == "__main__":
    game = TimeVariantGame()
    game.write("opt_time.txt", "b_time.txt", "a_time.txt")
    util.plot("opt_time.txt", "b_time.txt", "a_time.txt")
