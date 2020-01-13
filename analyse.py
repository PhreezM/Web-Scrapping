#import pandas
import pandas as pd

def main():
    print("start")
    df = pd.read_csv('recup.csv')
    df.drop(columns=["Unnamed: 0"], inplace=True)
    print("Tableau non trier ")
    print(df)
    #Recuperer 5 premier caracteres 
    df.head()
    #Recuperer 5 derniers caracteres 
    df.tail
    #Recuperer structure global
    print(df.shape)
    #Vérifier la présence de doublon
    print(df.duplicated().sum())
    #Suppression des doublons 
    df.drop_duplicates(inplace = True)

    #Vérifier le nombre de valeur null 
    print(df.isnull().sum())

    #.dropna() qui supprime toutes les valeurs manquants du DataFrame:
    df.dropna(inplace=True)
    #On Vérifie qu'il n y a plus de valeurs null
    print(df.isnull().sum())

    df = df.apply(pd.to_numeric, errors='ignore')

    #Vérifier que le bien est conforme
    #df = df[df['MetreCarre'] >= 9.0]
    print("Tableau  trier ")
    print(df)

    df.to_csv('recup_clean.csv')

main()
print("end")