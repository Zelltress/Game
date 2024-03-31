import text as tx
import random

'''
def introScene():
    priority = ['user_1', 'user_2', 'user_3', 'user_4']
    users = {}

    print(tx.PRIORITY)
    user_1 = input(tx.USER)
    user_2 = input(tx.USER)
    user_3 = input(tx.USER)
    user_4 = input(tx.USER)
'''
priority = ['user_1', 'user_2', 'user_3', 'user_4']
pr = [1, 2, 3, 4]
users = {}

random.shuffle(pr)
print(pr)
for i in range(1, 4):
    priority[i] = priority[pr[i]]
print(priority)

'''
if __name__ == "__main__":
    while True:
        print(tx.GREETING)
        print(tx.PLOT_1)
        print(tx.PLOT_2)
        print(tx.GM_DSCRPTN_1)
        print(tx.GM_DSCRPTN_2)
        print(tx.GM_DSCRPTN_3)
        print(tx.START)
        introScene()
'''
