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
        #actualisation du start a la prochaine occurence
        start = texte.find(sequence, start)
        position.append(start)
        #incrementation pour eviter la repetition de meme occurence
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


#fonction qui renvoie un tableau des lettres de l'alphabet en minuscule ou la valeur du tableau est le pourcentage
#de presence de la lettre dans le texte
def pourcentageLettres(texte):
    #tableau de 26 valeurs (une pour chaque lettre de l'alphabet)
    lettres = [0] * 26
    
    #parcours chaque caractère du texte et incremente la case de la lettre corespondant a chaque caractere
    for char in texte:
        index = ord(char) - ord('a')
        lettres[index] += 1
        
    #divise par la taille du texte et multiplie par 100 chaque case pour avoir le pourcentage     
    for lettre in range(26):     
        lettres[lettre] /= len(texte)
        lettres[lettre] *= 100
    return lettres


# Calcul de la probabilite que si on choisi deux lettres au hazard, elle soit identique
# prend en parametre le pourcentages de presence de chaque lettres ainsi que la taille du texte
def deuxLettresIdentiques(pourcentages, taille_texte):
    prob_identique = 0
    #calcul la probabilte pour chaque lettre
    for p in pourcentages:
        #met le pourcentage en format de probabilites et trouve le nombre de lettre presente dans le texte
        p = p/100
        nombre_lettre = p * taille_texte
        
        #trouve la probabilite que la lettre actuel soit celle que l'on est trouve deux fois
        prob_lettre = (nombre_lettre*(nombre_lettre-1))/(taille_texte * (taille_texte-1))
        #incremente la probabilite de trouver n'importe quelle lettre 2 fois
        prob_identique += prob_lettre
    return prob_identique

#fonction permettant de prendre un texte et calculer la probabilite que si 2 lettres soit choisi aleatoirement, elles soient les memes
def trouverDeuxLettres(texte):
    proportion = pourcentageLettres(texte)
    print(f"La probabilité de trouver 2 lettres identiques de maniere aleatoire dans ce texte est :\n{deuxLettresIdentiques(proportion, len(texte))}")


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
for i in range(26):
    proportion_identique_de_lettres.append(100/26)

#frequence de chaque lettres en anglais et francais. Source : Wikipedia
pourcentages_lettres_en = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153,
                           0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
                           2.758, 0.978, 2.360, 0.150, 1.974, 0.074]

pourcentages_lettres_fr = [7.636, 0.901, 3.26, 3.669, 14.715, 1.066, 0.866, 0.737, 7.529, 0.613,
                           0.074, 5.456, 2.968, 7.095, 5.796, 2.521, 1.362, 6.693, 7.948, 7.244,
                           6.311, 1.838, 0.049, 0.427, 0.128, 0.326]

taille_texte = 10000000000000000000000000000

print(f"Pour un texte de taille {taille_texte} la probabilité de tomber deux fois sur la même lettre de maniere aléatoire est:")
print(f"Pour un texte générer avec le meme nombre de chaque lettre :\n{deuxLettresIdentiques(proportion_identique_de_lettres, taille_texte)}")
print(f"Pour un texte francais :\n{deuxLettresIdentiques(pourcentages_lettres_fr, taille_texte)}")
print(f"Pour un texte anglais :\n{deuxLettresIdentiques(pourcentages_lettres_en, taille_texte)}\n")


texte = format("azertyuiopqsdfghjklmwxcvbnazertyuiopqsdfghjklmwxcvbn")
trouverDeuxLettres(texte)