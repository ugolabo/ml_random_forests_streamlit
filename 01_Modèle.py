import streamlit as st
import base64
import pandas as pd
from typing import List, Union
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import joblib

# Dans le requirements.txt,
# ne pas installer de modules standards à Python

# Exécuter localement
# streamlit run 01_Modèle.py

##################################################
# Configurer la page
# wide, centered
# auto or expanded
st.set_page_config(page_title="Projet intégrateur",
                   page_icon="img/favicon.ico",
                   layout="wide",
                   initial_sidebar_state="auto",
                   menu_items={
                       "About": "Interface du modèle de Random Forests."}
)
    
# Cacher le menu officiel (hamburger)
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
# ???
#st.markdown(hide_menu_style, unsafe_allow_html=True)

##################################################
# Entrer les données pour les modèles
# Construire l'interface du bandeau gauche
with st.sidebar:
    
    st.title("Métriques")
    
    st.caption("Les métriques sont bornées aux valeurs (catégories ou minimum et maximum) des features du jeu de données utilisé pour entrainer le modèle.")
    
    Gender_n = st.radio(":orange[Genre]:", ["f", "m"], horizontal=True)
    
    Age = st.slider(":orange[Âge]:", min_value=14, max_value=61, value=23)
    
    Height = st.slider(":orange[Taille] (en cm) - Utiliser le tableau de conversion plus bas:", min_value=145, max_value=195, value=170)
    st.caption("Ajuster la taille de la fenêtre.")
    st.caption("Ajuster la disposition de la liste en tirant ce bandeau vers la droite 👉")
    equivalent = """
    | pi-po | cm | pi-po | cm | pi-po | cm |
    |:--|:--|:--|:--|:--|:--|
    |4' 9"|145|5' 4"|163| 5' 11"|180|
    |4' 10"|147| 5' 5"|165|	6' 0"|183|
    |4' 11"|150| 5' 6"|168|	6' 1"|185|
    |5' 0"|152| 5' 7"|170| 6' 2"|188|
    |5' 1"|155|	5' 8"|173| 6' 3"|191|
    |5' 2"|157|	5' 9"|175| 6' 4"|193|
    |5' 3"|160|	5' 10"|178| 6' 5"|196|
    """
    st.caption(equivalent)
    st.caption("")
    
    FHWO_n = st.radio(":orange[Obésité dans la famille (présente ou passée)]:", ["non", "oui"], horizontal=True)
    
    FAVC_n = st.radio("Consommation d'aliments hypercaloriques:", ["non", "oui"], horizontal=True)
    
    FCVC_n = st.radio(":orange[Consommation de légumes avec les repas]:", ["jamais", "parfois", "souvent"], index=1, horizontal=True)

    NCP_n = st.radio(":orange[Nombre de repas quotidien]:", ["1", "2", "3", "4 et plus"], index=2, horizontal=True)


    CAEC_n = st.radio(":orange[Collations entre les repas]:", ["jamais", "parfois", "fréquemment", "toujours"], index=1, horizontal=True)
    st.caption("Ajuster la taille de la fenêtre.")
    st.caption("Ajuster la disposition de la liste en tirant ce bandeau vers la droite 👉")
    
    SMOKE_n = st.radio("Tabagisme:", ["non", "oui"], horizontal=True)
    
    CH2O_n = st.radio("Consommation quotidienne d'eau (en litre):", ["moins de 1", "1 à 2", "plus de 2"], horizontal=True)
    
    SCC_n = st.radio("Surveillance de sa consommation calorique:", ["non", "oui"], horizontal=True)
    
    FAF_n = st.radio("Activité physique hebdomadaire (en jour):", ["jamais", "1 à 2", "2 à 4", "4 à 5"], index=1, horizontal=True)

    TUE_n = st.radio("Temps quotidien d'utilisation d'appareils (en heure):", ["0 à 2", "3 à 5", "plus de 5"], index=1, horizontal=True)
    st.caption("Appareils mobiles, jeux vidéo, TV, ordinateurs, etc.")
    
    CALC_n = st.radio("Consommation d'alcool (avec ou sans repas):", ["jamais", "parfois", "fréquemment", "souvent"], index=1, horizontal=True)
    st.caption("Ajuster la taille de la fenêtre.")
    st.caption("Ajuster la disposition de la liste en tirant ce bandeau vers la droite 👉")

    Transport = st.radio("Transport le plus utilisé:", ["automobile", "motocyclette", "vélo", "en commun", "marche"], horizontal=True)

