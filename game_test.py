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
    count = 0
    intro_scene()

    user_name_1 = input(tx.USER)
    user_name_2 = input(tx.USER)

    user_1 = User(user_name_1, random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                  1, 1000)
    user_2 = User(user_name_2, random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                  1, 1000)

    print(user_1.display_stat(), '\n')
    print(user_2.display_stat(), '\n')

    while count < 3 or (user_1.army or user_1.ppl or user_1.church or user_1.treasury) != 0:

        print('\n', user_name_1, "! ", '\n', tx.PLOT_3, sep='')

        print(tx.PEOPLE_SPRNG[0])
        user_wrd = input()
        i = random.randint(10, 125)
        j = random.randint(50, 100)
        if user_wrd.lower() == answer[0]:
            user_1.ppl += i
            user_1.treasury -= j
        else:
            user_1.ppl -= i
        user_1.display_stat()

        print('\n', tx.TREASURY_SPRNG[1])
        user_wrd = input()
        i = random.randint(10, 25)
        j = random.randint(50, 100)
        if user_wrd.lower() == answer[0]:
            user_1.ppl += i
            user_1.treasury -= j
            user_1.wrld_authority = 2
        else:
            user_1.ppl -= i
        user_1.display_stat()

        if user_1.wrld_authority == 2:
            print('\n', user_name_2, "! ", tx.PLOT_4[0], sep='')
        else:
            print('\n', user_name_2, "! ", tx.PLOT_4[1], sep='')

        print('\n', tx.ARMY_SPRNG[0])
        user_wrd = input()
        i = random.randint(10, 25)
        j = random.randint(50, 100)
        if user_wrd.lower() == answer[0]:
            user_2.army += i
            user_2.treasury -= j
        else:
            user_2.army -= i
        user_2.display_stat()

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
        user_2.display_stat()

        count += 1

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
        user_1.display_stat()

        print('\n', tx.ARMY_SMMR[0])
        user_wrd = input()
        i = random.randint(10, 25)
        j = random.randint(50, 100)
        if user_wrd.lower() == answer[0]:
            user_1.army += i
            user_1.treasury -= j
        else:
            user_1.army += i
        user_1.display_stat()

        print('\n', tx.TREASURY_SMMR[0])
        user_wrd = input()
        i = random.randint(10, 25)
        j = random.randint(50, 100)
        if user_wrd.lower() == answer[0]:
            user_2.treasury += j
        else:
            user_2.treasury -= j
        user_2.display_stat()

        print('\n', tx.PEOPLE_SMMR[1])
        user_wrd = input()
        i = random.randint(10, 25)
        j = random.randint(50, 1000)
        if user_wrd.lower() == answer[0]:
            user_2.ppl += i
            user_2.treasury -= j
            user_2.wrld_authority = 2
        else:
            user_2.ppl -= i
        user_2.display_stat()

        count += 1

        print(tx.TREASURY_FALL[0])
        user_wrd = input()
        i = random.randint(10, 25)
        j = random.randint(50, 100)
        if user_wrd.lower() == answer[0]:
            user_1.ppl += i
            user_1.treasury -= j
        else:
            user_1.ppl -= i
        user_1.display_stat()

        print('\n', tx.CHURCH_FALL[0])
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
        user_1.display_stat()

        print('\n', tx.TREASURY_FALL[1])
        user_wrd = input()
        i = random.randint(10, 25)
        j = random.randint(50, 100)
        if user_wrd.lower() == answer[0]:
            user_2.treasury += j
        else:
            user_2.treasury -= j
        user_2.display_stat()

        print('\n', tx.PEOPLE_FALL[0])
        user_wrd = input()
        i = random.randint(10, 25)
        j = random.randint(50, 100)
        if user_wrd.lower() == answer[0].lower():
            user_2.ppl += i
            user_2.treasury -= j
        else:
            user_2.ppl -= i
        user_2.display_stat()

        count += 1

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
                break
            else:
                print(tx.END[1])
                break
            user_1.display_stat()

        print('\n', tx.ARMY_WNTR[1])
        user_wrd = input()
        i = random.randint(10, 25)
        j = random.randint(50, 100)
        if user_wrd.lower() == answer[0]:
            user_2.treasury += j
            user_2.army += i
        else:
            user_2.army -= i
        user_2.display_stat()

        print('\n', tx.PEOPLE_WNTR[0])
        user_wrd = input()
        i = random.randint(10, 25)
        j = random.randint(50, 100)
        if user_wrd.lower() == answer[0].lower():
            user_2.ppl -= 2 * i
            user_2.treasury -= 2 * j
            user_2.wrld_authority = 2
        else:
            user_2.ppl -= i
        user_2.display_stat()

        count += 1
