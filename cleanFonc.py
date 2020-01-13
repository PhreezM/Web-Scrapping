print("This line will be printed.") 
import pandas as pd
import itertools as it
import random
import time
import requests
import re
import bs4
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#print("Error 403") 
#from urllib.request import urlopen, HTTPError, URLError
#
#try:
#    myURL = urlopen("https://www.stephaneplazaimmobilier.com/immobilier-acheter?target=buy&type=2,1&room_min=2&location=75056&now=1&page=1")
#except HTTPError as e:
#    print('HTTP Error code: ', e.code)
#except URLError as e:
#    print('URL Error: ', e.reason)
#else:
#    print('No Error.')

#token2 = 'https://www.superimmo.com/achat/ile-de-france/p/'
#token2 = 'https://www.superimmo.com/location/ile-de-france/p/'
print("Start")
def get_pages( nb):
    token = 'https://www.superimmo.com/achat/ile-de-france/p/'
    pages = []
    for i in range(1,nb+1):
        j = token + str(i)
        pages.append(j)
    return pages

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

#il faut trouver : prix superficie ville département taille typeBiens  
#reste à trouver    taille (nombre pieces)
#########################################################
def traitPieces():
 html = open("Pieces.html").read()
 soup = BeautifulSoup(html, 'html.parser')
 label = soup.find_all('p', class_="media-heading")
 #print(label)
 fichier = open("atrait.html", "w")   
 fichier.write(str(label))
 fichier.close()
 htmlp = open("atrait.html").read()
 soupp = BeautifulSoup(htmlp, 'html.parser')
 array = []
 for i in range(0,10):
  lab2 = soupp.findAll("b", {"class":"titre"})[i].next.next.next.next
  #print(lab2.strip())
  array.append(lab2.strip())
  
 return array



def traitpiecesArray(mot):
    if mot == "m" or mot == "M" :
        return("")
    else:
            return(mot)
        
def traitChambreArray(mot):
    if mot == "2piè"  :
        return("2")
    else:
            return(mot)

def traitChambreArray(mot):
    print(mot)
    if mot == "1piè":
        return(1)
    elif  mot == "2iè":
            return(2)
    elif  mot == "3piè":
            return(3)
    elif  mot == "4piè":
            return(4)
    else:
            return("")

def traitChambreArray(mot):

    if len(mot) > 1 :
        return mot[0]
    elif  mot == 0:
        return ""
    else:
            return(mot)

        
def piecesArray(allo):
    longueurArray = len(allo)
    pieceTableau = []
    for num in range(longueurArray):
       #print(allo[num])
       try:
        test = traitpiecesArray(allo[num][0])
        pieceTableau.append(test)
       except:
        print("exe")
    #print(pieceTableau)
    return pieceTableau

def chambreArray(allo):
    longueurArray = len(allo)
    chambreTableau = []
    for num in range(longueurArray):
       #print(allo[num])
       string = allo[num].replace(" ", "")
       ss =  find_between( string, "-", "c" )
       sss = traitChambreArray(ss)
       chambreTableau.append(sss)
    #print(pieceTableau)
    return chambreTableau
  
# fonction principale qui permet de "tout lancer"
def my_function(response,famille_panda):
    #on recupere la réponse sous format texte on utilise html.parser pour la parser
    # cette réponse est utiliser pour créer un objet BeautifulSoup appeler soup
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # on ouvre un fichier html pour écrire cette réponse
    # le w signifie que l'on écrase a chaque fois le contenu précédent
    fichier = open("Pieces.html", "w")   
    fichier.write(response.text)
    fichier.close()
    #on récupere deux variables contenant respectivement
    #t1 la liste de toutes les pieces de toutes les annonces selon les requetes effectuer 
    #t2 la liste de toutes les chambres de toutes les annonces selon les requetes effectuer 
    t1 = piecesArray(traitPieces())
    t2 = chambreArray(traitPieces())
    #On récupere maitenant 3 autres variables qui correspondent : 
    #La liste des prix
    #le type de bien ainsi que le metre carrée 
    #Le lieu du bien ( Ville + Code postal)
    prixArrayFunction2 = prixArrayFunction(soup)
    typeMetreCarreArrayFunction2 = typeMetreCarreArrayFunction(soup)
    lieuArrayFunction2 = lieuArrayFunction(soup)
    #famille_panda2 = []
    # On crée un array Tableau qui contiendra la réponse à l'appel de fonction afficher
    # les parametres sont les 5 variables que l'on vient de voir précédemment ainsi que le tableau que l'on a recu en parametre que l'on va mettre à jour
    Tableau = afficher(prixArrayFunction2,typeMetreCarreArrayFunction2,lieuArrayFunction2,t1,t2,famille_panda)
    #On appelle ensutie la fonction ecriturefamille_panda_df pour écrire le tableau précedent dans du csv
    ecriturefamille_panda_df(Tableau)
    #On affiche ensuite le tableau à l'utilisateur
    print(Tableau)
    
    
    #########################################################
    #print(afficher(prixArrayFunction2,typeMetreCarreArrayFunction2,lieuArrayFunction2,famille_panda))
   
