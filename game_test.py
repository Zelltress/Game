# Case-study №5
# Developers: Ivanova A. Cherkashina D.

import text as tx
import random

answer = [tx.YES, tx.NO]


class User:

    def __init__(self, name, church, army, ppl, wrld_authority, treasury, count):
        self.name = name
        self.church = church
        self.army = army
        self.ppl = ppl
        self.wrld_authority = wrld_authority
        self.treasury = treasury
        self.count = count

    def check(self):
        if self.ppl < 0:
            print(tx.END[2])
            exit()
        elif self.church < 0:
            print(tx.END[0])
            exit()
        elif self.army < 0:
            print(tx.END[3])
            exit()
        elif self.treasury < 0:
            print(tx.END[4])
            exit()
        elif self.count >= 8:
            print(tx.END[5])
            exit()

    def display_stat(self):
        print('\n', tx.STATISTIC.format(self.name, self.church, self.army, self.ppl, self.treasury))


def intro_scene():
    print(tx.GREETING, '\n')
    print(tx.PLOT_1)
    print(tx.PLOT_2)
    print(tx.GM_DSCRPTN_1)
    print(tx.GM_DSCRPTN_2, '\n')
    print(tx.GM_DSCRPTN_3)

    print(tx.PRIORITY, '\n')


if __name__ == "__main__":
    intro_scene()

    user_name_1 = input(tx.USER)
    user_name_2 = input(tx.USER)

    user_1 = User(user_name_1, random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                  1, 1000, 0)
    user_2 = User(user_name_2, random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                  1, 1000, 0)

    print(user_1.display_stat(), '\n')
    print(user_2.display_stat(), '\n')

    print('\n', user_name_1, "!", '\n', tx.PLOT_3, sep='')

    print(tx.PEOPLE_SPRNG[0])
    user_wrd = input()
    i = random.randint(10, 25)
    j = random.randint(50, 100)
    if user_wrd.lower() == answer[0]:
        user_1.ppl += i
        user_1.treasury -= j
    else:
        user_1.ppl -= i
    user_1.count += 1
    user_1.display_stat()
    user_1.check()

    print(tx.TREASURY_SPRNG[1])
    user_wrd = input()
    i = random.randint(10, 25)
    j = random.randint(50, 100)
    if user_wrd.lower() == answer[0]:
        user_1.ppl += i
        user_1.treasury -= j
        user_1.wrld_authority = 2
    else:
        user_1.ppl -= i
    user_1.count += 1
    user_1.display_stat()
    user_1.check()

    if user_1.wrld_authority == 2:
        print('\n', user_name_2, "!", tx.PLOT_4[0], sep='')
    else:
        print('\n', user_name_2, "!", tx.PLOT_4[1], sep='')

    print(tx.ARMY_SPRNG[0])
    user_wrd = input()
    i = random.randint(10, 25)
    j = random.randint(50, 100)
    if user_wrd.lower() == answer[0]:
        user_2.army += i
        user_2.treasury -= j
    else:
        user_2.army -= i
    user_2.count += 1
    user_2.display_stat()
    user_2.check()

    print('\n', tx.CHUCRH_SPRNG[1])
    user_wrd = input()
    i = random.randint(10, 25)
    j = random.randint(50, 100)
    if user_wrd.lower() == answer[0]:
        user_2.church += i
        user_2.ppl -= i
    else:
        user_2.church -= i
        user_2.ppl += i
    user_2.count += 1
    user_2.display_stat()
    user_2.check()

    print(tx.PLOT_5)

    print(tx.CHURCH_SMMR[0])
    user_wrd = input()
    i = random.randint(10, 25)
    j = random.randint(50, 100)
    if user_wrd.lower() == answer[0]:
        user_1.ppl += i
        user_1.church += i
        user_1.treasury -= j
    else:
        user_1.ppl -= i
        user_1.church -= i
    user_1.count += 1
    user_1.display_stat()
    user_1.check()

    print(tx.ARMY_SMMR[0])
    user_wrd = input()
    i = random.randint(10, 25)
    j = random.randint(50, 100)
    if user_wrd.lower() == answer[0]:
        user_1.army += i
        user_1.treasury -= j
    else:
        user_1.army += i
    user_1.count += 1
    user_1.display_stat()
    user_1.check()

    print(tx.TREASURY_SMMR[0])
    user_wrd = input()
    i = random.randint(10, 25)
    j = random.randint(50, 100)
    if user_wrd.lower() == answer[0]:
        user_2.treasury += j
    else:
        user_2.treasury -= j
    user_2.count += 1
    user_2.display_stat()
    user_2.check()

    print(tx.PEOPLE_SMMR[1])
    user_wrd = input()
    i = random.randint(10, 25)
    j = random.randint(50, 1000)
    if user_wrd.lower() == answer[0]:
        user_2.ppl += i
        user_2.treasury -= j
        user_2.wrld_authority = 2
    else:
        user_2.ppl -= i
    user_2.count += 1
    user_2.display_stat()
    user_2.check()

    print(tx.TREASURY_FALL[0])
    user_wrd = input()
    i = random.randint(10, 25)
    j = random.randint(50, 100)
    if user_wrd.lower() == answer[0]:
        user_1.ppl += i
        user_1.treasury -= j
    else:
        user_1.ppl -= i
    user_1.count += 1
    user_1.display_stat()
    user_1.check()

    print(tx.CHURCH_FALL[0])
    user_wrd = input()
    i = random.randint(10, 12)
    j = random.randint(50, 100)
    if user_wrd.lower() == answer[0]:
        user_1.church += i
        user_1.treasury -= j
    if user_1.wrld_authority == 2:
        user_1.ppl += i
    else:
        user_1.church -= i
    user_1.count += 1
    user_1.display_stat()
    user_1.check()

    print(tx.TREASURY_FALL[1])
    user_wrd = input()
    i = random.randint(10, 25)
    j = random.randint(50, 100)
    if user_wrd.lower() == answer[0]:
        user_2.treasury += j
    else:
        user_2.treasury -= j
    user_2.count += 1
    user_2.display_stat()
    user_2.check()

    print(tx.PEOPLE_FALL[0])
    user_wrd = input()
    i = random.randint(10, 25)
    j = random.randint(50, 100)
    if user_wrd.lower() == answer[0].lower():
        user_2.ppl += i
        user_2.treasury -= j
    else:
        user_2.ppl -= i
    user_2.count += 1
    user_2.display_stat()
    user_2.check()

    if user_1.church <= 10:
        print(tx.CHURCH_WNTR[1])
        user_wrd = input()
        i = random.randint(10, 25)
        j = random.randint(50, 100)
    if user_wrd.lower() == answer[0]:
        user_1.ppl -= i
        user_1.army -= i
        user_1.treasury -= j
        user_1.church += 2 * i
    elif user_1.wrld_authority == 1:
        print(tx.END[0])
    else:
        print(tx.END[1])
    user_1.count += 1
    user_1.display_stat()
    user_1.check()

    print(tx.ARMY_WNTR[1])
    user_wrd = input()
    i = random.randint(10, 25)
    j = random.randint(50, 100)
    if user_wrd.lower() == answer[0]:
        user_2.treasury += j
        user_2.army += i
    else:
        user_2.army -= i
    user_2.count += 1
    user_2.display_stat()
    user_2.check()

    print(tx.PEOPLE_WNTR[0])
    user_wrd = input()
    i = random.randint(10, 25)
    j = random.randint(50, 100)
    if user_wrd.lower() == answer[0].lower():
        user_2.ppl -= 2 * i
        user_2.treasury -= 2 * j
        user_2.wrld_authority = 2
    else:
        user_2.ppl -= i
    user_2.count += 1
    user_2.display_stat()
    user_2.check()



