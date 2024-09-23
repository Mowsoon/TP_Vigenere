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

#fonction qui permet d'utiliser l'equation de friedman pour trouver la taille de la cle
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
    #range chaque lettre du texte chiffrer avec l'indice de la cle lui correspondant
    for i in range(len(texte_crypter)):
        segments[i % taille_cle] += texte_crypter[i]

    #pour chaque segment calcul la valeur de l'indice de la cle la plus probable
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


#Cherche les répétitions de séquence de mot de longueur >= 2 dans un mot ou texte entré en paramètre
def repetition(texte):
    plus_longue_sequence = ""

    # Parcours le texte pour trouver les sous-chaînes de longueur >= min_length
    for length in range(2, len(texte)//2 + 1):
        repet = {}

        for i in range(len(texte) - length + 1):
            sequence = texte[i:i+length]
            if sequence in repet:
                repet[sequence] += 1
            else:
                repet[sequence] = 1

        # Vérifie s'il y a une séquence répétée plus longue que celle déjà trouvée
        for seq, count in repet.items():
            if count > 1 and len(seq) > len(plus_longue_sequence):
                plus_longue_sequence = seq

    return plus_longue_sequence


#fonction qui permet d'estimer une clé d'un texte chiffré grâce à un mot probable et à une position
#il faut que le mot probable soit au moins deux fois plus grand que la clé inconnue pour espérer de la retrouver sinon on ne retrouvera que des morceaux de clé
def bazeries(texte_chiffre, mot_probable, position):
    dechiffre = ""

    #Déchiffre les lettres une par une dans la partie du texte chiffré débutant à la position indiquée en paramètre et jusqu'à la longueur du mot probable
    for i in range (0, len(mot_probable)):
        lettre = ord(texte_chiffre[i+position]) - ord('a')
        lettre_clair = ord(mot_probable[i]) - ord('a')

        valeur = (lettre - lettre_clair) % 26

        dechiffre += chr(valeur + ord('a'))

    #Vérification de l'existence de répétitions dans le mot déchiffré, dans le cas où l'on trouve une répétition alors on en déduit que c'est une clé possible et on la retourne
    cles_repet = repetition((dechiffre))
    return cles_repet


#Appelle la fonction bazeries en boucle pour chaque position possible dans le texte et renvoie une série de clé possible pour déchiffrer le texte chiffré
def bazeries_boucle (texte_chiffre, mot_probable):
    cle_probable = []

    #Parcours chaque position du texte pour essayer de trouver des clés possible en appelant la fonction bazeries
    for i in range (0, len(texte_chiffre)-len(mot_probable)):
        tmp = bazeries(texte_chiffre, mot_probable, i)
        #Vérifie si la clé n'est pas égale au mot vide et si elle n'est pas déjà dans la liste des clés possibles
        if tmp != "" and tmp not in cle_probable:
            cle_probable.append(tmp)

        tmp = ""

    return(cle_probable)

#-----------------------test------------------------------------------------
#initialisation du message et son cryptage en vigenere
texte = format("La nature est une source inepuisable de beaute et d'inspiration. Les montagnes majestueuses, les forets denses et les rivieres sinueuses offrent un spectacle a couper le souffle. Chaque saison apporte son lot de transformations, rendant la nature toujours changeante et fascinante. Au printemps, les arbres se parent de fleurs eclatantes, tandis que l'ete inonde les paysages de lumiere et de chaleur. L'automne, quant a lui, teinte la nature de couleurs chatoyantes, avec ses feuilles rouges et dorees, avant que l'hiver ne vienne recouvrir le tout d'un manteau blanc immacule. Ce cycle infini nous rappelle a quel point la nature est precieuse et merite d'etre protegee. Que ce soit lors d'une promenade en foret, d'une randonnee en montagne ou simplement en observant un coucher de soleil, la nature a le pouvoir de nous apaiser et de nous reconnecter a l'essentiel. Elle est un refuge pour ceux qui cherchent a echapper au stress de la vie moderne et une source de bien-etre pour tous ceux qui prennent le temps de la contempler.")
cle = format("test")

"""
#pour entrer le message et la cle avec le terminal
texte = affiche("message")
cle = affiche("cle")
"""

crypter = vigenere(texte, cle)

print(f"Le message crypter est : \n{crypter}\n")
Kasiki = methodeBabbageKasiki(crypter)
if len(cle) in Kasiki:
    print(f"La longueur de la cle est dans l'ensemble {Kasiki} d'apres Kasiki")
    for i in Kasiki:
        cle_potentiel = trouverCle(crypter, i)
        print(f"Pour la longueur {i} la cle serait {cle_potentiel}\nLe message originel serait donc {vigenere(crypter, cle_potentiel, mode='decryptage')}\n")
else:
    print("Kasiki n'a pas réussi a trouver la taille de la cle")

Friedman = friedman(crypter)
if len(cle) == Friedman:
    cle_potentiel = trouverCle(crypter, Friedman)
    print(f"La longueur de la cle est {Friedman} d'apres Friedman et sa valeur serait {cle_potentiel}\nLe message originel serait donc {vigenere(crypter, cle_potentiel, mode='decryptage')}\n")
else:
    print("Friedman n'a pas réussi a trouver la taille de la cle")

print(f"D'après la méthode de Bazeries : \nLes clés possibles trouvées sont : {bazeries_boucle(crypter, 'montagne')}")
