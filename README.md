# Machine Learning avec Random Forests; Streamlit 

Le projet est l'étape finale (MLOps) : le déploiement d'un modèle de Machine Learning avec Python. Le modèle prédit la propension à l'obésité. La mise en production de l'app interactive est assurée par Streamlit. Bouton droit vers : <a href="https://mlrandomforestsappv2-8dhyejlam2znalxyedh86o.streamlit.app/" target="_blank">site</a>.

<img src="img/ml_random_forests_streamlit.png" alt="" width="300px">

## Origine du projet

Consulter le dépôt les étapes précédant le déploiement : **ml_random_forests**.

Ce dépôt est l'ancien dépôt qui alimentait Streamlit. Il ne présente que le projet.

Le nouveau dépôt qui alimente Streamlit Cloud est : **ml_random_forests_streamlit_v2**.

## Mise en place et structure

Streamlit permet de construire des apps interactives avec un code source Python.

Streamlit Cloud se branche sur le dépôt de données, importe tous les actifs, crée un environnement virtuel selon des paramètres choisis sur Streamlit Cloud (la version de l'interpréteur Python, par exemple) et installe la version de l'interpréteur. Ensuite, Steamlit Cloud installe les modules indépendants du fichier 'requirements.txt'. L'app fonctionne avec le code source '01_Modele.py'. Le code source tire les images du sous-répertoire 'img/' et tire les fichiers Pickle (les modèles) du sous-répertoire 'modele/'.

L'app obtenue est une interface graphique qui permet de modifier des facteurs de vie (feature des modèles) comme si on fournissait de nouvelles données aux modèles. Chaque changement déclenche un calcul des prévisions (c'est l'interaction). Les données entrent dans le modèle et deux prévisions en ressortent : versions 1 et 2 du modèle. 

L'app intègre deux morceaux importants : deux versions du modèle, un binomila et l'autre multinomial.  modèle en format Pickle. Comme il s'agit de modèles Random Forests, le scaler développé dans le projet **ml_random_forests** n'a pas été retenu. On ne retrouve pas de fichier Pickle du scaler dans le sous-répertoire 'modele/'. Avant d'arrêter le choix sur les Random Forests, il y a eu des tests avec d'autres modèles de classification : régression logistique, arbre de décision simple et Support Vector Classification. Ces modèles fonctionnent mieux quand le données sont transformées avec un scaler pour niveller les disparités de variances entre features. Les Randoms Forests règlent beaucoup de problèmes dont les autres modèles de classification souffrent. Entre autres, les Random Forests ne sont pas affectées par les disparités de variances entre features.
