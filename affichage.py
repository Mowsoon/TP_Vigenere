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
    return estimation



def repetition(text, min_length=2):
    longest_sequence = ""

    # Parcourir le texte pour trouver les sous-chaînes de longueur >= min_length
    for length in range(min_length, len(text)//2 + 1):
        seen = {}
        for i in range(len(text) - length + 1):
            sequence = text[i:i+length]
            if sequence in seen:
                seen[sequence] += 1
            else:
                seen[sequence] = 1

        # Vérifier s'il y a une séquence répétée plus longue que celle déjà trouvée
        for seq, count in seen.items():
            if count > 1 and len(seq) > len(longest_sequence):
                longest_sequence = seq

    return longest_sequence


#il faut que le mot probable soit plus grand
def bazeries(texte_chiffre, mot_probable, position):
    dechiffre = ""
    for i in range (0, len(mot_probable)):
        lettre = ord(texte_chiffre[i+position]) - ord('a')
        lettre_clair = ord(mot_probable[i]) - ord('a')

        valeur = (lettre - lettre_clair) % 26

        dechiffre += chr(valeur + ord('a'))


    cles_repet = repetition((dechiffre))
    return cles_repet


def bazeries_boucle (texte_chiffre, mot_probable):

    cle_probable = []

    for i in range (0, len(texte_chiffre)-len(mot_probable)):
        tmp = bazeries(texte_chiffre, mot_probable, i)
        if tmp != "" and tmp not in cle_probable:
            cle_probable.append(tmp)

        tmp = ""

    print(cle_probable)
    return(cle_probable)


#-----------------------test------------------------------------------------

#initialisation du message et son cryptage en vigenere
texte = format("Dans un petit village niché au cœur des montagnes, une légende circulait depuis des générations. Elle parlait d'une grotte secrète, cachée au sommet du plus haut pic, qui renfermait des trésors oubliés depuis des siècles. Les anciens disaient que seuls les plus braves et les plus purs de cœur pouvaient espérer atteindre cette grotte, car le chemin était périlleux, semé d'embûches, et gardé par des créatures mysterieuses. Beaucoup avaient tenté l'aventure, mais aucun n'en était jamais revenu. Les habitants du village vivaient paisiblement, bercés par les récits des anciens, sans vraiment croire qu'un jour quelqu'un pourrait découvrir le secret de la montagne. Pourtant, un jour, un jeune homme du nom d'Élias, intrépide et curieux, décida de braver l'interdit. Depuis son enfance, il avait entendu parler de la légende et, malgré les avertissements de ses parents et des anciens du village, il sentait en lui un appel irrésistible à partir à la découverte de cette grotte mythique. Équipé d'un simple sac à dos, de provisions et d'une vieille carte transmise de génération en génération, Élias entreprit son voyage. Les premiers jours de marche furent relativement faciles, les sentiers étaient bien tracés et il pouvait encore apercevoir le village en contrebas à mesure qu'il montait. Mais plus il s'enfonçait dans la montagne, plus le paysage devenait hostile. Les arbres se raréfiaient, remplacés par des rochers escarpés et des falaises vertigineuses. Le vent soufflait avec une intensité grandissante, rendant chaque pas plus difficile. Pourtant, Élias continuait d'avancer, déterminé à percer le mystère. Au bout de quelques jours, il atteignit une partie du chemin que personne dans le village n'avait jamais évoquée. Un épais brouillard entourait les lieux, et une étrange sensation de malaise s'empara de lui. C'était comme si la montagne elle-même cherchait à le dissuader de continuer. Mais Élias, fort de sa détermination, refusa de faire demi-tour. Il savait qu'il était proche. Le soir venu, alors qu'il s'apprêtait à monter son camp pour la nuit, il entendit un bruit sourd résonner au loin. Intrigué, il suivit le son jusqu'à une petite crevasse dissimulée entre deux rochers. Là, il découvrit une entrée secrète, à peine visible sous les ombres du crépuscule. Sans hésiter, il s'y engouffra. À l'intérieur, il fut accueilli par un silence pesant et une obscurité totale. Il alluma sa lampe et progressa lentement à travers les étroits passages de la grotte. Les murs étaient ornés de gravures anciennes, retraçant des histoires de batailles, de royaumes disparus et de créatures légendaires. Plus il avançait, plus il se rendait compte que cette grotte n'était pas simplement un abri naturel, mais un lieu de grande importance pour une civilisation oubliée. Au bout de ce qui lui sembla être des heures, Élias déboucha dans une immense cavité. Devant lui, se dressait un gigantesque autel de pierre, sur lequel reposait un coffre en or massif, incrusté de pierres précieuses. Le cœur battant, il s'approcha lentement du coffre. Mais au moment où il tendit la main pour l'ouvrir, un grondement sourd fit trembler la grotte. Des ombres se mirent à bouger autour de lui, et il se retrouva face à face avec une créature gigantesque, mi-humaine, mi-féline, dont les yeux luisaient dans l'obscurité. 'Qui ose troubler le repos des anciens ?' gronda la créature d'une voix profonde. Pris de panique, Élias recula, mais quelque chose en lui l'empêchait de fuir. Il se redressa et, rassemblant tout son courage, il répondit : 'Je suis Élias, venu en quête de vérité, et non de trésors. Si je suis ici, c'est pour comprendre les mystères de cette montagne et honorer ceux qui y ont vécu avant nous.' La créature le fixa longuement, comme si elle sondait son âme. Puis, lentement, elle s'écarta, laissant le chemin libre vers le coffre. Élias, surpris mais soulagé, s'avança de nouveau. Lorsqu'il ouvrit le coffre, il ne trouva pas d'or, ni de bijoux, mais des parchemins anciens, contenant des écrits oubliés, des connaissances perdues sur le monde, la nature, et les secrets de la vie elle-même. Élias comprit alors que la véritable richesse ne résidait pas dans les biens matériels, mais dans la connaissance et la sagesse. Il quitta la grotte avec les parchemins, déterminé à les partager avec son village et à changer la façon dont ses habitants voyaient le monde. À son retour, il fut accueilli en héros. Non seulement il avait survécu à l'aventure, mais il apportait avec lui un savoir inestimable, capable de transformer leur vie à jamais. La légende de la montagne ne serait plus jamais perçue comme un simple conte, mais comme une vérité profonde sur la quête de soi et la valeur de la connaissance.")
cle = format("alban")

print(bazeries_boucle(vigenere(texte, cle), "mysterieuse"))

"""
#pour entrer le message et la cle avec le terminal
texte = affiche("message")
cle = affiche("cle")
"""
crypter = vigenere(texte, cle)
print(trouverCle(crypter, len(cle)))




#test pour le cryptage et decryptage
"""
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




#test de la methode de friedman
taille_trouver = friedman(crypter)

if len(cle) == taille_trouver:
    print(f"Gagne la longueur de la cle est bien {taille_trouver}")
    print(f"La cle est estimer etre {trouverCle(crypter,taille_trouver)}")

else:
    print(f"Perdu la cle n'est pas {taille_trouver}")

