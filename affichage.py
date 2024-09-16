import math
from collections import defaultdict


# fonction permettant d'entrer une chaine de caracteres et de la mettre sous le format avec seulement des lettres en minuscule
# parametre: X: permet d'adapter la phrase d'input
def affiche(x):
    text = input(f"Entrer votre {x} : ")

    #transforme la chaine de caracteres en gardant seulement les lettres en les mettants au format minuscule
    text = "".join([char for char in text.lower() if char.isalnum()])

    return text

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
    distance = [position[i + 1] - position[i] for i in range(len(position) - 1)]

    return distance


def longueur_cle(distance):
    if not distance:
        return 0
    pgcd = distance[0]
    for d in distance[1:]:
        pgcd = math.gcd(pgcd, d)
    return pgcd


texte = format("Réseau et sécurité M1 informatique TP sur l’implémentation et la cryptanalyse du chiffrement de Vigenère Dans ce TP, nous allons implémenter un chiffrement de Vigenère. Puis, nous implémenterons des outils pour le casser. 1. Implémentation du chiffrement de Vigenère Exercice 1 : Implémentez un programme (en C par exemple) qui demande à l’utilisateur de saisir un texte, et qui l’affiche. Exercice 2 : Modifiez votre programme pour qu’il convertisse toutes les lettres en minuscules, et qu’il enlève tous les autres caractères. Exemple: user$ prog2 Entrez un texte : Le soleil brille! Texte non chiffré : lesoleilbrille Exercice 3 : Implémentez une fonction qui prend en entrée deux lettres minuscules (l’une étant une lettre du texte non chiffré, et l’autre une lettre de la clé), et qui retourne la lettre minuscule correspondante chiffrée. Exemple : user$ prog3 m b b = 2 m + 2 = o Exercice 4 : Modifiez votre programme pour qu’il demande à l’utilisateur deux textes (l’un étant le texte non chiffré, et l’autre la clé), qui les convertit tous les deux (selon l’exercice 2), et qui chiffre le texte avec le chiffrement de Vigenère et la clé donnée. Exercice 5 : Implémentez un programme qui demande à l’utilisateur deux textes (l’un étant le texte chiffré, et l’autre la clé), et qui déchiffre le texte. 2. Cryptanalyse par estimation de la longueur de la clé et analyse fréquentielle 2.1 Méthode de Babbage et Kasiki Exercice 6 : Implémentez un programme qui prend en paramètre un texte chiffré, et qui affiche toutes les occurrences de séquences de 3 lettres ou plus qui se répétent. Exemple : user$ prog6 cipher: abcdefghijklmnopqrstuvwxyzabcdmnoabc abc trouvé 3 fois bcd trouvé 3 fois abcd trouvé 2 fois mno trouvé 2 fois Exercice 7 : Modifiez votre programme pour qu’il calcule la longueur de la clé à partir des distances entre les répétitions. Exercice 8 : Améliorez votre programme pour qu’il supprime les répétitions peu probables (par exemple, 10% des répétitions). Expliquez ce que vous considérez comme peu probable. 2.2 Test de Friedman Exercice 9 : Soit Tr un grand texte, généré aléatoirement, en utilisant seulement des lettres minuscules. Quelle est la probabilité Kr que deux lettres choisies aléatoirement soient égales, dans Tr ? Exercice 10 : Soit Te un grand texte rédigé en anglais, et utilisant uniquement des lettres minuscules. La probabilité que deux lettres choisies aléatoirement soient égales dans Te est environ Ke≈0.067. Expliquez pourquoi cette valeur est différente de la valeur de l’exercice 9. Exercice 11 : Soit T un texte utilisant uniquement des lettres minuscules. Écrivez un programme qui calcule la probabilité K que deux lettres choisies aléatoirement soient les mêmes dans T. Remarque : Vous pouvez considérer les 26 événements indépendants consistant à choisir la lettre li d’abord. Ainsi, K devient la somme des probabilités Ki, où Ki est la probabilité que deux lettres choisies aléatoirement soient égales à li. Exercice 12 : Le test de Friedman estime la longueur de la clé L comme (Ke-Kr)/(K-Kr). Calculez L. Remarque : Quand L=1, on a Ke=K, puisque le chiffrement de Vigenère correspond alors au cas d’un chiffrement par substitution simple. For L>1, K est égal à la probabilité que li soit égale à lj, avec li et lj qui correspondent à la même position dans la clé, plus la probabilité que li soit égale à lj, avec li et lj qui correspondent à des positions différentes dans la clé. Ainsi, K est égal à Ke/L (car il y a une probabilité 1/L que li et lj correspondent à la même position de la clé) plus (L-1).Kr/L (car il y a une probabilité (L-1)/L que li et lj correspondent à des positions différentes de la clé). Dans ce cas, on a (Ke-Kr)/(K-Kr)=L. Exercice 13 : Comment expliquez-vous que le test de Friedman puisse échouer ? Vous pouvez proposer plusieurs explications, par exemple en discutant sur les hypothèses de simplification faites dans la remarque de l’exercice 12. 2.3 Analyse fréquentielle Exercice 14 : Implémentez un programme qui prend en entrée un texte chiffré et une longueur de clé, et qui casse le chiffrement de Vigenère en utilisant une analyse fréquentielle. Le programme peut demander à l’utilisateur quel caractère chiffré correspond à quel caractère en clair, mais le programme doit fournir à l’utilisateur assez d’informations. 3. Cryptanalyse par méthode du mot probable La méthode de Bazeries consiste à deviner un mot probable, et essaye de trouver la clé en testant ce mot à toutes les positions possibles. Le mot probable doit idéalement avoir une longueur supérieure (strictement) à celle de la clé. Exercice 15 : Implémentez un programme qui prend en entrée un texte chiffré, un mot probable et une position. Le programme essaye de décrypter le texte chiffré en utilisant le mot probable comme clé. Si le mot probable est correctement placé, le résultat est la clé (répétée). Exercice 16 : Modifiez votre programme pour qu’il teste toutes les positions possibles, et affiche toutes les clés possibles. Remarque 1 : Une clé possible est un mot qui se répète. Remarque 2 : Prenez soin à bien faire en sorte que la clé s’affiche à partir de la bonne position (par exemple, si le mot probable est trouvé en position 2, la première lettre trouvée de la clé va être la lettre 2 ; il faut penser à réafficher la clé à partir de la première lettre).")
cle = format("soleil")
crypter = vigenere(texte, cle)
print(f"Le message crypter est : \n{crypter}\n")

occu = occurence(crypter)
print(f"La sequence la plus presente est {occu[0]} avec une occurence de {occu[1]}")

dist = distance(occu)
print(f"La distance entre chaque ocurence est de {dist}")
longueur = longueur_cle(dist)


if longueur == len(cle):
    print(f"Gagne la longueur de la cle est bien {longueur}")
else:
    print(f"Perdu avec un ecart de : {longueur - len(cle)}\nOu la cle vaut {len(cle)}\nEt la valeur trouver est {longueur}")
