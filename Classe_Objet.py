class Evenement:
    def __init__(self, type, nom, date_event, animateur):
        self.type = type # pour définir les différents évènements
        self.nom = nom #nom de l'évènement en fonction du type
        self.date_event = date_event
        self.animateur = animateur

class Utilisateur:
    def __init__(self, nom, prenom, adresse, date_debut, date_fin):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.date_debut = date_debut
        self.date_fin = date_fin

    def SeLogger(self, user, mdp):
        self.user = user
        self.mdp = mdp
        if(self.user == "admin" and self.mdp == "Admin02"):
            return True
        else:
           return False


"""
Pour définir un évènement par exemple selon mon modèle :
1.
type = Film
Nom = Avangers
Date_event(Date de projection) = 2021-04-10
animateur = Paul

2.
type = Debat
Nom(Thème_debat) = Le bonheur
Date_event = 2021-04-20
animateur = Jean

3.
type = Presentation Auteur
Nom(Auteur) = Victor Huguo
Date_event = 2021-05-01
animateur = Marie

"""
