import math
from collections import defaultdict


# fonction permettant d'entrer une chaine de caracteres et de la mettre sous le format avec seulement des lettres en minuscule
# parametre: X: permet d'adapter la phrase d'input
def affiche(x):
    text = input(f"Entrer votre {x} : ")

    #transforme la chaine de caracteres en gardant seulement les lettres en les mettants au format minuscule
    text = "".join([char for char in text.lower() if char.isalnum()])

    return text

#fonction identique a affiche mais faire pour les tests avec la chaine directement en parametre
def format(text):
    text = "".join([char for char in text.lower() if char.isalnum()])

    return text


# fonction permettant de crypter et decrypter une chaine de caracteres selon la methode de vignere
# parametre:    message:    chaine de caractere a modifier
#               cle:        chaine de caractere codant la modification
#               mode:       parametre optionnel permettant de choisir si on veut crypter ou decrypter, automatiquement en cypter
def vigenere(message, cle, mode='cryptage'):
    text = ""

    #initialisation du compteur pour la cle
    j = 0

    #boucle permettant de modifier chaque caractere un par un
    for i in range(len(message)):
        #si le compteur de la cle deplace la cle il est reinitialise
        if j >= len(cle):
            j = 0

        #recupere la valeur unicode des caracteres actuels et enleve la valeur de 'a' pour avoir la valeur dans l'alphabet
        lettre = ord(message[i]) - ord('a')
        cle_val = ord(cle[j]) - ord('a')
        print("lettre et cle")
        print(lettre, cle_val)

        #Si on crypte on avance la lettre de la valeur de la cle, sinon on recule
        if mode == "cryptage":
            valeur = (lettre + cle_val ) % 26
        if mode == "decryptage":
            valeur = (lettre - cle_val ) % 26

        #Le caractere trouver est remis sous code Unicode et remis sous format de lettre puis ajouter a le chaine de resultat
        text += chr(valeur + ord('a'))
        j += 1
    return text


#fonction qui mappe les sequences de 3 ou plus caracteres d'une chaine de caracteres
#et qui affiche les sequences qui revienne au moins une fois.
#Retourne egalement la sequence avec le plus grand nombre d'occurence avec ce nombre et la chaine original
def occurence(texte):
    #initialisation du dictionnaire qui stocke les occurences de chaque sequences
    occurences = defaultdict(int)

    longueur = len(texte)
    #boucle qui trouve toutes les sequences et qui compte leurs occurences
    for i in range(longueur):
        #j est initialise 3 caractere apres i et avance jusqu a la fin de la chaine
        for j in range(i + 3, longueur + 1):
            #trouve la sequence qui comprend les caracteres entre i et j
            sequence = texte[i:j]
            #incremente l'occurence de la sequence trouve
            occurences[sequence] += 1

    max_sequence = ""
    count_max = 0
    #boucle qui enregistre la sequence avec le plus d'occurence
    for sequence, count in occurences.items():
        if count > 1:
            if count_max < count:
                max_sequence = sequence
                count_max = count

    return [max_sequence, count_max, texte]

# fonction qui permet de trouver les distances entre chaque occurences d'une sequence sur une chaine de caracteres
def distance(chaine):
    sequence    = chaine[0]
    repetion    = chaine[1]
    texte       = chaine[2]

    position = []
    start = 0
    #boucle qui trouve les positions de chaque occurences de la sequences
    for _ in range(repetion):
        #actualisation du start pour trouver la prochaine occurence
        start = texte.find(sequence, start)
        position.append(start)
        #incrementation pour eviter la repetition d'occurence
        start += 1

    #calcul les distances entre chaque position
    distances = [position[i + 1] - position[i] for i in range(len(position) - 1)]

    return distances


#fonction permettant de calculer tous les diviseurs communs des distances
def longueur_cle(distances):
    if not distances: return []
    #calcul tous les diviseurs de la premiere distance
    diviseurs_commun = liste_diviseurs(distances[0])

    #boucle qui calcul les diviseurs de chaque distance et fais l'intersection avec les precedantes
    for d in distances[1:]:
        diviseurs_commun &= liste_diviseurs(d)

    return sorted(diviseurs_commun)