##################################################
# Traiter les données pour les modèles

# Gender_n
# Réassigner
Gender_n = 0 if Gender_n == 'f' else 1
#st.write(Gender_n, type(Gender_n))

# Age
# Réassigner
Age = int(Age)
#st.write(Age, type(Age))

# Height
# Réassigner
Height = float(Height / 100)
#st.write(Height, type(Height))

# FHWO_n
# Réassigner
FHWO_n = 0 if FHWO_n == 'non' else 1
#st.write(FHWO_n, type(FHWO_n))

# FAVC_n
# Réassigner
FAVC_n = 0 if FAVC_n == 'non' else 1
#st.write(FAVC_n, type(FAVC_n))

# FCVC_n
# Réassigner
if FCVC_n == "jamais":
    FCVC_n = 0
elif FCVC_n == "parfois":
    FCVC_n = 1
elif FCVC_n == "souvent":
    FCVC_n = 2
#st.write(FCVC_n, type(FCVC_n))

# NCP_n
# Réassigner
if NCP_n == "1":
    NCP_n = 1
elif NCP_n == "2":
    NCP_n = 2
elif NCP_n == "3":
    NCP_n = 3
elif NCP_n == "4 et plus":
    NCP_n = 4
#st.write(NCP_n, type(NCP_n))

# CAEC_n
# Réassigner
if CAEC_n == "jamais":
    CAEC_n = 0
elif CAEC_n == "parfois":
    CAEC_n = 1
elif CAEC_n == "fréquemment":
    CAEC_n = 2
elif CAEC_n == "toujours":
    CAEC_n = 3
#st.write(CAEC_n, type(CAEC_n))

# SMOKE_n
# Réassigner
SMOKE_n = 0 if SMOKE_n == 'non' else 1
#st.write(SMOKE_n, type(SMOKE_n))

# CH2O_n
# Réassigner
if CH2O_n == "moins de 1":
    CH2O_n = 1
elif CH2O_n == "1 à 2":
    CH2O_n = 2
elif CH2O_n == "plus de 2":
    CH2O_n = 3
#st.write(CH2O_n,type(CH2O_n))

# SCC_n
# Réassigner
SCC_n = 0 if SCC_n == 'non' else 1
#st.write(SCC_n, type(SCC_n))

# FAF_n
# Réassigner
if FAF_n == "jamais":
    FAF_n = 0
elif FAF_n == "1 à 2":
    FAF_n = 1
elif FAF_n == "2 à 4":
    FAF_n = 2
elif FAF_n == "4 à 5":
    FAF_n = 3
#st.write(FAF_n, type(FAF_n))

# TUE_n
# Réassigner
if TUE_n == "0 à 2":
    TUE_n = 1
elif TUE_n == "3 à 5":
    TUE_n = 2
elif TUE_n == "plus de 5":
    TUE_n = 3
#st.write(TUE_n, type(TUE_n))

# CALC_n
# Réassigner
if CALC_n == "jamais":
    CALC_n = 0
elif CALC_n == "parfois":
    CALC_n = 1
elif CALC_n == "fréquemment":
    CALC_n = 2
elif CALC_n == "souvent":
    CALC_n = 3
#st.write(CALC_n, type(CALC_n))

