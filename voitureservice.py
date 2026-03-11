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