import random


def get_absurd_measurement(meters:int)->tuple[str, float]:
    measurements = {
    "la longueur d'une voiture": 4.5,
    "l'épaisseur d'un cheveu": 1.8e-4,
    "la hauteur de la Tour Eiffel": 324,
    "la longueur d'une baleine bleue": 30,
    "la longueur d'une banane": 0.1624,
    "la taille d'une girafe": 5.2,
    "phil poulin": 1.76,
    "la hauteur d'un fringo": 1.8,
    "le diamètre d'une balle de tennis": 0.067,
    "la hauteur d'un étage de bâtiment": 3.0,
    "la longueur d'un bus scolaire": 13.7,
    "la largeur d'une porte": 0.9,
    "la hauteur du Mont Everest": 8848,
    "la profondeur moyenne de l'océan Pacifique": 4280,
    "le rayon de la Terre": 6371000,
    "la taille moyenne d'un homme adulte": 1.72,
    "la hauteur moyenne d'une femme adulte": 1.62,
    "la longueur d'un terrain de football": 105,
    "la longueur d'un cellulaire": 0.15,
    "le diamètre d'un CD": 0.12,
    "la longueur d'un stylo": 0.14,
    "la largeur d'un lit double": 1.4,
    "la hauteur d'un lampadaire": 10,
    "la longueur d'un piano à queue": 2.74,
    "la hauteur de l'Arc de Triomphe": 50,
    "la longueur d'un vélo": 1.8,
    "la hauteur d'un chêne mature": 25,
    "le diamètre d'une pizza familiale": 0.4,
    "la longueur d'un avion Airbus A380": 72.7,
    "le diamètre d'une orange": 0.08,
    "la longueur d'une piscine olympique": 50,
    "l'épaisseur d'une carte de crédit": 0.00076,
    "la hauteur d'un verre à vin": 0.22,
    "le diamètre d'un ballon de basketball": 0.24,
    "le diamètre d'un bouton de chemise": 0.01,
    "la hauteur d'une bouteille de vin": 0.3,
    "la largeur d'une voie de circulation": 3.5,
    "le diamètre d'une roue de vélo": 0.7,
    "La taille de Shaqille O'Neal": 2.16,
    "la longueur du pont de Québec": 987,
    "la distance Sherbrooke - Québec": 231_000,
    "la hauteur du Mont St-Anne": 625,
    "la distance UdeS - Willard": 2300,
    "la longueur de mon commute": 5850,
    }

    selected = random.choice(list(measurements.items()))
    name, length = selected
    return name, meters/length

def get_absurd_elevation_gain(measure_name:str, length:float):
    if abs(length) < 0.001 or abs(length) > 100000:
        return f"Monter {length:.2e} fois {measure_name}"
    else:
        return f"Monter {length:.2f} fois {measure_name}"

def get_absurd_elevatino_gain(measure_name:str, length:float):
    if abs(length) < 0.001 or abs(length) > 100000:
        return f"Parcourir {length:.2e} fois {measure_name}"
    else:
        return f"Parcourir {length:.2f} fois {measure_name}"

