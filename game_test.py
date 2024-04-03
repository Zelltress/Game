import text as tx
import random

mng_events = [1, 2, 3, 4, 5, 6, 7, 8, 9]
non_mng_events = [1, 2, 3, 4, 5, 6]
plot_event = [1, 2, 3]


class User:
    count = 0

    def __init__(self, name, church, army, ppl, wrld_authority, treasury):
        self.name = name
        self.church = church
        self.army = army
        self.ppl = ppl
        self.wrld_authority = wrld_authority
        self.treasury = treasury
        self.attrlist = ['church', 'army', 'ppl']
        User.count += 1
        self.quiz()

    def dependence(self):
        rand_attr = random.choice(self.attrlist)
        attr_value = getattr(self, rand_attr)
        setattr(self, rand_attr, attr_value + 10)

    def display_stat(self):
        print(tx.STATISTIC.format(self.name, self.church, self.army, self.ppl))


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

    while User.count != 40:  # нужно разместить quarter

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
