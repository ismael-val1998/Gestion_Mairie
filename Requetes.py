import sqlite3
import os
os.chdir("/home/isko/Documents/Mini_Projet_Python_Avec_Interface_Final")
import Classe_Objet


# Ajouter un objet dans la base de donnée
def Ajouter_evenement(a): #prendre un objet de type Evenement tels que defini dans mon fiichier Clase_Objet en paramètre
    with connexion:
        curseur.execute(" INSERT INTO Evenements (Type_event, Nom_event, Date_event, Id_User) VALUES (:Type_event, :Nom_event, :Date_event, :Id_User)",{'Type_event':a.type, 'Nom_event':a.nom,  'Date_event':a.date_event, 'Id_User' :a.animateur})
        print("Evènements Ajouté avec succès ...")

# Modifier un objet dans la base de donnée
def Modifier_evenement(a, id):  #prendre un objet en paramètre et l'identifiant de l'objet
    with connexion:
        curseur.execute(" UPDATE Evenements SET Type_event =:Type_event, Nom_event =:Nom_event, Date_event=:Date_event, Id_User =:Id_User WHERE Id =:Id", {'Type_event':a.type, 'Nom_event':a.nom,  'Date_event':a.date_event, 'Id_User' :a.animateur, 'Id':id})
        print("Evènements Modiifié avec succès ...")

 #Supprime un événement dans la base de donnée en prenant le id de  l'objet en paramètre
def Supprimer_evenement(id):
    with connexion:
        curseur.execute(" DELETE FROM Evenements WHERE Id =:Id", {'Id': id})
        print("Evènements Supprimé avec succès ...")

#Affiche tous les évènements presentent dans la base
def Liste_evenement():
    curseur.execute(" SELECT * FROM Evenements ")
    affiche = curseur.fetchall()
    return affiche


# Ajout un user en prenant un objet de type Utilisateur tels que defini dans mon fiichier Clase_Objet en paramètre
def Ajouter_utilisateur(u):
    with connexion:
        curseur_user.execute(" INSERT INTO Utilisateurs (Nom, Prenom, Adresse, date_debut, date_fin) VALUES (:Nom, :Prenom, :Adresse, :date_debut, :date_fin)", {'Nom':u.nom, 'Prenom':u.prenom, 'Adresse':u.adresse, 'date_debut':u.date_debut, 'date_fin':u.date_fin})
        print("Utilisateur Ajouté avec succès ...")

#Affiche tous les utilisateurs presentent dans la base
def Liste_utilisateur():
    curseur_user.execute(" SELECT * FROM Utilisateurs ")
    affiche = curseur_user.fetchall()
    return affiche

#Affiche l'ensemble des animateur avec leur evenement à gerer
def ResponsableEvenement():
    curseur.execute(" SELECT * FROM Evenements INNER JOIN Utilisateurs on Evenements.Id_User = Utilisateurs.Id")
    affiche = curseur.fetchall()
    for i in affiche:
        print(i)

# creation table utilisateur
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

# creation table évènements
connexion = sqlite3.connect("/home/isko/Documents/Mini_Projet_Python_Avec_Interface_Final/cinema.db")
curseur = connexion.cursor()
curseur.execute(""" CREATE TABLE IF NOT EXISTS Evenements(
                Id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
                Type_event          TEXT NOT NULL ,
                Nom_event           TEXT NOT NULL ,
                Date_event    NUMERIC NOT NULL ,
                Id_User       INTEGER NOT NULL
                )""" )

connexion.commit()
connexion.close()
