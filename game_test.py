import text as tx
import random


def intro_scene():
    priority = ['user_1', 'user_2', 'user_3', 'user_4']

    print(tx.PRIORITY_1)
    user_1 = input(tx.USER)
    user_2 = input(tx.USER)
    user_3 = input(tx.USER)
    user_4 = input(tx.USER)

    random.shuffle(priority)

    print(tx.PRIORITY_2)

def ounter_quarter():




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
