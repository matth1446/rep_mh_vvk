import random

# operation1 : première opération qui sera calculée (permet de manipuler le nombre d'opérandes, l'opérande qui sera testé, etc.)
# operation2 : deuxième opération qui sera calculée
# repetitions : nombre de répétition de l'expérience
# range_random : les nombres aléatoires seront générés dans la range [0, range_random]
# floating_nbs : nombre de chiffres après la virgule
# random_gen : méthode pour générer le random

def generateRandomWithStrategy(range_random, floating_nbs,random_strat):
    nb = 0
    if random_strat == 0:
        nb = random.random()*random.randint(0,range_random)
    if random_strat == 1:
        nb = 0.1 * random.randint(0,range_random*10)
    if random_strat == 2:
        nb = random.random()*range_random
    if (floating_nbs != 0):
        nb = round(nb,floating_nbs)
    return nb

def check_property(operation1, operation2, repetitions, range_random, floating_nbs,random_strat):
    correct_count = 0
    for _ in range(repetitions):
        a = generateRandomWithStrategy(range_random, floating_nbs,random_strat)
        b = generateRandomWithStrategy(range_random, floating_nbs, random_strat)
        c = generateRandomWithStrategy(range_random, floating_nbs, random_strat)
        w = generateRandomWithStrategy(range_random, floating_nbs, random_strat)
        x = generateRandomWithStrategy(range_random, floating_nbs, random_strat)
        y = generateRandomWithStrategy(range_random, floating_nbs, random_strat)
        z = generateRandomWithStrategy(range_random, floating_nbs, random_strat)
        # print(operation1, operation2, repetitions, range_random, floating_nbs,random_strat)
        # print(a, b, c, w, x, y, z)

        # Dynamically evaluate the operations
        result1 = eval(operation1)
        result2 = eval(operation2)

        if result1 == result2:
            correct_count += 1

    return correct_count/repetitions

# Define possible combinations of operations and repetition counts
operations = [
    {"operation1": "(x + y) + z", "operation2": "x + (y + z)"},  # Associativity (addition)
    {"operation1": "x + y", "operation2": "y + x"},              # Commutativity (addition)
    {"operation1": "(x * y) * z", "operation2": "x * (y * z)"},  # Associativity (multiplication)
    {"operation1": "x * y", "operation2": "y * x"},              # Commutativity (multiplication)
    {"operation1": "x - (y - z)", "operation2": "(x - y) - z"},  # Associativity (subtraction)
    {"operation1": "(x / y) / z", "operation2": "x / (y / z)"},  # Associativity (division)
    {"operation1": "x * (y / z)", "operation2": "(x * y) / z"},  # Combination of operations
    {"operation1": "((x + y) + z) + w", "operation2": "(x + (y + z)) + w"},  # Addition with 4 operands
    {"operation1": "(x * (y + z))", "operation2": "(x * y) + (x * z)"},  # Distributivity (multiplication over addition)
    {"operation1": "(x + y) * (z + w)", "operation2": "x * z + x * w + y * z + y * w"},  # Distribution over multiple terms
    {"operation1": "x ** (y ** z)", "operation2": "(x ** y) ** z"},  # Power associativity
    {"operation1": "(x - y) * (z + w)", "operation2": "(x * z - y * w)"},  # Combination of addition and subtraction
    {"operation1": "((x * y) / z) + ((a * b) / c)", "operation2": "(x / z) * (y + (a / c) * b)"},  # Combination of division and multiplication
]


# Define different repetition counts
#repetitions_list = [10, 100, 1000, 10000]
repetitions_list = [1, 10, 100, 1000, 10000]

# Define different ranges
range_random = [1, 3, 5, 10, 100, 10000, 1000000]

# Define floating numbers
floating_number = [0,1,2,5,50]

# Define strategy to generate random
random_strategy = [0,1,2]

file = open("output1.csv", "w")
file.write("idExperiment;op1;op2;repetitions;randomRange;floatingNumbers;randomStrategy;result\n")

i = 0
# Loop through all combinations of operations and repetitions
for op in operations:
    print(op)
    for reps in repetitions_list:
        for ran in range_random:
            for flo in floating_number:
                for strat in random_strategy:
                    try:
                        #print(f"\nChecking {op['operation1']} vs {op['operation2']} with {reps} repetitions:")
                        file.write(";".join([str(i),op['operation1'],op['operation2'], str(reps),str(ran),str(flo),str(strat),str(check_property(op['operation1'], op['operation2'], reps,ran,flo,strat))])+"\n")
                    except ZeroDivisionError:
                        pass
                        #file.write(";".join([str(i), op['operation1'], op['operation2'], str(reps), str(ran), str(flo), str(strat),"ZeroDivisionError"]) + "\n")
                    except OverflowError:
                        pass
                        #file.write(";".join([str(i), op['operation1'], op['operation2'], str(reps), str(ran), str(flo), str(strat),"OverflowError"]) + "\n")
                    finally:
                        i = i+1
file.close()