import text as tx
import random

answer = ['да', 'нет']


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

    def dependence(self):
        rand_attr = random.choice(self.attrlist)
        attr_value = getattr(self, rand_attr)
        setattr(self, rand_attr, attr_value + 10)

    def display_stat(self):
        print(tx.STATISTIC.format(self.name, self.church, self.army, self.ppl))

    # def description(self):


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

    user_name_1 = input(tx.USER)
    '''user_name_2 = input(tx.USER)
    user_name_3 = input(tx.USER)
    user_name_4 = input(tx.USER)'''

    # priority = [user_name_1, user_name_2, user_name_3, user_name_4]
    # random.shuffle(priority)

    # print(tx.PRIORITY_2)
    # print(priority)

    user_1 = User(user_name_1, random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                  1, 1000)
    '''user_2 = User(user_name_2, random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                  1, 1000)
    user_3 = User(user_name_3, random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                  1, 1000)
    user_4 = User(user_name_4, random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                  1, 1000)'''

    user_1.display_stat()

    while User.count != 2:  # нужно разместить quarter
        print(user_name_1, "! ", tx.PLOT_3, sep='')

        print(tx.ARMY_SPRNG[0])
        user_wrd = input()
        i = random.randint(5, 15)
        if user_wrd.lower() == answer[0].lower():
            user_1.army = user_1.army + i
        else:
            user_1.army = user_1.army - i
        user_1.display_stat()

        print(tx.PLOT_4)

        print(tx.CHUCRH_SPRNG[0])
        user_wrd = input()
        i = random.randint(5, 15)
        if user_wrd.lower() == answer[0].lower():
            user_1.church = user_1.church + i
        else:
            user_1.church = user_1.church - i
        user_1.display_stat()
