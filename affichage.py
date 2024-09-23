import math
import random
import string
from collections import defaultdict
from collections import Counter

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
def occurence(texte_crypter):
    #initialisation du dictionnaire qui stocke les occurences de chaque sequences
    occurences = defaultdict(int)

    longueur = len(texte_crypter)
    #boucle qui trouve toutes les sequences et qui compte leurs occurences
    for i in range(longueur):
        #j est initialise 3 caractere apres i et avance jusqu a la fin de la chaine
        for j in range(i + 3, longueur + 1):
            #trouve la sequence qui comprend les caracteres entre i et j
            sequence = texte_crypter[i:j]
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

    return [max_sequence, count_max, texte_crypter]

# fonction qui permet de trouver les distances entre chaque occurences d'une sequence sur une chaine de caracteres
# prend en parametre une liste qui a en premier element la sequence, en deuxieme son nombre d'occurence et enfin la chaine de caracteres
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
def liste_diviseurs_commun(distances):
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

def methodeBabbageKasiki(texte_crypter):
    return liste_diviseurs_commun(distance(occurence(texte_crypter)))



def generer_chaine_aleatoire(taille):
    chaine = ''.join(random.choice(string.ascii_lowercase) for _ in range(taille))
    return chaine


#frequence de chaque lettres en anglais et francais. Source : Wikipedia
def generer_proportion_anglaise():
    return [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153,
            0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
            2.758, 0.978, 2.360, 0.150, 1.974, 0.074]

def generer_proportion_francaise():
    return [7.636, 0.901, 3.26, 3.669, 14.715, 1.066, 0.866, 0.737, 7.529, 0.613,
            0.074, 5.456, 2.968, 7.095, 5.796, 2.521, 1.362, 6.693, 7.948, 7.244,
            6.311, 1.838, 0.049, 0.427, 0.128, 0.326]





#fonction qui renvoie un tableau des lettres de l'alphabet en minuscule ou la valeur du tableau est le pourcentage
#de presence de chaque lettres dans le texte
def pourcentageLettres(texte):
    lettres = [0] * 26
    compteur_lettres = Counter(texte)
    total_lettres = len(texte)

    for lettre in compteur_lettres:
        index = ord(lettre) - ord('a')
        lettres[index] = (compteur_lettres[lettre] / total_lettres) * 100 if total_lettres > 0 else 0
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
    return deuxLettresIdentiques(proportion, len(texte))


def friedman(texte_crypter, langue="fr"):
    taille_texte = len(texte_crypter)

    #calcul de Ke en fonction de la langue
    if langue == "fr":
        Ke = deuxLettresIdentiques(generer_proportion_francaise(), taille_texte)
    elif langue == "en":
        Ke = deuxLettresIdentiques(generer_proportion_anglaise(), taille_texte)
    else:
        return None #cas de langue inconnue

    #calcul de Kr sur un texte aleatoire
    if taille_texte < 1000000:
        Kr = trouverDeuxLettres(generer_chaine_aleatoire(taille_texte))
    #cas d'optimisation avec la loi des grands nombres
    else:
        Kr = deuxLettresIdentiques([100 / 26] * 26, taille_texte)

    #calcul de K avec le texte chiffrer
    K = trouverDeuxLettres(texte_crypter)

    if Ke == K: return 1
    return round((Ke - Kr) / (K - Kr))

#permet d'estimer la cle en connaissant sa taille et en fonction de l'analyse frequentielle
def trouverCle(texte_crypter, taille_cle):
    segments = [''] * taille_cle
    estimation = ""

    for i in range(len(texte_crypter)):
        segments[i % taille_cle] += texte_crypter[i]

    for segment in segments:
        frequence = pourcentageLettres(segment)
        indiceMaxFrequence = frequence.index(max(frequence))
        #en sachant que e est la lettre la plus presente on estime que le decalage de la cle est (l'indice de la lettre la plus présente)-(l'indice de e)
        decalage = (indiceMaxFrequence - (ord('e') - ord('a'))) % 26
        estimation += chr(decalage + ord('a'))
    #verification que la cle est valide
    if vigenere(vigenere(texte_crypter, estimation),estimation, mode='decryptage') == texte_crypter:
        return estimation
    print("Echec dans la recherche de la cle")
    return None




#-----------------------test------------------------------------------------
#initialisation du message et son cryptage en vigenere
texte = format("ceci est un texte exemple qui fait plaisir a la famille")
cle = format("test de cle")


"""
#pour entrer le message et la cle avec le terminal
texte = affiche("message")
cle = affiche("cle")
"""




""""
crypter = vigenere(texte, cle)
cle_possible = trouverCle(crypter, len(cle))
print(cle_possible)
print(vigenere(crypter, cle_possible, mode="decryptage"))
"""

"""
#test pour le cryptage et decryptage

print(f"Le message crypter est : \n{crypter}")
decrypter = vigenere(crypter, cle,"decryptage")
print(f"Le message decrypter est : \n{decrypter}")
"""


"""
#testde la methode de Babbage et Kasiki

longueur = methodeBabbageKasiki(crypter)

if len(cle) in longueur:
    print(f"Gagne la longueur de la cle est bien dans l'ensemble {longueur}")

else:
    print(f"Perdu la cle n'est pas dans l'ensemble {longueur}")

"""

"""
#test pour le calcul de proportion

proportion_identique_de_lettres = [100/26] * 26
pourcentages_lettres_en = generer_proportion_anglaise()
pourcentages_lettres_fr = generer_proportion_francaise()
taille_texte = 1000000
print(f"Pour un texte de taille {taille_texte} la probabilité de tomber deux fois sur la même lettre de maniere aléatoire est:")


#Ce test permet de demontrer que pour un texte d'une tres grande taille (1 000 000+)completement aleatoire,
#la probabilité de trouver deux lettres identique est la meme que si les proportions de chaque lettres sont identiques
#mais generer une grande chaine de carateres ainsi est couteux en mémoire.
texte_aleatoire = generer_chaine_aleatoire(taille_texte)
print(f"Pour un texte avec des proportions completements aleatoire:\n{trouverDeuxLettres(texte_aleatoire)}")
print(f"Pour un texte générer avec le meme nombre de chaque lettre:\n{deuxLettresIdentiques(proportion_identique_de_lettres, taille_texte)}")



print(f"Pour un texte francais:\n{deuxLettresIdentiques(pourcentages_lettres_fr, taille_texte)}")
print(f"Pour un texte anglais:\n{deuxLettresIdentiques(pourcentages_lettres_en, taille_texte)}\n")
"""



"""
#test de la methode de friedman
taille_trouver = friedman(crypter)

if len(cle) == taille_trouver:
    print(f"Gagne la longueur de la cle est bien {taille_trouver}")
    print(f"La cle est estimer etre {trouverCle(crypter,taille_trouver)}")

else:
    print(f"Perdu la cle n'est pas {taille_trouver}")

"""