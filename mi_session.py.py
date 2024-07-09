# Exercice 2: 
def build_list() :
#creer une nouvelle liste vide pour les etudiants
    list_etudiants = []
#ajouter la boucle qui termine quand l'utilisateur entre le nombre 0 
    while True :
#demander au utilisateur d'entrer les noms des etudiants
        nom = input("veuillez saisir le nom de l'étudiant :")
# Si l'utilisateur entre le nombre 0 ca stop de lui demander encore
        if nom == '0':
            break
# Demande à l'utilisateur d'entrer l'âge de l'étudiant
        age = int(input("veuillez saisir l'age de l'etudiant que t'as entre son nom : "))
#former le nom et l'age en (nom, age)
        list_etudiants.append((nom, age))
#Demander a l'utilisateur si il veut entrer d'autre etudiant
        continuer = input("ajouter un autre etudiant ? (0/1):")
        if continuer == '0':
            break
#retourner la liste termine des etudiants 
    return list_etudiants
liste_classe = build_list()
print("la liste demande est :", liste_classe)
#apres entrer les noms et l'age des etudiants on clique sur 0 et ca affiche 
#la liste demande est : [('viny', 34), ('ryan', 43), ('tity', 31), ('antony', 27), ('calvin', 39), ('lilian', 27)]


# Exercice 3: 

#question1
def switch(liste, i, j):
#cette commande pour changer les positions des deux elements d'une liste
    liste[i], liste[j] = liste[j], liste[i]

#question2
def bubbleSort(liste):
# trier la liste en ordre alphabétique 
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j][0] > liste[j+1][0]:
                switch(liste, j, j+1)
#Afficher la liste après les changements 
        print(f"Itération {i}: {liste}")

#question3
def selectionSort(liste):
#trier la liste en ordre croissant de l'age
    n = len(liste)
    for i in range(n):
#trouver le plus petit element
        min_element = i
        for j in range(i+1, n):
#Comparaison des âges des étudiants
            if liste[j][1] < liste[min_element][1]:
                min_element = j
#placer les elements a leurs place 
        switch(liste, i, min_element)
#afficher la liste finale apres les changements
        print(f"Itération {i + 1}: {liste}")