#fonction permettant de calculer les diviseurs d'une valeur
def liste_diviseurs(n):
    diviseurs = set()
    #boucle de 1 jusqu'a la racine de la valeur
    for i in range(1, int(math.sqrt(n))+1):
        #si un diviseur est trouver l'ajoute ainsi que son oppose par rapport a la valeur si ce n'est pas lui meme
        if n%i==0:
            diviseurs.add(i)
            if i != n//i:
                diviseurs.add(n//i)
    return diviseurs

def proportion_lettre_dans_texte(texte):
    # Initialiser un tableau de 26 valeurs à 0 (une pour chaque lettre de l'alphabet)
    lettres = [0] * 26

    # Parcourir chaque caractère du texte
    for char in texte:
        # Vérifier si le caractère est une lettre minuscule
        if 'a' <= char <= 'z':
            # Convertir la lettre en indice (0 pour 'a', 1 pour 'b', etc.)
            index = ord(char) - ord('a')
            # Incrémenter l'indice correspondant dans le tableau
            lettres[index] += 1
    for lettre in range(26):
        lettres[lettre] /= len(texte)
        lettres[lettre] *= 100
    return lettres


# Calcul de la probabilité qu'une lettre soit choisie deux fois
def prob_lettres_identiques(pourcentages, taille_texte):
    prob_identique = 0
    for p in pourcentages:
        p = p/100
        nombre_lettre = p * taille_texte
        prob_lettre = (nombre_lettre*(nombre_lettre-1))/(taille_texte * (taille_texte-1))
        prob_identique += prob_lettre
    return prob_identique

def proba_lettres_identiques_dans_texte(texte):
    proportion = proportion_lettre_dans_texte(texte)
    print(f"La probabilité de trouver 2 fois la meme lettre de maniere aleatoire dans ce texte est :\n{prob_lettres_identiques(proportion, len(texte))}")


"""
texte = format(" la cle s’affiche a partir de la bonne position")
cle = format("test")


crypter = vigenere(texte, cle)
print(f"Le message crypter est : \n{crypter}")
decrypter = vigenere(crypter, cle,"decryptage")
print(f"Le message decrypter est : \n{decrypter}")

occu = occurence(crypter)
print(f"La sequence la plus recurente est : {occu[0]} avec {occu[1]} occurences")


dist = distance(occu)
print(f"La distance entre chaque occurences est de {dist}\n")

longueur = longueur_cle(dist)
print(f"la taille de la cle est {len(cle)}")

if len(cle) in longueur:
    print(f"Gagne la longueur de la cle est bien dans {longueur}")

else:
    print(f"Perdu la cle n'est pas dans {longueur}")
"""



proportion_identique_de_lettres = []
for i in range (26):
    proportion_identique_de_lettres.append(100/26)


pourcentages_lettres_en = [8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15,
                           0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.10, 5.99, 6.33, 9.06,
                           2.76, 0.98, 2.36, 0.15, 1.97, 0.07]

pourcentages_lettres_fr = [7.64, 0.89, 3.26, 3.67, 14.72, 1.06, 0.87, 0.74, 7.53, 0.61,
                           0.05, 5.46, 2.97, 7.10, 5.79, 2.52, 1.36, 6.69, 7.95, 7.24,
                           6.31, 1.83, 0.05, 0.30, 0.24, 0.32]

taille_texte = 100000000000000000000000000

print(f"Pour un texte de taille {taille_texte} la probabilité de tomber deux fois sur la même lettre de maniere aléatoire est:")
print(f"Pour un texte générer avec le meme nombre de chaque lettre :\n{prob_lettres_identiques(proportion_identique_de_lettres, taille_texte)}")
print(f"Pour un texte francais :\n{prob_lettres_identiques(pourcentages_lettres_fr, taille_texte)}")
print(f"Pour un texte anglais :\n{prob_lettres_identiques(pourcentages_lettres_en,taille_texte)}\n")


texte = format("azertyuiopqsdfghjklmwxcvbnazertyuiopqsdfghjklmwxcvbn")
proba_lettres_identiques_dans_texte(texte)