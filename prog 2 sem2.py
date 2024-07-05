#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os

def listing_directory(directory_path):
    file_list = []
    for item in os.listdir(directory_path):  
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            file_name, ext = os.path.splitext(item)
            size = os.path.getsize(item_path) / (1024 * 1024)  
            file_list.append((file_name, ext, round(size, 2)))  
    return file_list


directory_path = 'C:\\Users\\user'

print(listing_directory(directory_path))


# In[4]:


def selection_sort(file_list):
    n = len(file_list)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if file_list[j][2] < file_list[min_index][2]:  # comparer les tailles des fichiers
                min_index = j
        file_list[i], file_list[min_index] = file_list[min_index], file_list[i]
    return file_list

# Exemple d'utilisation
sorted_list_by_size = selection_sort(listing_directory('C:\\Users\\user')) # Remplacez par le chemin 
print("Tri par taille de fichier :")
print(sorted_list_by_size)


# In[4]:


def bubble_sort_by_name(files_list):
    n = len(files_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if files_list[j][0] > files_list[j + 1][0]:  # Comparaison par nom de fichier (1er élément du triplet)
                files_list[j], files_list[j + 1] = files_list[j + 1], files_list[j]
    return files_list
# Exemple de liste de fichiers
files_list = [("fichier2", ".txt", 3), ("image_fati", ".png", 10), ("fichier1", ".txt", 2)]

# Trier par nom (tri par bulles)
sorted_by_name = bubble_sort_by_name(files_list)
print("Trié par nom :", sorted_by_name)

