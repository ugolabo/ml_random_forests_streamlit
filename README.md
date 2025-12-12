# Machine Learning avec Random Forests; Streamlit 

Le projet est l'étape finale (MLOps) : le déploiement d'un modèle de Machine Learning avec Python. Le projet commence dans le dépôt: **ml_random_forests**. Le modèle prédit la propension à l'obésité. La mise en production de l'app interactive est assurée par Streamlit. Bouton droit vers : <a href="https://mlrandomforestsappv2-8dhyejlam2znalxyedh86o.streamlit.app/" target="_blank">site</a>.

<img src="img/ml_random_forests_streamlit.png" alt="" width="300px">

## Origine du projet

Consulter le dépôt les étapes précédant le déploiement : **ml_random_forests**.

Ce dépôt est l'ancien dépôt qui alimentait Streamlit. Il ne présente que le projet.

Le nouveau dépôt qui alimente Streamlit Cloud est : **ml_random_forests_streamlit_v2**.

## Mise en place et structure

Streamlit est un module Python indépendant permet de construire des apps interactives avec un code source Python. Un projet simple implique un seul code source Python. Un projet complexe comporte un ensemble de code source Python. Aucun HTML, CSS, JavaScript ou TypeScript, PHP ou autres langages n'est requis. Il est possible d'émuler l'app en local pour le développement.

On envoie le projet sur un dépôt GitHub. On branche Streamlit Cloud sur le dépôt de données pour qu'il importe tous les actifs.

Streamlit Cloud crée un environnement virtuel, selon des paramètres choisis (la version de l'interpréteur Python, par exemple) et installe la version de l'interpréteur. Ensuite, Steamlit Cloud installe les modules indépendants du fichier 'requirements.txt' dans le projet. L'app fonctionne avec le code source '01_Modele.py'. Le code source tire les images du sous-répertoire 'img/' et tire les fichiers Pickle (les modèles) du sous-répertoire 'modele/'.

L'app web obtenue est une interface graphique qui permet d'alimenter le modèle avec de nouvelles données : un nouvel individu (une nouvelle observation) et ses facteurs de vie (les features x). Le modèle prédit automatiquement la catégorie d'IMC de l'individu (la variable y). Chaque changement déclenche un calcul des prévisions (c'est l'interaction). Les données entrent dans le modèle et deux prévisions en ressortent. Le modèle multinomial prédit une des 7 catégories. Le modèle binomial prédit une des 2 catégories.

L'app interactive intègre deux morceaux importants : deux modèles (binomial et multinomial) en format Pickle. Comme il s'agit de Random Forests, le scaler développé dans le projet **ml_random_forests** n'a pas été retenu. On ne retrouve pas de fichier Pickle du scaler dans le sous-répertoire 'modele/'. Avant d'arrêter le choix sur les Random Forests, il y a eu des tests avec d'autres modèles de classification. Certains de ces modèles fonctionnent mieux quand les données sont transformées avec un scaler. L'explication est fournie dans le dépôt : **ml_random_forests**. Les Randoms Forests règlent beaucoup de problèmes dont les autres modèles de classification souffrent.
