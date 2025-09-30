**Test technique**

**installation et utilisation**

 - pip install -r requirements.txt
 - from main.py import *
 - pour récupérer la critique la plus similaire à la critique numéro 40 de fight_club : similarity(40, reviews_to_list("fightclub_critiques.csv"))


**présentation de la solution :** 

après des recherches sur les différents de traitement de textes en Python, j'ai décidé de m'orienter vers l'algorithme 
de similarité cossine étant déjà familier avec ce dernier. Pour implémenter cet solution de façon simple j'ai simplement
utiliser le package "skilearn" cependant il aurait était également possible d'implémenter l'outil NLTK
(natural language toolkit) de python afin d'avoir une meilleur analyse des données en prenant nottament en compte le
fait que les textes soient en français 

la solution consiste tout d'abord à récupérer toute la partie "texte" des fichiers CSV fournit et d'en faire une liste
intitulé "reviews" \- ce que fait la fonction "reviews_to_list - 

Une fois cette liste de texte récupéré on crée une "matrice" qui pour chaque critique de la liste va calculer la 
similarité cosinus de celle-ci avec toute les autres. ainsi si l'on veut connaitre la valeur de similarité cosine entre
la critique 1 et la critique 2 il nous suffit de regarder matrice[1][2], sachant que la valeur comprise entre 0 et 1 et 
qu'une valeur de 1 signifie qu'il s'agit du même texte

Afin donc de récupérer la critique la plus "similaire" d'une critique dont l'identifiant est x, 
il nous suffit de parcourir toute les valeurs de matrice[x] et de récupérer l'index de la valeur la plus élevé ET 
inférieur à 1 (sinon l'on récupérera juste la même critique) une fois cette index y récupéré on peut retrouver le texte
de la critique en question en il nous suffit de récupérer la critique reviews[j], reviews étant la liste des critiques 
créer à partir des fichiers CSV fournit 

**Similarité cosinus explication :**
https://youtu.be/e9U0QAFbfLI

documents utilisé pour la réalisation de cette solution : 
- https://spotintelligence.com/2022/12/19/text-similarity-python/
- https://memgraph.com/blog/cosine-similarity-python-scikit-learn
- https://www.geeksforgeeks.org/python/python-read-csv-columns-into-list/



