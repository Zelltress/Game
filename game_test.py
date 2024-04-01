import text as tx
import random

mng_event = 0
non_mng_event = 0
plot_event = 0


class user():

    @classmethod
    def __init__(self, chrch, army, ppl, wrld_authority):
        self.chrch = chrch
        self.army = army
        self.ppl = ppl
        self.wrld_authority = wrld_authority

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


def intro_scene():
    priority = ['user_1', 'user_2', 'user_3', 'user_4']

    print(tx.PRIORITY_1)
    user_1 = input(tx.USER)
    user_2 = input(tx.USER)
    user_3 = input(tx.USER)
    user_4 = input(tx.USER)

    random.shuffle(priority)

    random.randint(1,100)
    priority =

    print(tx.PRIORITY_2)


if __name__ == "__main__":
    while True:
        print(tx.GREETING)
        print(tx.PLOT_1)
        print(tx.PLOT_2)
        print(tx.GM_DSCRPTN_1)
        print(tx.GM_DSCRPTN_2)
        print(tx.GM_DSCRPTN_3)
        print(tx.START)
        intro_scene()