# filtre map reduce 
###############################################################
#Les fonctions suivantes vont nous permettre de récuper 3 tableaux dans les quels il y'aura respectivement
#La liste de tous les prix 
#La liste contenant les metres carrées
#La lsite contenant le lieu (Ville + code postal)

def prixArrayFunction(bSoup):
    #soup = bSoup
    prix = bSoup.find_all("b", {"class":"prix"})
    prixArray = []
    for index in range(len(prix)): 
        prixArray.append(prix[index].getText())
        #print(prix[index].getText())
    return  prixArray

def typeMetreCarreArrayFunction(bSoup):
    #soup = bSoup
    typeMetreCarre = bSoup.find_all("b", {"class":"titre"})
    typeMetreCarreArray = []
    for index in range(len(typeMetreCarre)): 
        typeMetreCarreArray.append(typeMetreCarre[index].getText())
    
    return  typeMetreCarreArray

def lieuArrayFunction(bSoup):
    #soup = bSoup
    html = bSoup.find_all('div', class_='media-body')
    fichier = open("recuperationLieu.html", "w")   
    fichier.write(str(html))
    fichier.close()
    htmlp = open("recuperationLieu.html").read()
    soupp = BeautifulSoup(htmlp, 'html.parser')
    lieuArray=[]
    for tag in soupp.p.find_all_next('b',class_=None):
        lieuArray.append(tag.getText())
    
    return  lieuArray
###############################################################
#Fonctions de traitements 
def trait(mot):
    if mot[0] == "a" or mot[0] == "A" :
        return("Appartement")
    elif  mot[0] == "m" or mot[0] == "M":
            return("Maison")
    else:
            return("")

def traitPrix(mot):
    return re.sub("[^0-9]", "",mot)

def traitLieu(mot):
    #re.search(r'(?<=())\w+',lieuArrayFunction2[index])[0],
    return re.search(r'(?<=())\w+',mot)[0]

def traitCP(mot):
    #find_between( lieuArrayFunction2[index], "(", ")" )
    return find_between(mot,"(", ")" )
    
#re = expression réguilière
#Les expressions régulières, ou plus communément regex (contraction de regular expression) permettent de représenter des modèles de chaînes de caractère.
def traitMetreCar(mot):
    trait1 = re.sub("[^0-9^,]", "",mot)
    trait2 = trait1.replace(",",".")
    return trait2
###############################################################
#Fonction qui permet de mettre à jour le tableau famille_pandaqui contient les données  concernant Prix','Lieu','CP','Type','MetreCarre','Pieces','Chambres'

def afficher(prixArrayFunction2,typeMetreCarreArrayFunction2,lieuArrayFunction2,t1,t2,famille_panda):
    #Chaque tableau fait la meme taille car on travaille sur un nombre fixe d'annonces par pages
    #On peut donc boucler sur la taille d'un seul tableau
    #On mettra à jour le tableau en fonction des parametres, ces derniers seront utilisées dans les fonction trait** qui permettront de garder que le nécessaire
    for index in range(len(typeMetreCarreArrayFunction2)): 
        famille_panda.append([traitPrix(prixArrayFunction2[index]),traitLieu(lieuArrayFunction2[index]),traitCP(lieuArrayFunction2[index]),re.sub("[^a-z^A-Z]", "",trait(typeMetreCarreArrayFunction2[index])),traitMetreCar(typeMetreCarreArrayFunction2[index]),t1[index],t2[index]])
    
    famille_panda_df = pd.DataFrame(famille_panda)
    famille_panda_df.columns = ['Prix','Lieu','CP','Type','MetreCarre','Pieces','Chambres']
    #print(famille_panda_df)
    return famille_panda_df

#Fonction qui permet d'enrengistrer le tableau en format csv et en format text
def ecriturefamille_panda_df(famille_panda):

    famille_panda_df = pd.DataFrame(famille_panda)
    famille_panda_df.to_csv('recup.csv', encoding='utf-8')
    fichier = open("recuperation.txt", "w")   
    fichier.write(str(famille_panda))
    fichier.close()
    #print("Fichier recuperatiton Fermer")
    


def responseLon():
    #on initialise un tableau que l'on remplira
    famille_panda = []
    # on fait une boucle qui va appeller 5 fois la fonction my_function qui va nous permettre de récuperer les données souhaites
    # a chaque fois que l'appel est effectuer on va passer en parametres
    # la response de la requete effectuer et le tableau que l'on a crée auparavent que l'on completera au fur et a mesurer
    for i in get_pages(5):
        response = requests.get(i)
        my_function(response,famille_panda)
    #print(famille_panda)
 
#Appel de la fonction 
responseLon()

print("end")