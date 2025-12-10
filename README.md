# Machine Learning avec Random Forests; Streamlit 

Le projet est l'étape finale (MLOps) : le déploiement d'un modèle de Machine Learning avec Python. Le modèle prédit la propension à l'obésité.

Le projet consiste à la mise en production d'un modèle de Machine Learning avec Python. Le modèle prédit la propension à l'obésité. Le modèle apprend que l'Indice de Masse Corporelle (IMC) est relié à des facteurs de vie (alimentation, activité, habitudes, etc.). L'hygiène de vie mène à l'obésité ou non. Ces mêmes facteurs servent ensuite à classer si un individu sera obèse à long terme.

<img src="img/arbre_b.png" alt="" width="400px">

L'IMC est une variable continue. On peut établir des catégories. Un poids normal se situe entre 18.5 et 24.9 et l'obésité commence à 30.0. Entre les deux se trouve le surpoids. Deux individus, un à 31.0 et l'autre à 35.0 sont dans la catégorie Obèse. Le premier individu est aussi dans la sous-catégorie Obèse Classe I alors que le deuxième individu est dans la sous-catégorie Obèse Classe II. La catégorie Surpoids se subdivise aussi en sous-catégories.

Le modèle est entrainé en deux versions. La version binomiale (basée sur l'échelle des catégorie; Non Obèse (0) ou Obèse (1)) et la version multinomiale (basée sur l'échelle des sous-catégories).

Un autre repo est dédié au développement du modèle.

Le modèle est implanté dans une interface graphique qui permet de modifier les facteurs, de relancer le modèle et de faire des prévisions. Bouton droit vers : <a href="https://ugolabo-ml-random-forests-st-01-modele-widb6v.streamlit.app/" target="_blank">site</a>.

## Mise en place et structure

La structure du repo (répertoires et fichiers) est la configuration requise par Streamlit Cloud pour construire l'interface graphique.
