from tkinter import *
from tkinter import messagebox
import os
os.chdir("/home/isko/Documents/Mini_Projet_Python_Avec_Interface_Final")
import sqlite3
import Classe_Objet
import Requetes



## ****** Les fonctions des Bouttons ******

#Valider formulaire d'authentification
def valider():
    global entree1
    global entree2
    username = entree1.get() # recupère la donnée saisie pour le username
    password = entree2.get() # recupère la donnée saisie pour le password
    personne = Classe_Objet.Utilisateur(" ", " ", " ", " ", " ") #Créaton d'un utilisateur quelconque
    Admin = personne.SeLogger(username, password) #fonction qui revoie vrai si c'est bien l'admin qui s'authentifie
    if(Admin):
        pageAdmin()
    elif(username == "" and password ==""):
        messagebox.showinfo("", "Veuillez remplir les champs") #affiche un message à l'ecran
    else:
        messagebox.showinfo("", "Vous etes un simple membre de la Mairie")
        pageNonAdmin()

#Ajoute les données saisies dans la base de donnée
def Ajouter():
    global entree1
    global entree2
    global entree3
    global entree4
    E1 = entree1.get()
    E2 = entree2.get()
    E3 = entree3.get()
    E4 = entree4.get()
    evenement = Classe_Objet.Evenement(E1, E2, E3, E4) #créattion d'objet évènement
    Ajouter_evenement(evenement) # Fonction qui recupère un objet puis le stocke dans la base de donnée
    messagebox.showinfo("", " Evènenment ajouté")

#Modifie les données saisies dans la base de donnée
def Modifier():
    global entree1
    global entree2
    global entree3
    global entree4
    E1 = entree1.get()
    E2 = entree2.get()
    E3 = entree3.get()
    E4 = entree4.get()
    evenement = Classe_Objet.Evenement(E1, E2, E3, E4)
    Modifier_evenement(evenement, event_id) #Fonction qui recupère un objet et son indince puis le modifie dans la base de donnée
    messagebox.showinfo("", " Evènenment modifé")

#Supprime une donnée dans la base de donnée
def Supprimer():
    Supprimer_evenement(event_id) #Fonction qui recupère l'indice d'un objet puis le supprime dans la base de donnée
    messagebox.showinfo("", " Evènenment supprimé")

#affiche les données de la base dans une une listBox
def AfficheDansInterface(listeboxe):
    a = Liste_evenement()
    for i in a:
        listeboxe.insert('end' ,i)

#affiche les données après operations effectués sur la base de données
def Consulter():
    donnes = Liste_evenement()
    for i in donnes:
        print(i)

#Vide le contenu des champs saisis aprés avoir ajouté ou modifié un évènement
def Initialiser():
    entree1.delete (0, END)
    entree2.delete (0, END)
    entree3.delete (0, END)
    entree4.delete (0, END)
    entree1.focus_set()

#Enreigistrer l'utiliisateur dans la base de donnée
def Sauvegarder():
    global entree1
    global entree2
    global entree3
    global entree4
    global entree5
    E1 = entree1.get()
    E2 = entree2.get()
    E3 = entree3.get()
    E4 = entree4.get()
    E5 = entree5.get()
    user = Classe_Objet.Utilisateur(E1, E2, E3, E4, E5)
    Ajouter_utilisateur(user)
    messagebox.showinfo("", " Utilisateur ajouté")

