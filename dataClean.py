#%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("start")
#Création d'un diagramme circulaire :
#df = dataframe
def diagCirul(df):
 df["Lieu"].value_counts(normalize=True).plot(kind='pie',shadow=False, startangle=90,autopct='%1.1f%%')

#Création d'un nuage de points
def nuagePoints(df):
 df.plot.scatter(x='MetreCarre',y='Prix')
 plt.title('nuage de points représentant le prix en fonction du m2\n')
 plt.show()


#Matrice de corrélation
def matCorr(df):
 sns.heatmap(df.corr(), annot=True, cmap='Blues')
 plt.title("Matrice de corrélation entre les différentes caractéristiques des annonces\n", fontsize=18, color='#009432')
 #Les couleurs sont bien choisies du plus foncé pour une forte corrélation au plus clair pour une faible corrélation.
 #prix en fonction du code postal
 plt.figure(figsize=(10,6))
 sns.barplot(x=df['CP'], y=df['Prix'], palette="Reds_r")
 plt.xlabel('\nCode Postal', fontsize=15, color='#c0392b')
 plt.ylabel("Prix \n", fontsize=15, color='#c0392b')
 plt.title("Prix en fonction du code postal\n", fontsize=18, color='#e74c3c')
 plt.xticks(rotation= 45)
 plt.tight_layout()
 
def lm(df):
    plt.figure(figsize=(10,6))
    sns.barplot(x=df['MetreCarre'], y=df['Prix'], palette="Reds_r")
    plt.xlabel('M2', fontsize=15, color='#c0392b')
    plt.ylabel("Prix\n", fontsize=15, color='#c0392b')
    plt.title("Prix selon le M2\n", fontsize=18, color='#e74c3c')
    plt.xticks(rotation= 45)
    plt.tight_layout()
   

#Nombre d'annonces par département 
def annDept(df):
    nbr = df[['Prix','Lieu']].groupby('Lieu').count().sort_values(by='Prix', ascending=False)
    nbr.reset_index(0, inplace=True)
    nbr.rename(columns={'Prix':'Nb_annonces'}, inplace=True)
    #print(nbr.head())

    plt.figure(figsize=(10,6))
    sns.barplot(x=nbr['Lieu'], y=nbr['Nb_annonces'], palette="Reds_r")
    plt.xlabel('\nArrondissements', fontsize=15, color='#c0392b')
    plt.ylabel("Nombre d'annonces\n", fontsize=15, color='#c0392b')
    plt.title("Nombre d'annonces par département \n", fontsize=18, color='#e74c3c')
    plt.xticks(rotation= 45)
    plt.tight_layout()

def annM2(df):
    nbr = df[['Prix','MetreCarre']].groupby('MetreCarre').count().sort_values(by='Prix', ascending=False)
    nbr.reset_index(0, inplace=True)
    nbr.rename(columns={'Prix':'Nb_annonces'}, inplace=True)
    print(nbr.head())

    plt.figure(figsize=(10,6))
    sns.barplot(x=nbr['MetreCarre'], y=nbr['Nb_annonces'])
    plt.xlabel('MetreCarre', fontsize=15, color='#c0392b')
    plt.ylabel("Nombre d'annonces\n", fontsize=15, color='#c0392b')
    plt.title("Nombre d'annonces par m2 \n", fontsize=18, color='#e74c3c')
    plt.xticks(rotation= 45)
    plt.tight_layout()


def main():
    #lecture du fichier csv
    df = pd.read_csv('recup_clean.csv')
    #Supprimer colonne en trop
    df.drop(columns=["Unnamed: 0"], inplace=True)
    #afficher 5 premieres lignes
    #print(df.head())
    #Afficher dataframe
    #print(df)
    
    #On appelle maintenant les fonctions permettant d'afficher les graphiques
    diagCirul(df)
    nuagePoints(df)
    matCorr(df)
    annDept(df)
    annM2(df)
    lm(df)
    plt.show()
    #On affiche les figures
   

main()

print("end")