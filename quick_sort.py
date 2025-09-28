# Mon premier Quick Sort simple
# Auteur: Sirallah

def quick_sort(liste):
    # Si la liste a 0 ou 1 élément, elle est déjà triée
    if len(liste) <= 1:
        return liste
    
    # On prend l'élément du milieu comme pivot
    pivot = liste[0]
    
    # On crée deux nouvelles listes
    petits = []
    grands = []
    
    # On met chaque élément dans la bonne liste
    for element in liste[1:]:
        if element < pivot:
            petits.append(element)
        else:
            grands.append(element)
    
    # On combine tout
    return quick_sort(petits) + [pivot] + quick_sort(grands)

# Test simple
liste_test = [5, 2, 8, 1, 9]
print("Avant:", liste_test)
resultat = quick_sort(liste_test)
print("Après:", resultat)
