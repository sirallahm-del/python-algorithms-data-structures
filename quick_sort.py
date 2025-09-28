# Quick Sort étape par étape
# Auteur: Sirallah

# Notre liste à trier
liste = [5, 2, 8, 1, 9]
print("Liste de départ:", liste)
# On choisit le premier élément comme pivot
pivot = liste[0]
print("Notre pivot est:", pivot)
# On crée deux listes vides
plus_petits = []
plus_grands = []
# Quick Sort étape par étape
# Auteur: Sirallah

# Notre liste à trier
liste = [5, 2, 8, 1, 9]
print("Liste de départ:", liste)

# On choisit le premier élément comme pivot
pivot = liste[0]
print("Notre pivot est:", pivot)

# On crée deux listes vides
plus_petits = []
plus_grands = []

# On regarde chaque élément après le premier
for i in range(1, len(liste)):
    element = liste[i]
    print("On regarde l'élément:", element)
    
    if element < pivot:
        plus_petits.append(element)
        print(element, "va dans plus_petits")
    else:
        plus_grands.append(element)
        print(element, "va dans plus_grands")

print("Plus petits:", plus_petits)
print("Plus grands:", plus_grands)
