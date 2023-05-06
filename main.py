from unidecode import unidecode

# Partie 1 : Structure de données

class Sommet():
    def __init__(self, entrant: list, sortant: list, nom: str=""):
        """
        Crée un sommet avec ses arcs entrants et sortants et son nom (optionnel)
        :param entrant: liste des arcs entrants
        :param sortant: liste des arcs sortants
        :param nom: nom du sommet
        """
        self.entrant = entrant
        self.sortant = sortant
        self.nom = nom

class Arc():
    """
    Crée un arc avec son nom, sa nature et sa durée (optionnel)
    :param nom: nom de l'arc
    :param nature: nature de l'arc (téléski, télésiège, télécabine, téléphérique, piste verte, piste bleue, piste rouge, piste noire)
    :param duree_1: temps de parcours de la remontée ou de la piste pour un débutant (optionnel)
    :param duree_2: temps de parcours de la piste pour un fonceur (optionnel)
    """
    
    echelle = 3.059e-3 # échelle de la carte
    attente_remontees = 10
    v_remontees = {"téléski": 12.5, "télésiège": 15, "télécabine": 22.5, "téléphérique": 30}
    v_pistes = {"piste verte": [20, 20], "piste bleue": [17.5, 35], "piste rouge": [15, 45], "piste noire": [12.5, 50]} # [vitesse débutant, vitesse fonceur]

    def __init__(self, nom: str, nature: str, duree_1: float=0, duree_2: float=0):
        self.nature = nature
        self.nom = nom
        if self.nature == ("téléski" or "télésiège" or "télécabine" or "téléphérique"):
            self.duree = (duree_1 / self.echelle) / (self.v_remontees[self.nature] / 3.6) / 60 + self.attente_remontees
        elif self.nature == ("piste verte" or "piste bleue" or "piste rouge" or "piste noire"):
            self.duree_1 = (duree_1 / self.echelle) / (self.v_pistes[self.nature][0] / 3.6) / 60 # durée pour un débutant
            self.duree_2 = (duree_2 / self.echelle) / (self.v_pistes[self.nature][1] / 3.6) / 60 # durée pour un fonceur


