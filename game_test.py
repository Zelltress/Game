import text as tx
import random


class User:

    # @classmethod
    def __init__(self, name, chrch, army, ppl, wrld_authority):
        self.name = name
        self.chrch = chrch
        self.army = army
        self.ppl = ppl
        self.wrld_authority = wrld_authority

    def display_stat(self):
        print(tx.STATISTIC.format(self.name, self.chrch, self.army, self.ppl))

    # @staticmethod
    def сounter_quarter(self):
        mng_event = 0
        non_mng_event = 0
        plot_event = 0
        track = 0
        count = 0
        while self == User:
            if mng_event == 1 and non_mng_event == 1 and plot_event == 1:
                count += 1
                mng_event = 0
                non_mng_event = 0
                plot_event = 0
        return count


def intro_scene():
    print(tx.GREETING)
    print(tx.PLOT_1)
    print(tx.PLOT_2)
    print(tx.GM_DSCRPTN_1)
    print(tx.GM_DSCRPTN_2)
    print(tx.GM_DSCRPTN_3)

    print(tx.PRIORITY_1)


if __name__ == "__main__":
    # while True:

    intro_scene()

    user_name_1 = input(tx.USER)
    user_name_2 = input(tx.USER)
    user_name_3 = input(tx.USER)
    user_name_4 = input(tx.USER)

    priority = [user_name_1, user_name_2, user_name_3, user_name_4]
    random.shuffle(priority)

    print(tx.PRIORITY_2)
    print(priority)

    user_1 = User(user_name_1, 20, 60, 45, 1)
    user_2 = User(user_name_2, 20, 60, 45, 1)
    user_3 = User(user_name_3, 20, 60, 45, 1)
    user_4 = User(user_name_4, 20, 60, 45, 1)

    user_1.display_stat()
    user_1.сounter_quarter

