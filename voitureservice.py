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