arcs = {
    # Téléskis
    "PYRAMIDE": Arc("PYRAMIDE", "téléski", 3.2),
    "SOURCES": Arc("SOURCES", "téléski", ),
    "ROCHER DE L'OMBRE": Arc("ROCHER DE L'OMBRE", "téléski"),
    "PRAZ JUGET": Arc("PRAZ JUGET", "téléski"),
    "BOUC BLANC": Arc("BOUC BLANC", "téléski"),
    "GROS MURGER": Arc("GROS MURGER", "téléski"),
    "LOZE": Arc("LOZE", "téléski"),
    "STADE": Arc("STADE", "téléski", 1.1),
    "EPICEA": Arc("EPICEA", "téléski"),
    "MARQUIS": Arc("MARQUIS", "téléski", 4),
    "STE AGATHE": Arc("STE AGATHE", "téléski", 1.5),
    "STADE": Arc("STADE", "téléski"),
    "GRANGES": Arc("GRANGES", "téléski", 1.5),
    "COMBE": Arc("COMBE", "téléski", 1.7),
    "PTE BOSSE": Arc("PTE BOSSE", "téléski", 0.9),
    # Télésièges
    "CHANROSSA": Arc("CHANROSSA", "télésiège", 4.3),
    "ROC MERLET": Arc("ROC MERLET", "télésiège", 1.6),
    "ROC MUGNIER": Arc("ROC MUGNIER", "télésiège", 3.6),
    "CREUX NOIRS": Arc("CREUX NOIRS", "télésiège", 3.6),
    "MARMOTTES": Arc("MARMOTTES", "télésiège", 4.9),
    "SUISSES": Arc("SUISSES", "télésiège", 4.3),
    "BIOLLAY": Arc("BIOLLAY", "télésiège", 3.3),
    "PRALONG": Arc("PRALONG", "télésiège", 3.1),
    "COQS": Arc("COQS", "télésiège"),
    "COL DE LA LOZE": Arc("COL DE LA LOZE", "télésiège"),
    "DOU DES LANCHES": Arc("DOU DES LANCHES", "télésiège"),
    "CRÊTES": Arc("CRÊTES", "télésiège"),
    "PLANTREY": Arc("PLANTREY", "télésiège"),
    "TOVETS": Arc("TOVETS", "télésiège"),
    "3 VALLÉES": Arc("3 VALLÉES", "télésiège", 4.3),
    "CHAPELETS": Arc("CHAPELETS", "télésiège", 3.5), 
    "SIGNAL": Arc("SIGNAL", "télésiège", 4.5),
    "GRAVELLES": Arc("GRAVELLES", "télésiège", 2.2),
    "AIGUILLE DU FRUIT": Arc("AIGUILLE DU FRUIT", "télésiège", 4.6),
    # Télécabines
    "VIZELLE": Arc("VIZELLE", "télécabine", 3.8),
    "JARDIN ALPIN": Arc("JARDIN ALPIN", "télécabine"),
    "LA TANIA": Arc("LA TANIA", "télécabine"),
    "FORET": Arc("FORET", "télécabine"),
    "PRAZ": Arc("PRAZ", "télécabine"),
    "CHENUS": Arc("CHENUS", "télécabine"),
    "VERDONS": Arc("VERDONS", "télécabine"),
    "GRANGETTES": Arc("GRANGETTES", "télécabine"),
    "ARIONDAZ": Arc("ARIONDAZ", "télécabine", 5.6),
    # Téléphériques
    "SAULIRE": Arc("SAULIRE", "téléphérique", 4.1),
    # Pistes vertes
    "Renard": Arc("Renard", "piste verte"),
    "Verdons A": Arc("Verdons A", "piste verte"),
    "Verdons B": Arc("Verdons B", "piste verte"),
    "Lac Bleu": Arc("Lac Bleu", "piste verte"),
    "Loze Est": Arc("Loze Est", "piste verte"),
    "Plan Fontaine A": Arc("Plan Fontaine A", "piste verte"),
    "Plan Fontaine B": Arc("Plan Fontaine B", "piste verte"),
    "Belvédère": Arc("Belvédère", "piste verte", 3.2),
    "Praline A": Arc("Praline A", "piste verte", 3),
    "Praline B": Arc("Praline B", "piste verte", 2.5),
    # Pistes bleues
    "Plan Mugnier": Arc("Plan Mugnier", "piste bleue", 3.2),
    "Mont Russes": Arc("Mont Russes", "piste bleue", 3.2),
    "Pyramide": Arc("Pyramide", "piste bleue", 3.2),
    "Altiport A": Arc("Altiport A", "piste bleue", 0.7),
    "Altiport B": Arc("Altiport B", "piste bleue", 2.4),
    "Altiport C": Arc("Altiport C", "piste bleue", 1.2),
    "Super Pralong": Arc("Super Pralong", "piste bleue", 1.8),
    "Pralong A": Arc("Pralong A", "piste bleue", 1.7),
    "Pralong B": Arc("Pralong B", "piste bleue", 1.8),
    "Biollay Verdons A": Arc("Biollay Verdons A", "piste bleue", 1.8),
    "Biollay Verdons B": Arc("Biollay Verdons B", "piste bleue", 1.7),
    "Biollay": Arc("Biollay", "piste bleue", 3.2),
    "Anémones": Arc("Anémones", "piste bleue"),
    "Col de la Loze": Arc("Col de la Loze", "piste bleue"),
    "Folyères": Arc("Folyères", "piste bleue"),
    "Arolles A": Arc("Arolles A", "piste bleue"),
    "Arolles B": Arc("Arolles B", "piste bleue"),
    "Crêtes A": Arc("Crêtes A", "piste bleue"),
    "Crêtes B": Arc("Crêtes B", "piste bleue"),
    "Stade": Arc("Stade", "piste bleue"),
    "Tovets": Arc("Tovets", "piste bleue"),
    "Provères": Arc("Provères", "piste bleue"),
    "Cospillot": Arc("Cospillot", "piste bleue"),
    "Piste Bleue": Arc("Piste Bleue", "piste bleue", 4.1),
    "Marquis": Arc("Marquis", "piste bleue", 4.1),
    "Granges": Arc("Granges", "piste bleue", 1.5),
    "Carabosse": Arc("Carabosse", "piste bleue", 1.2),
    "Grandes Bosses A": Arc("Grandes Bosses A", "piste bleue", 1.8),
    "Grandes Bosses B": Arc("Grandes Bosses B", "piste bleue", 3),
    "Ariondaz": Arc("Ariondaz", "piste bleue", 1.7),
    "Indiens": Arc("Indiens", "piste bleue", 4.1),
    "Gravelles": Arc("Gravelles", "piste bleue", 0.6),
    "Prameruel": Arc("Prameruel", "piste bleue", 3.1),
    # Pistes rouges
    "Jean Pachod": Arc("Jean Pachod", "piste rouge", 4.4),
    "Roc Merlet": Arc("Roc Merlet", "piste rouge", 1.7),
    "Creux A": Arc("Creux A", "piste rouge", 6.2),
    "Creux B": Arc("Creux B", "piste rouge", 2.7),
    "Roc Mugnier": Arc("Roc Mugnier", "piste rouge", 3.6),
    "Lac Creux A": Arc("Lac Creux A", "piste rouge", 3.5),
    "Lac Creux B": Arc("Lac Creux B", "piste rouge", 2.6),
    "Roches Grises": Arc("Roches Grises", "piste rouge", 3.6),
    "Combe Saulire A": Arc("Combe Saulire A", "piste rouge", 1.3),
    "Combe Saulire B": Arc("Combe Saulire B", "piste rouge", 3.2),
    "Combe Saulire C": Arc("Combe Saulire C", "piste rouge", 1.2),
    "Park City": Arc("Park City", "piste rouge", 2.3),
    "Rama": Arc("Rama", "piste rouge", 1.5),
    "Stade Descente": Arc("Stade Descente", "piste rouge"),
    "Marquetty": Arc("Marquetty", "piste rouge", 3.4),
    "Cave des Creux": Arc("Cave des Creux", "piste rouge", 2.2),
    "Mur": Arc("Mur", "piste rouge", 2.8),
    "Lanches": Arc("Lanches", "piste rouge"),
    "Bouc Blanc A": Arc("Bouc Blanc A", "piste rouge"),
    "Bouc Blanc B": Arc("Bouc Blanc B", "piste rouge"),
    "Moretta Blanche": Arc("Moretta Blanche", "piste rouge"),
    "Murettes": Arc("Murettes", "piste rouge"),
    "Amoureux": Arc("Amoureux", "piste rouge"),
    "Saint Bon": Arc("Saint Bon", "piste rouge"),
    "Brigues": Arc("Brigues", "piste rouge"),
    "Loze": Arc("Loze", "piste rouge"),
    "Dou du Midi": Arc("Dou du Midi", "piste rouge"),
    "Petit Dou": Arc("Petit Dou", "piste rouge"),
    "Jantzen": Arc("Jantzen", "piste rouge"),
    "Chenus": Arc("Chenus", "piste rouge"),
    "Déviation 1550": Arc("Déviation 1550", "piste rouge"),
    "Stade": Arc("Stade", "piste rouge", 1.1),
    "Bel Air": Arc("Bel Air", "piste rouge", 2.1),
    "Rochers A": Arc("Rochers A", "piste rouge", 2.8),
    "Rochers B": Arc("Rochers B", "piste rouge", 2.1),
    "Chapelets": Arc("Chapelets", "piste rouge", 3.5),
    # Pistes noires
    "Chanrossa": Arc("Chanrossa", "piste noire", 4.45),
    "Turcs A": Arc("Turcs A", "piste noire", 2.3),
    "Turcs B": Arc("Turcs B", "piste noire", 2.3),
    "Suisses": Arc("Suisses", "piste noire", 4.6),
    "Combe Pylones": Arc("Combe Pylones", "piste noire", 3.2),
    "Grand Couloir": Arc("Grand Couloir", "piste noire", 3.2),
    "m": Arc("m", "piste noire", 4),
    "Dou des Lanches": Arc("Dou des Lanches", "piste noire"),
    "Jockeys": Arc("Jockeys", "piste noire"),
    "Jean Blanc": Arc("Jean Blanc", "piste noire"),
}

