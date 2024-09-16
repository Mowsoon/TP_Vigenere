import math


def affiche(x):
    text = input("Entrer votre {} : ".format(x))

    text = "".join([char for char in text.lower() if char.isalnum()])

    return text

def cryptage(message, codage):

    text = ""
    j = 0
    for i in range(len(message)):
        if j >= len(codage):
            j = 0
        lettre = ord(message[i]) - 96
        cle = ord(codage[j]) - 96
        valeur = lettre + cle

        if valeur > 26:
            valeur -= 26

        text += chr(valeur + 96)
        j += 1

    return text

def decryptage(message, codage):

    text = ""
    j = 0
    for i in range(len(message)):
        if j >= len(codage):
            j = 0
        lettre = ord(message[i]) - 96
        cle = ord(codage[j]) - 96
        valeur = lettre - cle
        if valeur < 1:
            valeur += 26
        text += chr(valeur + 96)
        j += 1
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
                if occu :
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
        distance.append(position[i+1] - position[i])

    return distance


def longueur_cle(distance):
    pgcd = distance[0]
    for i in range(distance[:1]):
        pgcd = math.gcd(pgcd, i)
    return pgcd


texte = affiche("Message")
cle = affiche("cle")
crypter = cryptage(texte,cle)
decrypter = decryptage(crypter,cle)
print("message crypter : {}\nmessage decrypter : {}".format(crypter, decrypter))
'''
occu = occurence("abcdefghijklmnopqrstuvwxyzabcdmnoabc")
print(longueur_cle(distance(occu)))'''