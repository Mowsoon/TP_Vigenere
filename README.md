# TP_Vigenere

### **Exercice 8 : Enlever les répétions peu probable:**

Puisque la méthode de Babbage et Kasiki calcul la taille de la clé en fonction des répétitions d'occurence, si ces répétitions ne pas très communes elles ont la possibilités de fausser le résultat et de nous empecher de trouver la clé car on ne trouve pas de diviseurs communs car certaine répétitions seraient dû au hazard et non à une répétition de la clé sur la même séquence:

- On peut donc enlever les séquences avec des occurences bien plus faible que la moyenne et ainsi seulement garder les plus grandes récurences qui on une probabilité de correspondre au répétition de la clé plus élevé.


- Dans cette logique on peut même seulement garder la séquence avec le plus d'occurence car elle est celle qui a les plus grandes chance de correspondre aux répétitions de la clé tout en ayant l'option qui réduit le plus les chances de ne pas trouver de diviseurs commun.


   





### **Exercice 13 : Pourquoi le test de Friedman peut-il échouer ?**

Le test de Friedman pour estimer la longueur de la clé L repose sur des hypothèses qui peuvent ne pas toujours être valides dans des situations réelles. Voici plusieurs raisons qui peuvent expliquer l'échec du test :

### La taille du texte:

- Le test suppose que les lettres du texte clair suivent une distribution classique de leur langue, hors si le texte n'est pas assez long il ne sera pas fidèle à ses proportions, où si le texte possède une distribution insolite alors le test ne fonctionera pas.

### La forme de la clé:

- Si la clé comporte n'est pas indépendante d'un caractère à l'autre et comporte des répétitions où qu'elle soit trop courte peut également amener à des erreurs.

### Dépendance au langage:

- Le test a pour condition de devoir connaitre le langage du texte en clair car les proportions de chaque lettre d'un langage à l'autre ne sont pas les mêmes ainsi si on ne connait pas le langage du message de départ on ne pourra probablement pas trouver la taille de la clé.
