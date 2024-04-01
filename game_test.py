import text as tx
import random

mng_event = 0
non_mng_event = 0
plot_event = 0



def user(chrch, army, ppl, wrld_authority):

    chrch = random.randint(1, 100)
    army = random.randint(1, 100)
    ppl = random.randint(1, 100)
    wrld_authority = 1

'''
class user():

    @classmethod
    def __init__(self, chrch, army, ppl, wrld_authority):
        self.chrch = chrch
            random.randint(1, 100))
        self.army = random.randint(1, 100)
        self.ppl = random.randint(1, 100)
        self.wrld_authority = 1

    @staticmethod
    def сounter_quarter():
        global mng_event, non_mng_event, plot_event
        track = 0
        count = 0
        while track == user:
            if mng_event == 1 and non_mng_event == 1 and plot_event == 1:
                count += 1
                mng_event = 0
                non_mng_event = 0
                plot_event = 0
'''

def intro_scene():
    print(tx.PRIORITY_1)
    user_name_1 = input(tx.USER)
    user_name_2 = input(tx.USER)
    user_name_3 = input(tx.USER)
    user_name_4 = input(tx.USER)

    user_1 = user()

    priority = ['user_name_1', 'user_name_2', 'user_name_3', 'user_name_4']
    random.shuffle(priority)

    print(tx.PRIORITY_2)
    print(priority)


if __name__ == "__main__":
    while True:
        print(tx.GREETING)
        print(tx.PLOT_1)
        print(tx.PLOT_2)
        print(tx.GM_DSCRPTN_1)
        print(tx.GM_DSCRPTN_2)
        print(tx.GM_DSCRPTN_3)
        print(tx.START)
        user()
        intro_scene()
