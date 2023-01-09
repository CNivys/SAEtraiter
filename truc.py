import random
import pickle
import matplotlib.pyplot as plt

nb = int(input("Veuillez choisir le nombre de tirage : "))
n = int(input("Veuillez choisir une graine : "))
random.seed(n)
tab = []

#tirage
for i in range(nb):
    t = 0
    #print("\n")
    f = open("tirage n°{}".format(i+1), "wb")
    for i in range(5):
        t = int(round(random.uniform(1, 45)))
        pickle.dump(t, f)
        #print(t, end =" ")

#lecture des fichiers avec les tirages
for i in range(nb):
    f = open("tirage n°{}".format(i + 1), "rb")
    print("\n")
    for i in range(5):
        ti = pickle.load(f)
        tab.append(ti)
        print(ti, end=" ")

tab.sort()
print("\n")
print(tab)

#histogramme:

plt.hist(tab, bins=45 ,rwidth=0.8)  # Création de l'histogramme
plt.xlabel('Valeurs')
plt.xticks(range(0,45))
plt.ylabel('Nombres')
plt.title("Exemple d'histogramme simple")
plt.show()