# Transport
# convertit en
# Automobile_n, Motorbike_n, Bike_n
# Public_Transportation_n, Walking_n
# Réassigner
if Transport == "automobile":
    Automobile_n = 1
    Motorbike_n = 0
    Bike_n = 0
    Public_Transportation_n = 0
    Walking_n = 0
elif Transport == "motocyclette":
    Automobile_n = 0
    Motorbike_n = 1
    Bike_n = 0
    Public_Transportation_n = 0
    Walking_n = 0
elif Transport == "vélo":
    Automobile_n = 0
    Motorbike_n = 0
    Bike_n = 1
    Public_Transportation_n = 0
    Walking_n = 0
elif Transport == "en commun":
    Automobile_n = 0
    Motorbike_n = 0
    Bike_n = 0
    Public_Transportation_n = 1
    Walking_n = 0
elif Transport == "marche":
    Automobile_n = 0
    Motorbike_n = 0
    Bike_n = 0
    Public_Transportation_n = 0
    Walking_n = 1
# !!!Valider
#st.write(Automobile_n, type(Automobile_n))
#st.write(Motorbike_n, type(Motorbike_n))
#st.write(Bike_n, type(Bike_n))
#st.write(Public_Transportation_n, type(Public_Transportation_n))
#st.write(Walking_n, type(Walking_n))

# Nobeyesdad_n et
# Nobeyesdad_n2
Nobeyesdad_n = 1
Nobeyesdad_n2 = 1

# Construire des listes
keys = ["Gender_n", "Age", "Height", "FHWO_n", "FAVC_n", "FCVC_n", "NCP_n", "CAEC_n", "SMOKE_n", "CH2O_n", "SCC_n", "FAF_n", "TUE_n", "CALC_n", "Automobile_n", "Motorbike_n", "Bike_n", "Public_Transportation_n", "Walking_n", "Nobeyesdad_n", "Nobeyesdad_n2"]
values = [Gender_n, Age, Height, FHWO_n, FAVC_n, FCVC_n, NCP_n, CAEC_n, SMOKE_n, CH2O_n, SCC_n, FAF_n, TUE_n, CALC_n, Automobile_n, Motorbike_n, Bike_n, Public_Transportation_n, Walking_n, Nobeyesdad_n, Nobeyesdad_n2]

# Convertir les listes en DataFrame
metriques = pd.DataFrame([values], columns=keys)
# !!!Valider
#st.write(metriques)

##################################################
# Construire l'interface de la page
# 1ere partie
st.title ("Modèles")

st.header("Instructions et résultats")

st.markdown("Changer les métriques dans le bandeau de gauche pour alimenter les modèles. Les métriques colorées ont le plus d'influence sur les prévisions:")

st.caption(":orange[Genre], :orange[Âge], :orange[Taille (en cm)], :orange[Obésité dans la famille (présente ou passée)], Consommation d'aliments hypercaloriques, :orange[Consommation de légumes avec les repas], :orange[Nombre de repas quotidien], :orange[Collations entre les repas], Tabagisme, Consommation quotidienne d'eau (en litre), Surveillance de sa consommation calorique, Activité physique hebdomadaire (en jour), Temps quotidien d'utilisation d'appareils (en heure), Consommation d'alcool (avec ou sans repas) et Transport le plus utilisé.")