#Interface pour ajouter un utilisateur
def Add_user():
    global entree1
    global entree2
    global entree3
    global entree4
    global entree5

    #la fenetre ajout utilisateur
    fen = Tk()
    fen.title("Ajouter Utilisateur")
    fen.eval('tk::PlaceWindow . center') #center la fenetre
    fen.geometry('550x350')
    fen['bg'] = '#808000'

    #Formulaire a remplir
    #creaction et positionnement des labels
    L1 = Label(fen, text=" Nom : ", bg = 'white')
    L1.grid (row = 2, column = 1, padx = 20, pady = 15)

    L2 = Label(fen, text=" Prenom : ", bg = 'white')
    L2.grid (row = 3, column = 1, padx = 20, pady = 15)

    L3 = Label(fen, text=" Adresse: ", bg = 'white')
    L3.grid (row = 4, column = 1, padx = 20, pady = 15)

    L4 = Label(fen, text=" Date début : ", bg = 'white')
    L4.grid (row = 5, column = 1, padx = 20, pady = 15)

    L5 = Label(fen, text=" Date fin : ", bg = 'white')
    L5.grid (row = 6, column = 1, padx = 20, pady = 15)

    #creation et posionnement des champs pour la saisie des valeurs
    entree1 = Entry(fen, width = 20)
    entree1.grid (row = 2, column = 2, padx = 20, pady = 5)

    entree2 = Entry(fen, width = 20)
    entree2.grid (row = 3, column = 2, padx = 20, pady = 5)

    entree3 = Entry(fen, width = 20)
    entree3.grid (row = 4, column = 2, padx = 20, pady = 5)

    entree4 = Entry(fen, width = 20)
    entree4.grid (row = 5, column = 2, padx = 20, pady = 5)

    entree5 = Entry(fen, width = 20)
    entree5.grid (row = 6, column = 2, padx = 20, pady = 5)

    # le cannevas sera utliser pour inserer une photo du nouvel user
    cannevasImg = Canvas (fen, width = 120, height = 120, bg = "ivory")
    cannevasImg.grid(row = 1, column = 4, rowspan = 3, padx = 10, pady = 10)

    #creation et postionnement des bouttons(contiennent des fonctions)
    bouton1 = Button(fen, text = 'Enreigistrer', bg = 'white', command = Sauvegarder)
    bouton1.grid(row = 4, column = 4, padx = 10, pady = 10)

    bouton2 = Button(fen, text = 'Fermer', bg = 'white', command = fen.destroy)
    bouton2.grid(row = 5, column = 4, padx = 10, pady = 10)

    bouton3 = Button(fen, text = 'Réinitialiser', bg = 'white', command = Initialiser)
    bouton3.grid(row = 6, column = 4, padx = 10, pady = 10)

    fen.mainloop()

## ***** Page admin ******

#Interface de l'administrateur
def pageAdmin():
    global entree1
    global entree2
    global entree3
    global entree4

    fen = Tk () # la fenêtre de l'admin
    fen.title('Admin')
    fen.geometry('925x500')

    #creation et posionnement des Frame(conteneurs qui permettent de séparer des éléments)
    main = Frame(fen, bg = '#8FBC8F', bd = 5, width = 925, height = 500, relief = RIDGE)
    main.pack()

    #Cadre des fenetre 2 et 3
    fenetre1 = Frame(main, bg = 'white', bd = 5, width = 925, height = 250, relief = RIDGE)
    fenetre1.pack(side = TOP)

    #Pour les labels et les champs de saisies
    fenetre2 = Frame(fenetre1, bg = '#8FBC8F', bd = 5, width = 725, height = 250, relief = RIDGE)
    fenetre2.pack(side = LEFT)

    #Pour les boutons
    fenetre3 = Frame(fenetre1, bg = '#FFD700', bd = 5, width = 200, height = 250, relief = RIDGE)
    fenetre3.pack(side = RIGHT)

    #Pour la listBox
    fenetre4 = Frame(main, bg = 'white', width = 925, bd = 5, height = 300, relief = RIDGE)
    fenetre4.pack(side = BOTTOM)

    #creation et postionnement des labels dans la feentre2
    L1 = Label(fenetre2, text=" Type Evenement : ", bg = 'white')
    L1.grid (row = 2, column = 1, padx = 20, pady = 15) #positionnement du label dans la fenetre2

    L2 = Label(fenetre2, text=" Nom : ", bg = 'white')
    L2.grid (row = 3, column = 1, padx = 20, pady = 15)

    L3 = Label(fenetre2, text=" Date Evenement : ", bg = 'white')
    L3.grid (row = 4, column = 1, padx = 20, pady = 15)

    L4 = Label(fenetre2, text=" Nom de l'Animateur : ", bg = 'white')
    L4.grid (row = 5, column = 1, padx = 20, pady = 15)

    #creation et posionnement des champs pour la saisie des valeurs dans la fenetre2
    entree1 = Entry(fenetre2, width = 30)
    entree1.grid (row = 2, column = 2, padx = 40, pady = 5)

    entree2 = Entry(fenetre2, width = 30)
    entree2.grid (row = 3, column = 2, padx = 40, pady = 5)

    entree3 = Entry(fenetre2, width = 30)
    entree3.grid (row = 4, column = 2, padx = 40, pady = 5)

    entree4 = Entry(fenetre2, width = 30)
    entree4.grid (row = 5, column = 2, padx = 40, pady = 5)

    #creation et postionnement des bouttons dans la fenetre3
    bouton1 = Button(fenetre3, text = 'Ajouter Evenement', bg = 'white', command = Ajouter)
    bouton1.grid(row = 2, column = 6,  pady = 10)

    bouton2 = Button(fenetre3, text = 'Modifier Evenement', bg = 'white', command = Modifier )
    bouton2.grid(row = 3, column = 6, padx = 10, pady = 10)

    bouton3 = Button(fenetre3, text = 'Supprimer Evenement', bg = 'white',command = Supprimer)
    bouton3.grid(row = 4, column = 6, padx = 10, pady = 10)

    bouton4 = Button(fenetre3, text = 'Consulter Evenements', bg = 'white', command = Consulter )
    bouton4.grid(row = 3, column = 7, pady = 10)

    bouton5 = Button(fenetre3, text = 'Ajouter Utlisateur', bg = 'white', command = Add_user)
    bouton5.grid(row = 5, column = 6, padx = 10, pady = 10)

    bouton6 = Button(fenetre3, text = 'Réinitialiser', bg = 'white', command = Initialiser)
    bouton6.grid(row = 4, column = 7, padx = 10, pady = 10)

    bouton7 = Button(fenetre3, text = 'Fermer', bg = 'white', command = fen.destroy)
    bouton7.grid(row = 5, column = 7, padx = 10, pady = 10)

    #Récuperer l'indice et la valeur que contient l'indice
    event_id = 0
    def Selectionner_evenement(event):
        global event_id
        value = donne.curselection() #recupère l'indice
        data = donne.get(value)     # recupère la valeur à cet indice
        event_id = data[0]
        return data

    #listeBox pour afficher les données dans la fenetre4
    donne = Listbox(fenetre4, width = 500, bg='ivory', selectmode="SINGLE")
    donne.bind('<<ListboxSelect>>', Selectionner_evenement)
    donne.pack()
    AfficheDansInterface(donne)

    fen.mainloop()

