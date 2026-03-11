class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService=None

    def afficherInformations(self):
        print(f"Permis : {self.numeroPermis}")
        print(f"Nom : {self.nom}")
        print(f"Prenom : {self.prenom}")
        if self.voitureService != None:
            print("voiture de service")
            self.voitureService.afficherInformations()
        else:
            print("il n'est pas voiture de service")
    def affecterVoiture(self, voiture):
        if self.voitureService != None:
            print(f"employe {self.nom} {self.prenom} a deja une voiture de service")
            return
        if voiture.chauffeur !=None:
            print(f" la voiture {voiture.matricule} est deja affecte pour un autre employe")
            return
        self.voitureService = voiture
        voiture.chauffeur = self
        print(f"la voiture {voiture.matricule} est deja affecte a {self.nom} {self.prenom}")

    def retirerVoiture(self):
        if self.voitureService != None:
            print(f"la voiture {self.voitureService.matricule} a ete retirer de {self.nom} {self.prenom}")
            self.voitureService.chauffeur = None
            self.voitureService = None
        else:
            print(f"{self.nom} {self.prenom} na pas voiture a retirer")
class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None
    def afficherInformations(self):
        print(f"matricule: {self.matricule}")
        print(f"annee: {self.annee}")
        print(f"marque: {self.marque}")
        print(f"kilometrage: {self.kilometrage}")
        if self.chauffeur != None:
            print(f"chauffeur: {self.chauffeur.nom} {self.chauffeur.prenom}")
        else:
            print("aucun chauffeur")

        e1=Employe("ON920", "CHERIF","berihan")
        e2=Employe("QC928", "CHERIFa","ber")
        e3=Employe("NB750", "CHEche","berhaha")

        v1=Voiture("Fv854","2021","audi","2100")
        v2=Voiture("Fv874","2023","honda","21550")
        v3=Voiture("LJ854","20235","honda","21547")

        e1.affecterVoiture(v1)
        e2.affecterVoiture(v2)
        e3.affecterVoiture(v3)