##################################################
# Préparer et faire les calculs
class rf_classification:
    """Classe pour créer une instance de données par défaut
    et de modèle prédictif (l'algorithme de Random Forest); la classe
    permet d'importer de nouvelles de données, de les changer
    dans l'attribut d'instance et d'exécuter le modèle prédictif."""
    
    def __init__(self) -> Union[pd.DataFrame, RandomForestClassifier]:
        """Instantier des données de départ ou par défaut
        et un modèle prédictif(l'algorithme de Random Forest)"""

        # Constantes pour créer un DataFrame de données
        COLS: List[str] = ['Gender_n', 'Age', 'Height', 'FHWO_n', 'FAVC_n',
                           'FCVC_n', 'NCP_n', 'CAEC_n', 'SMOKE_n', 'CH2O_n',
                           'SCC_n', 'FAF_n', 'TUE_n', 'CALC_n',
                           'Automobile_n', 'Motorbike_n', 'Bike_n',
                           'Public_Transportation_n', 'Walking_n',
                           'Nobeyesdad_n', 'Nobeyesdad_n2']
        VALS: List[int, float] = [0, 20, 1.75, 0, 0,
                                  1, 3, 1, 0, 1,
                                  0, 1, 3, 1,
                                  0, 0, 0,
                                  4, 0,
                                  1, 1]

        # Attribut de départ ou par défaut
        self.questionnaire: pd.DataFrame\
            = pd.DataFrame(np.array([VALS]), columns=COLS)
        # Attributs
        self.modele_1_prediction: RandomForestClassifier\
            = joblib.load('modele/modele_1_rf.pkl')
        self.modele_2_prediction: RandomForestClassifier\
            = joblib.load('modele/modele_2_rf.pkl')
    

    def importer_changer_donnees(self,
                                 nom_fichier_ext: str,
                                 nom_feuille: str) -> pd.DataFrame:
        """Importer de nouvelles données et
        changer les données avec les nouvelles pour le modèle prédictif"""
        
        #!!!
        self.donnees: pd.DataFrame = pd.read_excel(nom_fichier_ext,
                                                   sheet_name=nom_feuille,
                                                   skiprows=24,
                                                   decimal=',')
        self.questionnaire: pd.DataFrame = self.donnees
        return self.questionnaire
    

    # 1er modèle
    def faire_classification_1(self) -> str:
        """Faire une classification (0 ou 1) avec le modèle prédictif 1
        et les données dans les attributs de l'instance"""
        
        donnees: pd.DataFrame = self.questionnaire
        donnees2: pd.DataFrame =\
            donnees.rename(columns={'Nobeyesdad_n': 'NObeyesdad_n',
                                    'Nobeyesdad_n2': 'NObeyesdad_n2'})
        donnees3: pd.DataFrame =\
            donnees2.drop(labels=['NObeyesdad_n', 'NObeyesdad_n2'], axis=1)
    
        self.resultat: RandomForestClassifier =\
            self.modele_1_prediction.predict(donnees3)
        if int(self.resultat) == 0:
            return "non-obèse"
        else:
            return "obèse"


    # 2e modèle
    def faire_classification_2(self) -> str:
        """Faire une classification (1,2,3,4,5,6,7) avec le modèle prédictif 2
        et les données dans les attributs de l'instance"""
        
        donnees: pd.DataFrame = self.questionnaire
        donnees2: pd.DataFrame =\
            donnees.rename(columns={'Nobeyesdad_n': 'NObeyesdad_n',
                                    'Nobeyesdad_n2': 'NObeyesdad_n2'})
        donnees3: pd.DataFrame =\
            donnees2.drop(labels=['NObeyesdad_n', 'NObeyesdad_n2'], axis=1)
    
        self.resultat: RandomForestClassifier =\
            self.modele_2_prediction.predict(donnees3)
        if int(self.resultat) == 1:
            return "poids insuffisant"
        elif int(self.resultat) == 2:
            return "poids normal"
        elif int(self.resultat) == 3:
            return "surpoids de niveau I"
        elif int(self.resultat) == 4:
            return "surpoids de niveau II"
        elif int(self.resultat) == 5:
            return "obésité de type I"
        elif int(self.resultat) == 6:
            return "obésité type de II"
        elif int(self.resultat) == 7:
            return "obésité type de III"


# Instantier
jeu: rf_classification = rf_classification()

# !!!Valider
#st.write("Données par défaut")
#st.write(jeu.questionnaire)
#st.write("Modèles")
#st.write(jeu.modele_1_prediction)
#st.write(jeu.modele_2_prediction)

# Entrer le métrique du bandeau de gauche
jeu.questionnaire = metriques