print(arcs["PYRAMIDE"].duree)

sommets = [
    Sommet(
        [arcs["CHANROSSA"], arcs["ROC MERLET"]],
        [arcs["Chanrossa"], arcs["Jean Pachod"], arcs["Roc Merlet"]],
        "CHANROSSA"
    ),
    Sommet(
        [arcs["Creux A"], arcs["Jean Pachod"], arcs["Chanrossa"], arcs["Rama"]],
        [arcs["CHANROSSA"], arcs["MARMOTTES"], arcs["Creux B"]],
        "CREUX"
    ),
    Sommet(
        [arcs["Roc Mugnier"], arcs["Creux B"], arcs["Gravelles"], arcs["Cave des Creux"], arcs["Mur"], arcs["Prameruel"]],
        [arcs["ROC MUGNIER"], arcs["AIGUILLE DU FRUIT"], arcs["GRAVELLES"]],
        "PRAMEUEL"
    ),
    Sommet(
        [arcs["ROC MUGNIER"], arcs["COMBE"], arcs["Pyramide"], arcs["Mont Russes"], arcs["Plan Mugnier"], arcs["Grandes Bosses A"]],
        [arcs["Roc Mugnier"], arcs["PYRAMIDE"], arcs["Grandes Bosses B"]]
    ),
    Sommet(
        [arcs["PYRAMIDE"], arcs["Roc Merlet"]],
        [arcs["Plan Mugnier"], arcs["Mont Russes"], arcs["Pyramide"], arcs["ROC MERLET"]]
    ),
    Sommet(
        [arcs["CREUX NOIRS"]],
        [arcs["Roches Grises"]],
        "CREUX NOIRS"
    ),
    Sommet(
        [arcs["SAULIRE"]],
        [arcs["Grand Couloir"], arcs["Creux A"], arcs["Combe Saulire A"], arcs["Lac Creux A"]],
        "SAULIRE"
    ),
    Sommet(
        [arcs["MARMOTTES"], arcs["SUISSES"], arcs["VIZELLE"], arcs["Combe Saulire B"]],
        [arcs["Combe Saulire B"], arcs["Combe Pylones"], arcs["m"], arcs["Turcs A"], arcs["Suisses"]],
        "VIZELLE"
    ),
    Sommet(
        [arcs["Combe Pylones"], arcs["Combe Saulire C"], arcs["Grand Couloir"], arcs["Biollay Verdons A"], arcs["m"], arcs["VERDONS"], arcs["SOURCES"]],
        [arcs["VIZELLE"], arcs["SAULIRE"], arcs["Verdons A"], arcs["Renard"], arcs["Biollay Verdons B"]],
        "VERDONS"
    ),
    Sommet(
        [arcs["Combe Saulire B"], arcs["Grand Couloir"], arcs["ROCHER DE L'OMBRE"]],
        [arcs["Stade Descente"], arcs["Combe Saulire C"]]
    ),
    Sommet(
        [arcs["Lac Creux A"]],
        [arcs["Lac Creux B"], arcs["CREUX NOIRS"]]
    ),
    Sommet(
        [arcs["Turcs A"], arcs["AIGUILLE DU FRUIT"]],
        [arcs["Turcs B"], arcs["Park City"]]
    ),
    Sommet(
        [arcs["GRAVELLES"], arcs["Lac Creux B"], arcs["Park City"]],
        [arcs["Cave des Creux"], arcs["Altiport A"]]
    ),
    Sommet(
        [arcs["Turcs B"], arcs["Suisses"], arcs["Altiport B"], arcs["Super Pralong"]],
        [arcs["SUISSES"], arcs["Mur"], arcs["Altiport C"]]
    ),
    Sommet(
        [arcs["PRALONG"]],
        [arcs["Super Pralong"], arcs["Pralong A"], arcs["Biollay Verdons A"], arcs["Marquetty"], arcs["Biollay"]]
    ),
    Sommet(
        [arcs["Pralong A"], arcs["Altiport A"]], # ajouter ALTIPORT
        [arcs["Prameruel"], arcs["Pralong B"], arcs["Altiport B"]]
    ),
    Sommet(
        [arcs["JARDIN ALPIN"], arcs["Biollay Verdons B"]],
        []
    ),
    Sommet(
        [arcs["Biollay"], arcs["Altiport C"], arcs["Pralong B"]],
        [arcs["PRALONG"]], # ajouter ALTIPORT
        "PRALONG"
    ),
    Sommet(
        [arcs["COQS"], arcs["CHENUS"], arcs["CRÊTES"], arcs["PRAZ JUGET"], arcs["Col de la Loze"]],
        [arcs["Crêtes A"], arcs["Lanches"], arcs["Chenus"], arcs["Anémones"], arcs["COL DE LA LOZE"], arcs["Lac Bleu"]],
        "CHENUS"
    ),
    Sommet(
        [arcs["COL DE LA LOZE"], arcs["DOU DES LANCHES"]],
        [arcs["Col de la Loze"], arcs["Dou des Lanches"]],
        "COL DE LA LOZE"
    ),
    Sommet(
        [arcs["Crêtes A"], arcs["LOZE"], arcs["PLANTREY"], arcs["BOUC BLANC"]],
        [arcs["Crêtes B"], arcs["Loze Est"], arcs["Loze"], arcs["Dou du Midi"], arcs["Petit Dou"], arcs["Jean Blanc"], arcs["Bouc Blanc A"], arcs["Déviation 1550"]],
        "LOZE"
    ),
    Sommet(
        [arcs["Crêtes B"], arcs["FORET"]],
        [arcs["CRÊTES"], arcs["Arolles A"]]
    ),
    Sommet(
        [arcs["Dou des Lanches"], arcs["Bouc Blanc A"], arcs["Arolles A"], arcs["LA TANIA"]],
        [arcs["DOU DES LANCHES"], arcs["PRAZ JUGET"], arcs["Arolles B"], arcs["Bouc Blanc B"], arcs["Plan Fontaine A"], arcs["Jockeys"], arcs["Murettes"]],
        "PRAZ JUGET"
    ),
    Sommet(
        [arcs["Arolles B"], arcs["Bouc Blanc B"], arcs["Plan Fontaine A"], arcs["GROS MURGER"]],
        [arcs["BOUC BLANC"], arcs["Plan Fontaine B"], arcs["Moretta Blanche"], arcs["Folyères"]]
    ),
    Sommet(
        [arcs["Folyères"], arcs["Plan Fontaine B"], arcs["Moretta Blanche"]],
        [arcs["GROS MURGER"], arcs["LA TANIA"]],
        "LA TANIA"
    ),
    Sommet(
        [arcs["Brigues"], arcs["Amoureux"], arcs["Jockeys"], arcs["Murettes"], arcs["Jean Blanc"]],
        [arcs["Saint Bon"], arcs["PRAZ"], arcs["FORET"]],
        "COURCHEVEL - LE PRAZ - 1300m"
    ),
    Sommet(
        [arcs["Saint Bon"]],
        [],
        "ST BON - 1100m"
    ),
    Sommet(
        [arcs["Déviation 1550"], arcs["Dou du Midi"], arcs["Stade"], arcs["Provères"], arcs["Tovets"]],
        [arcs["TOVETS"], arcs["GRANGETTES"]],
        "COURCHEVEL - 1550m"
    ),
    Sommet(
        [arcs["Verdons B"], arcs["Anémones"], arcs["Jantzen"], arcs["Loze"], arcs["GRANGETTES"], arcs["TOVETS"], arcs["Petit Dou"]],
        # On considère que seul Verdons relie Lac à ce sommet
        [arcs["JARDIN ALPIN"], arcs["VERDONS"], arcs["LOZE"], arcs["CHENUS"], arcs["Stade"], arcs["Tovets"], arcs["Provères"], arcs["Brigues"], arcs["Amoureux"]]
    ),
    Sommet(
        [arcs["Marquetty"], arcs["Renard"], arcs["Verdons A"], arcs["Stade Descente"], arcs["Loze Est"], arcs["Lac Bleu"], arcs["Chenus"]],
        [arcs["BIOLLAY"], arcs["SOURCES"], arcs["ROCHER DE L'OMBRE"], arcs["COQS"], arcs["Verdons B"]],
        "LAC"
    ),
    Sommet(
        [arcs["Piste Bleue"], arcs["Marquis"], arcs["Indiens"], arcs["Belvédère"]],
        [arcs["3 VALLÉES"], arcs["MARQUIS"], arcs["STE AGATHE"], arcs["ARIONDAZ"]],
        "COURCHEVEL - 1650m"
    ),
    Sommet(
        [arcs["Stade"], arcs["Granges"], arcs["Carabosse"], arcs["Praline B"]],
        [arcs["STADE"], arcs["GRANGES"], arcs["Belvédère"]]
    ),
    Sommet(
        [arcs["Chapelets"], arcs["Rochers B"], arcs["Bel Air"], arcs["Praline A"]],
        [arcs["Praline B"], arcs["CHAPELETS"]]
    ),
    Sommet(
        [arcs["CHAPELETS"], arcs["SIGNAL"]],
        [arcs["Chapelets"], arcs["Rochers A"], arcs["Grandes Bosses A"]],
        "SIGNAL"
    ),
    Sommet(
        [arcs["Rochers A"], arcs["ARIONDAZ"]],
        [arcs["COMBE"], arcs["Rochers B"], arcs["Bel Air"], arcs["Ariondaz"]],
        "BEL AIR"
    ),
    Sommet(
        [arcs["Ariondaz"], arcs["GRANGES"], arcs["MARQUIS"], arcs["3 VALLÉES"], arcs["Grandes Bosses B"]],
        [arcs["SIGNAL"], arcs["Granges"], arcs["Carabosse"], arcs["Praline A"], arcs["PTE BOSSE"], arcs["Indiens"], arcs["Piste Bleue"], arcs["Marquis"]],
        "BOSSES"
    ),
    Sommet(
        [arcs["PTE BOSSE"]],
        [arcs["Gravelles"]]
    ),
    Sommet(
        [arcs["STADE"]],
        [arcs["Stade"]]
    )
]

