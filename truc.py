import numpy.random
import pickle
import matplotlib.pyplot as plt

nb = int(input("Veuillez choisir le nombre de tirage : "))
n = int(input("Veuillez choisir une graine : "))
numpy.random.seed(n)
tab = []
tabVer=[]

#tirage
for i in range(nb):
    t = 0
    #print("\n")
    f = open("tirage n°{}".format(i+1), "wb")
    for i in range(5):
        t = int(round(numpy.random.uniform(1, 45)))
        tabVer.append(t)
        if t not in tabVer:
            pickle.dump(t, f)
        else:
            t = int(round(numpy.random.uniform(1, 45)))
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

def recherche_dichotomique(element, tab):
    a = 0
    b = len(tab)-1
    m = (a+b)//2
    while a < b :
        if tab[m] == element:
            return m
        elif tab[m] > element:
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    return a

tab = fusion_sort(tab)
print("\n")
print(tab)
print(recherche_dichotomique(2, tab))

#histogramme:

plt.hist(tab, bins=45, rwidth=0.8)  # Création de l'histogramme
plt.xlabel('Valeurs')
plt.xticks(range(0,46))
plt.ylabel('Nombres')
plt.title("Histogrammes des tirages")
plt.show()

