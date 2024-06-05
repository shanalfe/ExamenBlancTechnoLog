class Magasin ():
   
    def __init__(self, type_musique) -> None:
        self.type_musique = type_musique
        self.vinyles = []
        self.dvds = []

    def ajouter_vinyle(self, vinyle):
        self.vinyles.append(vinyle)

    def ajouter_dvd(self, dvd):
        self.dvds.append(dvd)

    def afficher_vinyles(self):
        return self.vinyles
    
    def afficher_dvds(self):
        return self.dvds
    
    def retirer_vinyle(self, vinyle):
        if vinyle in self.vinyles:
            self.vinyles.remove(vinyle)
        else:
            print("Ce vinyle n'est pas dans le magasin")

    def retirer_dvd(self, dvd):
        if dvd in self.dvds:
            self.dvds.remove(dvd)
        else:
            print("Ce dvd n'est pas dans le magasin")