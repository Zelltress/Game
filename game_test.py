import text as tx
import random

mng_events = [1, 2, 3, 4, 5, 6, 7, 8, 9]
non_mng_events = [1, 2, 3, 4, 5, 6]
plot_event = [1, 2, 3]

'''
class Quiz:
    def __init__(self, mng_events, non_mng_events, plot_events):
        self.mng_events = mng_events
        self.non_mng_events = non_mng_events
        self.plot_events = plot_events
'''
def quiz():
    if count ==



class User:

    def __init__(self, name, church, army, ppl, wrld_authority, treasury):
        self.name = name
        self.church = church
        self.army = army
        self.ppl = ppl
        self.wrld_authority = wrld_authority
        self.treasury = treasury

    def display_stat(self):
        print(tx.STATISTIC.format(self.name, self.church, self.army, self.ppl))

    def quarter(self):  # нужно доработать
        mng_event = 0
        non_mng_event = 0
        plot_event = 0
        global count = 5
        while self == User:  # еще нужно проверить на работоспособность
            if mng_event == 1 and non_mng_event == 1 and plot_event == 1:
                count += 1
                mng_event = 0
                non_mng_event = 0
                plot_event = 0

        print(tx.QUARTER, count * 3)
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
    intro_scene()

    while True:  # нужно разместить quarter

        user_name_1 = input(tx.USER)
        user_name_2 = input(tx.USER)
        user_name_3 = input(tx.USER)
        user_name_4 = input(tx.USER)

        priority = [user_name_1, user_name_2, user_name_3, user_name_4]
        random.shuffle(priority)

        print(tx.PRIORITY_2)
        print(priority)

        user_1 = User(user_name_1, 20, 60, 45, 1, 1000)
        user_2 = User(user_name_2, 20, 60, 45, 1, 1000)
        user_3 = User(user_name_3, 20, 60, 45, 1, 1000)
        user_4 = User(user_name_4, 20, 60, 45, 1, 1000)
