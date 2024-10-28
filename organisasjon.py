# organisasjon.py
import json

# JSON-data som en streng
json_data = """
[
{"navn":"Donald Duck","stilling":"Floor worker","avdeling":"Production","sjef":"Skrue Duck"},
{"navn":"Ole Duck","stilling":"Trainee","avdeling":"Production","sjef":"Skrue Duck"},
{"navn":"Dole Duck","stilling":"Trainee","avdeling":"Production","sjef":"Skrue Duck"},
{"navn":"Doffen Duck","stilling":"Trainee","avdeling":"Production","sjef":"Skrue Duck"},
{"navn":"Anton Duck","stilling":"Sales","avdeling":"Sales","sjef":"Skrue Duck"},
{"navn":"Skrue Duck","stilling":"CEO","avdeling":"HR","sjef":""},
{"navn":"Bestemor Duck","stilling":"HR","avdeling":"HR","sjef":"Skrue Duck"}
]
"""

# Konverter JSON-strengen til et Python-objekt
data = json.loads(json_data)

class Person:
    def __init__(self, navn, sjef=None, avdeling=None, prosjekter=None):
        self.navn = navn
        self.sjef = sjef
        self.avdeling = avdeling
        self.prosjekter = prosjekter

def les_organisasjon_fra_json():
    """Itierer personer fra json_data.

    Args:
        filnavn: Ingen.

    Returns:
        En liste med objekter som representerer personer i organisasjonen.
    """

    personer = []
    for person_data in data:
        person = Person(
            person_data['navn'],
            person_data.get('sjef'),
            person_data.get('avdeling'),
            person_data.get('prosjekter', [])  # Standardverdi for prosjekter hvis ikke angitt
        )
        personer.append(person)

    return personer