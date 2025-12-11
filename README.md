# Machine Learning avec Random Forests; Streamlit 

Le projet est l'étape finale (MLOps) : le déploiement d'un modèle de Machine Learning avec Python. Le modèle prédit la propension à l'obésité. 
Bouton droit vers : <a href="https://ugolabo-ml-random-forests-st-01-modele-widb6v.streamlit.app/" target="_blank">site</a>.

<img src="img/ml_random_forests_streamlit.png" alt="" width="300px">

## Origine du projet

Consulter le dépôt les étapes précédant le déploiement : **ml_random_forests**.

Ce dépôt est l'ancien dépôt qui alimentait Streamlit. Il ne présente que le projet.

Le nouveau dépôt qui alimente Streamlit Cloud est : **aaa**.
Le projet a été mis à jour avec la version 3.12.12 de Python et des versions plus récente des modules indépendants dont Streamlit. 

## Mise en place et structure

Streamlit permet de construire des apps interactives avec un code source Python. Consulter le projet : TODO.

description ici

structure du répertoire 'projet_ml_st', descriptions des fichiers et dossiers, requirements.txt

Note...

La structure du sous-répertoire du projet est la configuration requise par Streamlit Cloud pour construire l'interface graphique. L'app intègre deux morceaux importants : les versions 1 et 2 du modèle en format Pickle. Comme il s'agit d'un modèle de Random Forests, les scalers n'ont pas été retenus. Avant d'arrêter le choix sur les Random Forests, il y a eu des tests avec d'autres modèles de classification : arbre de décision simple et Support Vector Classification. Ces modèle fonctionnent mieux quand le données sont normalisées ou standardisées avec deux sortes de scalers. Les Randoms Forests règlent beaucoup de problèmes dont les autres modèles de classification souffrent. Entre autres, les Random Forests ne sont pas affectées par les disparités de variances entre features. Il est alors inutile d'utiliser des scalers.

L'app obtenue est une interface graphique qui permet de modifier les facteurs de vie comme si on fournissait au modèle de nouvelles données. Chaque changement déclenche un calcul des prévisions (c'est l'interaction). Les données entrent dans le modèle et deux prévisions en ressortent : versions 1 et 2 du modèle. 

Bouton droit vers : <a href="https://ugolabo-ml-random-forests-st-01-modele-widb6v.streamlit.app/" target="_blank">site</a>.
