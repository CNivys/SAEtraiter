import random
import pickle
import matplotlib.pyplot as plt

nb = int(input("Veuillez choisir le nombre de tirage : "))
n = int(input("Veuillez choisir une graine : "))
random.seed(n)
tab = []
tabVer = []
ti=[]

#tirage
for i in range(nb):
    t = 0
    #print("\n")
    t = random.sample(range(1, 46), 5)
    f = open("Tirage", "wb")
    for i in range(5):
        tv = t[i]
        tab.append(tv)
        pickle.dump(tv, f)

f = open("Tirage", "rb")
ti = pickle.load(f)
tab.append(ti)
print(ti, end=" ")

def fusion(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def fusion_sort(tab):
    if len(tab) < 2:
        return tab
    middle = len(tab) // 2
    left = fusion_sort(tab[:middle])
    right = fusion_sort(tab[middle:])
    return fusion(left, right)


tab = fusion_sort(tab)
print("\n")
print(tab)

#histogramme:

plt.hist(tab, bins=45, rwidth=0.8)  # Création de l'histogramme
plt.xlabel('Valeurs')
plt.xticks(range(0, 46))
plt.ylabel('Nombres')
plt.title("Histogrammes des tirages")
plt.show()

