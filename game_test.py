import text as tx
import random

answer = ['да', 'нет']


class User:

    def __init__(self, name, church, army, ppl, wrld_authority, treasury):
        self.name = name
        self.church = church
        self.army = army
        self.ppl = ppl
        self.wrld_authority = wrld_authority
        self.treasury = treasury
        self.attrlist = ['church', 'army', 'ppl']

    def dependence(self):
        rand_attr = random.choice(self.attrlist)
        attr_value = getattr(self, rand_attr)
        setattr(self, rand_attr, attr_value + 10)

    def display_stat(self):
        print(tx.STATISTIC.format(self.name, self.church, self.army, self.ppl, self.treasury))

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
    count = 0
    intro_scene()

    user_name_1 = input(tx.USER)
    user_name_2 = input(tx.USER)
    user_name_3 = input(tx.USER)
    user_name_4 = input(tx.USER)

    # priority = [user_name_1, user_name_2, user_name_3, user_name_4]
    # random.shuffle(priority)

    # print(tx.PRIORITY_2)
    # print(priority)

    user_1 = User(user_name_1, random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                  1, 1000)
    user_2 = User(user_name_2, random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                  1, 1000)
    user_3 = User(user_name_3, random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                  1, 1000)
    user_4 = User(user_name_4, random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                  1, 1000)

    user_1.display_stat()

    while count < 10 or (user_1.army or user_1.ppl or user_1.church or user_1.treasury) != 0:

        print('\n',user_name_1, "! ",'\n', tx.PLOT_3, sep='')

        print(random.choice(tx.PEOPLE_SPRNG))
        user_wrd = input()
        i = random.randint(5, 15)
        j = random.randint(20, 50)
        if user_wrd.lower() == answer[0].lower():
            user_1.ppl = user_1.ppl + i
            user_1.treasury = user_1.treasury - j
        else:
            user_1.ppl = user_1.ppl - i
        user_1.display_stat()


        print('\n', tx.TREASURY_SPRNG[1])
        user_wrd = input()
        i = random.randint(5, 15)
        j = random.randint(20, 50)
        if user_wrd.lower() == answer[0].lower():
            user_1.ppl = user_1.ppl + i
            user_1.treasury = user_1.treasury - j
            user_1.wrld_authority = 2
        else:
            user_1.ppl = user_1.ppl - i
        user_1.display_stat()


        if user_1.wrld_authority == 2:
            print('\n',user_name_2, "! ",'\n', tx.PLOT_4[0], sep='')
        else:
            print('\n',user_name_2, "! ",'\n', tx.PLOT_4[1], sep='')

        print('\n',random.choice(tx.ARMY_SPRNG))
        user_wrd = input()
        i = random.randint(5, 15)
        j = random.randint(20, 50)
        if user_wrd.lower() == answer[0].lower():
            user_2.army = user_2.army + i
            user_2.treasury = user_2.treasury - j
        else:
            user_2.army = user_2.army - i
        user_2.display_stat()

        print('\n',random.choice(tx.CHUCRH_SPRNG))
        user_wrd = input()
        i = random.randint(5, 15)
        j = random.randint(20, 50)
        if user_wrd.lower() == answer[0].lower():
            user_2.church = user_2.church + i
            user_2.treasury = user_2.treasury - j
        else:
            user_2.church = user_2.church - i
        user_2.display_stat()

        print('\n',random.choice(tx.PEOPLE_SPRNG))
        user_wrd = input()
        i = random.randint(5, 15)
        j = random.randint(20, 50)
        if user_wrd.lower() == answer[0].lower():
            user_2.ppl = user_2.ppl + i
            user_2.treasury = user_2.treasury - j
        else:
            user_2.ppl = user_2.ppl - i
        user_2.display_stat()
