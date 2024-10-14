from math import exp

def banking_year(sum,years):
    for i in range(years):
        sum = sum - 1
        sum = sum * (i+1)
    return sum -1

if __name__ == "__main__" : 
    years = 50
    print("A la fin des {} ans, il reste {}€".format(years,banking_year(exp(1),years)))