# !!!Valider
#st.write("Nouvelles données")
#st.write(jeu.questionnaire)

# !!!Valider
#st.write("Prévision")
#st.write(jeu.faire_classification_1())
#st.write(jeu.faire_classification_2())

##################################################
# Construire l'interface de la page
# 2e partie
col1, col2 = st.columns(2)

with col1:
    st.subheader("Modèle (1) binomial")
    st.markdown(f"**Résultat**: :orange[{jeu.faire_classification_1()}]")
    st.markdown("0: non-obèse<br> 1: obèse", unsafe_allow_html=True)
    st.image("img/random-forests.png", caption="Random Forests", width=200)


with col2:
    st.subheader("Modèle (2) multinomial")
    st.markdown(f"**Résultat**: :orange[{jeu.faire_classification_2()}]")
    st.markdown("1: poids insuffisant<br> 2: poids normal<br> 3: surpoids de niveau I<br> 4: surpoids de niveau II<br> 5: obésité de type I<br> 6: obésité type de II<br> 7: obésité type de III<br> Selon une classification basée sur<br> l'Indice de Masse Corporelle<br> (IMC = Poids/Taille<sup>2</sup>).", unsafe_allow_html=True)

st.header("Description")

st.markdown("Les 2 modèles permettent de prédire (classification) la catégorie de poids (actuelle ou future) à partir de métriques de son hygiène de vie.<br><br> Il faut d'abord entrainer les modèles avec les données d'individus dont on connait l'Indice de Masse Corporelle (IMC) avec 19 *features*: les mêmes métriques que ceux dans le bandeau de gauche.<br><br> Les modèles sont testés, validés, puis sauvegardés en format Pickle (format binaire). Les modèles peuvent être importés comme des données. On peut leur attribuer de nouvelles données pour obtenir des prévisions.", unsafe_allow_html=True)

st.subheader("Quelques bémols...")

st.markdown("Avec un jeu de données modeste de 2111 observations (1688 pour l'entrainement et 423 pour les tests), les 2 modèles sont à prendre avec un grain de sel. L'objectif principal est de concrétiser un projet d'analyses des données et de *Machine Learning*, puis de le rendre opérationnel avec ce site web interactif.<br><br> Le Modèle (1) binomial donne un score de justesse de 94.3%. Le Modèle (2) multinomial donne un score de justesse de 84.2%. Les scores sont calculés à partir des matrices de confusion sur le jeu de données de test de 423 observations, ci-dessous.", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image("img/matrice1.png", caption="Matrice de confusion 1", use_column_width=True)

with col2:
    st.image("img/matrice2.png", caption="Matrice de confusion 2", use_column_width=True)

st.markdown(
    "De plus, comme les modèles ont été entrainés avec une métrique Âge dont la moyenne-médiane est de 24.3-22.8 avec un 1er quartiles à 20 et un 3e quartiles à 26, la surreprésentation des vingtenaires dans l'entrainement biaise les prévisions avec d'autres groupes d'âge. D'autant plus que dans les 2 modèles, l'âge demeure le facteur explicatif (*feature*) prépondérant.<br><br> Les 5 premiers facteurs d'impact (en ordre) du Modèle 1: :orange[Âge], :orange[Taille], :orange[Obésité dans la famille (présente ou passée)], :orange[Nombre de repas quotidien] et :orange[Collations entre les repas]. Les 5 premiers facteurs d'impact (en ordre) du Modèle 2: :orange[Âge], :orange[Taille], :orange[Obésité dans la famille (présente ou passée)], :orange[Genre] et :orange[Consommation de légumes avec les repas]. En d'autres mots, ce sont les métriques qui ont le plus d'influence sur les prévisions.", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image("img/modele1.png", caption="Modele 1 - % d'influence (sur 100%)", use_column_width=True)

with col2:
    st.image("img/modele2.png", caption="Modele 2 - % d'influence (sur 100%)", use_column_width=True)