## ***** Page non admin *****

#Interface des membres de la mairie qui ne sont pas administrateur
def pageNonAdmin():
    global entree1
    global entree2
    global entree3
    global entree4

    fen = Tk ()
    fen.title('Membre')
    fen.geometry('750x500')
    fen['bg']= '#EEE8AA'

    main = Frame(fen, bd = 5, width = 750, height = 500, relief = RIDGE)
    main.pack()

    #Pour les fenetre 2 et 3
    fenetre1 = Frame(main, bg = 'white', bd = 5, width = 750, height = 300, relief = RIDGE)
    fenetre1.pack(side = TOP)

    #Pour les labels et les champs de saisies
    fenetre2 = Frame(fenetre1, bg = '#EEE8AA', bd = 5, width = 450, height = 300, relief = RIDGE)
    fenetre2.pack(side = LEFT)

    #Pour les boutons
    fenetre3 = Frame(fenetre1, bg = 'orange', bd = 5, width = 300, height = 300, relief = RIDGE)
    fenetre3.pack(side = RIGHT)

    #Pour la listBox
    fenetre4 = Frame(main, bg = 'white', width = 750, bd = 5, height = 200, relief = RIDGE)
    fenetre4.pack(side = BOTTOM)

    L1 = Label(fenetre2 , text=" Type Evenement : ", bg = 'white')
    L1.grid (row = 2, column = 1, padx = 20, pady = 15)

    L2 = Label(fenetre2 , text=" Nom : ", bg = 'white')
    L2.grid (row = 3, column = 1, padx = 20, pady = 15)

    L3 = Label(fenetre2 , text=" Date Evenement : ", bg = 'white')
    L3.grid (row = 4, column = 1, padx = 20, pady = 15)

    L4 = Label(fenetre2 , text=" Nom de l'Animateur : ", bg = 'white')
    L4.grid (row = 5, column = 1, padx = 20, pady = 15)

    entree1 = Entry(fenetre2 , width = 30)
    entree1.grid (row = 2, column = 2, padx = 40, pady = 15)

    entree2 = Entry(fenetre2 , width = 30)
    entree2.grid (row = 3, column = 2, padx = 40, pady = 15)

    entree3 = Entry(fenetre2 , width = 30)
    entree3.grid (row = 4, column = 2, padx = 40, pady = 15)

    entree4 = Entry(fenetre2 , width = 30)
    entree4.grid (row = 5, column = 2, padx = 40, pady = 15)

    bouton1 = Button(fenetre3, text = 'Ajouter Evenement', command = Ajouter)
    bouton1.grid(row = 2, column = 4, padx = 15, pady = 15)

    bouton2 = Button(fenetre3, text = 'Modifier Evenement', command = Modifier)
    bouton2.grid(row = 3, column = 4, padx = 15, pady = 15)

    bouton3 = Button(fenetre3, text = 'Réinitialiser', command = Initialiser)
    bouton3.grid(row = 4, column = 4, padx = 15, pady = 15)

    bouton4 = Button(fenetre3, text = 'Fermer', command = fen.destroy)
    bouton4.grid(row = 5, column = 4, padx = 15, pady = 5)

    #Affichage LstBox
    event_id = 0
    def Selectionner_evenement(event):
        global event_id
        value = donne.curselection() #recupère l'indice
        data = donne.get(value)     # recupère la valeur à cet indice
        event_id = data[0]
        return data

    donne = Listbox(fenetre4, width = 500, bg='ivory', selectmode="SINGLE")
    donne.bind('<<ListboxSelect>>', Selectionner_evenement)
    donne.pack()
    AfficheDansInterface(donne)
    fen.mainloop()


