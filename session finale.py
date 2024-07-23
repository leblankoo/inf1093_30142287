#!/usr/bin/env python
# coding: utf-8

# In[5]:


#figure 1 question 2 :
def quicksort(liste) :
    if len(liste) <= 1:
        return liste
    pivot = liste.pop()
    
    petit = []
    grand = []
    
    for nombre in liste : 
#ici on compare les ages des etudiants de la liste :
        if nombre[1] < pivot [1]: 
            petit.append(nombre)
        else :
            grand.append(nombre)
    return quicksort(petit) + [pivot] + quicksort(grand)
#definir la liste des etudiants :
list = [("Viny",34 ), ("Ryan",43 ), ("Tity",31 ), ("Antony",27 ),("Calvin",39 ),("Lilian",27 ),("Merlin",19 ),("Rachy",25 )]
#afficher la liste finale :
print(quicksort(list))


# In[10]:


#exercice 2 question 2 :
def search(arr, name, low, high):
# Si la recherche est toujours valide
    if high >= low:
# Calculer le nombre milieu
        mid = (high + low) // 2  
        
# Si le nom a l'indice milieu est qu'on cherche
        if arr[mid][0] == name:
            return arr[mid][1]
        
# Si le nom a l'indice milieu est supérieur au nom au'on cherche
        elif arr[mid][0] > name:
# Rechercher dans la liste gauche
            return search(arr, name, low, mid - 1)
        
# Si le nom a l'indice milieu est inferieur au nom au'on cherche
        else:
            return search(arr, name, mid + 1, high) 
    
    else:
# Retourner None si le nom n'est pas trouvé
        return None  

def searchByName(name):
    students = list = [("Viny",34 ), ("Ryan",43 ), ("Tity",31 ), ("Antony",27 ),("Calvin",39 ),("Lilian",27 ),("Merlin",19 ),("Rachy",25 )]
    students.sort()  # Trier la liste par ordre alphabétique des noms
# lancer la recherche dichotomique
    return search(students, name, 0, len(students) - 1)  


print(searchByName("Viny"))  # son age est 23
print(searchByName("Lilian"))  # son age est 27


# In[ ]:


#Exercice3 question 1 :
def printNames(list):
    for chaque_student in list:
#pour chaque couple de la liste on choisis le premier element qui est 0 :
        print("les noms des etudiants de cette listes sont :",chaque_student[0])
#on definis la liste des etudiant
list = [("Viny",34 ), ("Ryan",43 ), ("Tity",31 ), ("Antony",27 ),("Calvin",39 ),("Lilian",27 ),("Merlin",19 ),("Rachy",25 )]
printNames(list)


# In[12]:


def printRecNames(list, n=0):
    if n < len(list):
        print(list[n][0])
        printRecNames(list, n + 1)

list = [("Viny",34 ), ("Ryan",43 ), ("Tity",31 ), ("Antony",27 ),("Calvin",39 ),("Lilian",27 ),("Merlin",19 ),("Rachy",25 )]
printRecNames(list)


# In[ ]:




