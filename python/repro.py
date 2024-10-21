from random import *


def testTrans(x, y, z):
    a = x + y
    b = y + z
    return a + z == x + b


def runAlea():
    x = random() * randint(0, 10000000000)
    y = random() * randint(0, 10000000000)
    z = random() * randint(0, 10000000000)
    return testTrans(x, y, z)


def test(n):
    j = 0
    k = 0
    for i in range(n):
        if not runAlea():
            j = j + 1
        if i % 100000 == 0 and i > 0:
            print("\nresultats partiels :\ntours :{}\nerreur : {}\ntaux : {}".format(i, j, j / i))
    return j / n


if __name__ == "__main__":
    print(round((1-test(100))*100,2)) #for standard file : number between 0 and 100 approximate to 2 numbers after the coma
    # taux = []
    # for i in range(100):
    #     res = test(100)
    #     taux.append(res)
    # print("x+(y+z) == (x+y)+z approximately {}% of cases".format((1 - res) * 100))
    # print("Taux d'erreur :", taux)
    # print("Taux d'erreur max :", max(taux))
    # print("Taux d'erreur min :", min(taux))