## ******* main() *****

#page d'acceuille => l'étape de l'authentification
fenetre = Tk()
fenetre.title('Authentificattion')
fenetre.eval('tk::PlaceWindow . center')    #center la fenetre
fenetre.geometry("480x200")
fenetre['bg']= '#87CEEB'

#formulaire de la connexion
L1 = Label(fenetre, text=" Username  ")
L1.grid (row = 1,column = 1, sticky = "E", padx = 10, pady = 5)

L2 = Label(fenetre, text=" Password  ")
L2.grid (row = 2, column = 1, sticky = "E", padx = 10, pady = 5)

#Les champs de saisies
entree1 = Entry(fenetre)
entree1.grid (row = 1, column = 2)

entree2 = Entry(fenetre)
entree2.grid (row = 2, column = 2)
entree2.config(show="*") #cache les caractère lors de la saisie du mot de passe

# le cannevas sera utliser pour inserer une image
cannevasImg = Canvas (fenetre, width =190, height = 150, bg = "ivory")
logo = PhotoImage (file="/home/isko/Documents/Mini_Projet_Python_Avec_Interface_Final/imageMairie1.png") #le chemin ou se trouve l'imaage
image = cannevasImg.create_image(88, 80, anchor = CENTER, image = logo) #place l'image sur la page actuelle
cannevasImg.grid(row = 1, column = 3, rowspan = 3, padx = 10, pady = 10)

boutonValider = Button (fenetre, text=' Connexion ', command = valider)
boutonValider.grid (row = 3, column = 2, pady = 10)

boutonQuitter = Button (fenetre, text=' Quitter ', command = fenetre.destroy)
boutonQuitter.grid (row = 3, column = 1, padx = 10, pady = 10)


#Connexion à la base de donnée
connexion = sqlite3.connect("/home/isko/Documents/Mini_Projet_Python_Avec_Interface_Final/cinema.db")
curseur_user = connexion.cursor()
curseur_user.execute(""" CREATE TABLE IF NOT EXISTS Utilisateurs(
                Id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
                Nom           TEXT NOT NULL ,
                Prenom        TEXT NOT NULL ,
                Adresse       TEXT NOT NULL ,
                date_debut    NUMERIC NOT NULL ,
                date_fin      NUMERIC NOT NULL
                    )""" )


connexion = sqlite3.connect("/home/isko/Documents/Mini_Projet_Python_Avec_Interface_Final/cinema.db")
curseur = connexion.cursor()
curseur.execute(""" CREATE TABLE IF NOT EXISTS Evenements(
                Id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
                Type_event          TEXT NOT NULL ,
                Nom_event           TEXT NOT NULL ,
                Date_event    NUMERIC NOT NULL ,
                Id_User       INTEGER NOT NULL,
                CONSTRAINT Evenement_User_FK FOREIGN KEY (id_User) REFERENCES User(id)
                )""" )


fenetre.mainloop()  #Lancement du gestionnaire d'événements
connexion.commit()
connexion.close()   #fermuture de la base de donnée


