import numpy as np
import random
import TimeVariantGame as time
import util

class CapitalVariantGame(time.TimeVariantGame):

    def set_game(self):
        # for Game A:
        while(1):
            self.init_Game_A()
            if self.val_A < 0:
                break

        # for Game B:
        while(1):
            self.init_Game_B()
            other = CapitalVariantGame()
            other.M = self.M
            other.p1 = self.p1
            other.p1_win = self.p1_win
            other.p1_lose = self.p1_lose
            other.p = self.p2
            other.payoff_win = self.p2_win
            other.payoff_lose = self.p2_lose
            other.val_B1 = ((other.p1 * other.p1_win + (1.0 - other.p1) * other.p1_lose))
            other.val_A = ((other.p2 * other.p2_win + (1.0 - other.p2) * other.p2_lose))
            if other.game_is_losing():
                break
        
        if self.game_is_losing():
            self.set_game()

    def play_B(self):
        self.count += 1
        result_B = random.uniform(0,1)
        if self.capital % self.M == 0:
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

    def game_is_losing(self):
        if self.M == 1:
            return True

        #test if we can ever get to M from capital
        possible = False
        for i in range(self.M):
            if (self.capital + i*self.payoff_win) % self.M == 0:
                possible = True
                break
            if (self.capital + i*self.payoff_lose) % self.M == 0:
                possible = True
                break
        if not possible:
            return True

        try:
            state = np.zeros((self.M,self.M))
            state[0][self.p1_win%self.M] += self.p1
            state[0][self.p1_lose%self.M] += 1.0-self.p1
            for i in range(1,self.M):
                state[i][(i+self.payoff_win)%self.M] += self.p
                state[i][(i+self.payoff_lose)%self.M] += 1.0-self.p

            q = (state-np.eye(self.M))
            ones = np.ones(self.M)
            q = np.c_[q,ones]
            QTQ = np.dot(q, q.T)
            bQT = np.ones(self.M)
            sol = np.linalg.solve(QTQ,bQT)
            sol /= sum(sol)
            # print(sol)
            # print(self.val_B1*sol[0] + self.val_A *sum(sol[1:]))
            # print(state)

            return self.val_B1*sol[0] + self.val_A *sum(sol[1:]) <= 0.0
        except:
            #matrix is singular
            return True


    def start(self):
        self.set_game()
        self.count = 0
        initial_capital = self.capital
        print("M = %d" %self.M)
        while(self.count < 1000):
            if self.capital % self.M == 0:
                self.play_B()
            else:
                self.play_A()
            print("count = %d" %self.count)
            print("capital = %d" %self.capital)

        print("val_A = %f" %self.val_A)
        print("val_B = %f" %self.val_B)
        print("val_B1 = %f" %self.val_B1)
        print("val_B2 = %f" %self.val_B2)


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
            if self.capital % self.M == 0:
                self.play_B()
                f.write("%d," %self.count)
                f.write("%d\r\n" %self.capital)
            else:
                self.play_A()
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
    game = CapitalVariantGame()
    game.write("opt_dev.txt", "b_dev.txt", "a_dev.txt")
    util.plot("opt_dev.txt", "b_dev.txt", "a_dev.txt")


