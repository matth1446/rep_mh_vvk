from random import *

def testTrans(x,y,z):
    a = x+y
    b = y+z
    return a+z==x+b
    
def runAlea():
    x = random() * randint(0,10000000000)
    y = random() * randint(0,10000000000)
    z = random() * randint(0,10000000000)
    return testTrans(x,y,z)
    
def test(n):
    j = 0
    k = 0
    while k*100000 <n:
        for i in range(100000):
            if not runAlea():
                j = j+1
        k = k+1
        print("\nresultats partiels :\ntours :{}\nerreur : {}\ntaux : {}".format(k*100000,j,j/(k*100000)))
