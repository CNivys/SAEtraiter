import random
nb = int(input("Veuillez choisir le nombre de tirage : "))
n = int(input("Vueillez choisir une seed : "))
random.seed(n)

for i in range(nb):
    print("\n")
    random.seed(n)
    for i in range(5):
        print(round(random.uniform(1,45)), end =" ")