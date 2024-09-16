import math
from collections import defaultdict


# fonction permettant d'entrer une chaine de caracteres et de la mettre sous le format avec seulement des lettres en minuscule
# parametre: X: permet d'adapter la phrase d'input
def affiche(x):
    text = input(f"Entrer votre {x} : ")

    #transforme la chaine de caracteres en gardant seulement les lettres en les mettants au format minuscule
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
        #si le compteur de la cle depace la cle il est reinitialise
        if j >= len(cle):
            j = 0

        #recupere la valeur unicode des caracteres actuels et enleve la valeur de 'a' pour avoir la valeur dans l'alphabet
        lettre = ord(message[i]) - 96
        cle_val = ord(cle[j]) - 96

        #Si on crypte on avance la lettre de la valeur de la cle, sinon on recule
        if mode == "cryptage":
            valeur = (lettre + cle_val - 1) % 26 + 1
        if mode == "decryptage":
            valeur = (lettre - cle_val - 1) % 26 + 1

        #Le caractere trouver est remis sous code Unicode et remis sous format de lettre puis ajouter a le chaine de resultat
        text += chr(valeur + 96)
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
    #boucle qui affiche les sequences avec plus que 1 occurences et trouve celle avec la plus grande
    for sequence, count in occurences.items():
        if count > 1:
            print(f"{sequence} trouve {count} fois")
            if count_max < count:
                max_sequence = sequence
                count_max = count
    return [max_sequence, count_max, texte]


def distance(occu):
    position = []
    distance = []
    sequence = occu[0]
    repetion = occu[1]
    texte = occu[2]
    start = 0
    for i in range(repetion):
        start = texte.find(sequence, start) + 1
        position.append(start - 1)

    for i in range(len(position) - 1):
        distance.append(position[i + 1] - position[i])

    return distance


def longueur_cle(distance):
    pgcd = distance[0]
    for i in range(distance[:1]):
        pgcd = math.gcd(pgcd, i)
    return pgcd

'''
texte = affiche("Message")
cle = affiche("cle")
crypter = vigenere(texte, cle)
decrypter = vigenere(crypter, cle, "decryptage")
print("message crypter : {}\nmessage decrypter : {}".format(crypter, decrypter))
'''
occu = occurence("abcdefghijklmnopqrstuvwxyzabcdmnoabc")
'''print(longueur_cle(distance(occu)))'''
