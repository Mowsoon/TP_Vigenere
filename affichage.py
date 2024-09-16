import math

# fonction permettant d'entrer une chaine de caracteres et de la mettre sous le format avec seulement des lettres en minuscule
# parametre: X: permet d'adapter la phrase d'input
def affiche(x):
    text = input("Entrer votre {} : ".format(x))

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


def occurence(texte):
    occu = []
    occurrences = {}

    longueur = len(texte)

    for i in range(longueur):
        for j in range(i + 3, longueur + 1):
            sequence = texte[i:j]
            if sequence in occurrences:
                occurrences[sequence] += 1
            else:
                occurrences[sequence] = 1

    count_max = 0
    for sequence, count in occurrences.items():
        if count > 1:
            print("{} trouve {} fois".format(sequence, count))
            if count_max < count:
                count_max = count
                if occu:
                    occu.pop()
                    occu.pop()
                occu.append(sequence)
                occu.append(count)
    occu.append(texte)
    return occu


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


texte = affiche("Message")
cle = affiche("cle")
crypter = vigenere(texte, cle)
decrypter = vigenere(crypter, cle, "decryptage")
print("message crypter : {}\nmessage decrypter : {}".format(crypter, decrypter))
'''
occu = occurence("abcdefghijklmnopqrstuvwxyzabcdmnoabc")
print(longueur_cle(distance(occu)))'''