# Exemple

def afficher_sommets_adjacents():
    print("Requête type : Je suis en haut de Chanrossa.")
    input_utilisateur = input("Où êtes-vous ? ")
    input_utilisateur = input_utilisateur.strip(".").split(" ")
    indice_localisation = input_utilisateur.index("de")
    localisation = " ".join(input_utilisateur[indice_localisation+1:])
    #print(localisation)
    sommet_localisation = None
    if "haut" in input_utilisateur:
        i = 0
        while sommet_localisation is None:
            if arcs[localisation] in sommets[i].entrant:
                sommet_localisation = sommets[i]
        i += 1
    elif "bas" in input_utilisateur:
        pass
    print(sommet_localisation)
    print(sommets[0])

#afficher_sommets_adjacents()

def ecrire_arcs(arcs, nom_fichier):
    """
    Écrit les arcs dans un fichier texte.
    :arcs: liste d'arcs
    :nom_fichier: nom du fichier dans lequel écrire
    :return: None
    """
    with open(nom_fichier, 'w') as f:
        for arc in arcs.values():
            nom_sans_accents = unidecode(arc.nom)
            nature_sans_accents = unidecode(arc.nature)
            f.write(f"{{'nom': '{nom_sans_accents}', 'nature': '{nature_sans_accents}'}}\n")

def ecrire_sommets(sommets, nom_fichier):
    """
    Écrit les sommets dans un fichier texte.
    :sommets: liste de sommets
    :nom_fichier: nom du fichier dans lequel écrire
    :return: None
    """
    with open(nom_fichier, 'w') as f:
        for sommet in sommets:
            entrant = [unidecode(arc.nom) for arc in sommet.entrant]
            sortant = [unidecode(arc.nom) for arc in sommet.sortant]
            nom = unidecode(sommet.nom) if sommet.nom else ""
            entrant_str = str(entrant)
            sortant_str = str(sortant)
            nom_str = f"'nom': '{nom}'" if nom else ""
            f.write(f"{{'entrant': {entrant_str}, 'sortant': {sortant_str}, {nom_str}}}\n")

ecrire_arcs(arcs, "liste_pistes.txt")
ecrire_sommets(sommets, "liste_sommets.txt")